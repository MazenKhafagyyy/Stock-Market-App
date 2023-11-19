import base64
from flask import Flask, render_template, request
import finnhub
from datetime import datetime, timedelta
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import io

app = Flask(__name__)

api_key = 'ckuqblpr01qmtr8lgnu0ckuqblpr01qmtr8lgnug'
finnhub_client = finnhub.Client(api_key=api_key)

def company_datas(tick):
    profile_data = finnhub_client.company_profile2(symbol=tick)
    return profile_data


def suprise_earn(tick: str):
    pass


def financial_report(tick: str):
    pass

def prices(tick):
    # Current datetime
    current_datetime = datetime.now()

    # Datetime one year ago
    one_year_ago = current_datetime - timedelta(days=365)

    # Convert both to Unix timestamps
    current_timestamp = int(current_datetime.timestamp())
    one_year_ago_timestamp = int(one_year_ago.timestamp())

    data = finnhub_client.stock_candles(tick, 'D', one_year_ago_timestamp, current_timestamp)

    stock_prices = data['c']
    print(type(stock_prices))
    return stock_prices

def graph_linear_reg(tick):
    # Current datetime
    current_datetime = datetime.now()

    # Datetime one year ago
    one_year_ago = current_datetime - timedelta(days=365)

    # Convert both to Unix timestamps
    current_timestamp = int(current_datetime.timestamp())
    one_year_ago_timestamp = int(one_year_ago.timestamp())

    finnhub_client = finnhub.Client(api_key="ckuqblpr01qmtr8lgnu0ckuqblpr01qmtr8lgnug")

    data = finnhub_client.stock_candles(tick, 'D', one_year_ago_timestamp, current_timestamp)

    stock_prices = data['c']

    # Create a corresponding time series (assuming each price corresponds to a new day)
    days = list(range(len(stock_prices)))

    # Reshape the data to fit the model
    X = np.array(days).reshape(-1, 1)
    y = np.array(stock_prices)

    # Create and fit the linear regression model
    model = LinearRegression()
    model.fit(X, y)

    # Coefficients
    slope = model.coef_[0]
    intercept = model.intercept_

    # Prepare data for plotting
    predicted_prices = model.predict(X)

    # Plot
    plt.figure(figsize=(12, 6))
    plt.scatter(X, y, color='blue', label='Actual Stock Prices')
    plt.plot(X, predicted_prices, color='red', label='Predicted Stock Prices (Linear Regression)')
    plt.title('Stock Prices vs. Days')
    plt.xlabel('Days')
    plt.ylabel('Stock Price')
    plt.legend()

    my_stringIObytes = io.BytesIO()
    plt.savefig(my_stringIObytes, format='jpg')
    my_stringIObytes.seek(0)
    my_base64_jpgData = base64.b64encode(my_stringIObytes.read()).decode()
    print(my_base64_jpgData)

    return my_base64_jpgData

def graph_suprise_earn(tick):
    data = (finnhub_client.company_earnings(tick, limit=5))

    # Create empty lists to store the 'period', 'actual', and 'estimate' values
    period_values = []
    actual_earn = []
    estimate_earn = []

    # Iterate through each dictionary in the list and extract the values
    for record in data:
        period_values.append(record['period'])
        actual_earn.append(record['actual'])
        estimate_earn.append(record['estimate'])

    # Setting up the bar chart
    X_axis = np.arange(len(period_values))

    # Create the figure before plotting
    fig = plt.figure(figsize=(10, 5))

    # Plot the bars
    plt.bar(X_axis - 0.2, actual_earn, 0.4, label='Actual')
    plt.bar(X_axis + 0.2, estimate_earn, 0.4, label='Estimate')

    # Set the x-axis labels and title, and show legend
    plt.xticks(X_axis, period_values)
    plt.xlabel('Period')
    plt.ylabel('Earnings')
    plt.title(f'{tick} Earnings: Actual vs Estimate')
    plt.legend()

    my_stringIObytes = io.BytesIO()
    plt.savefig(my_stringIObytes, format='jpg')
    my_stringIObytes.seek(0)
    my_base64_jpgData = base64.b64encode(my_stringIObytes.read()).decode()
    print(my_base64_jpgData)

    return my_base64_jpgData


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/company-data', methods=["POST"])
def receive_data():
    stock_name = request.form['stock_name']
    stock_prices = prices(stock_name)
    company_data = company_datas(stock_name)
    linear_reg_graph = graph_linear_reg(stock_name)
    suprise_earn_img = graph_suprise_earn(stock_name)
    return render_template(
        "result.html",
        company_data=company_data,
        stock_name=stock_name,
        stock_prices=stock_prices,
        linear_reg_graph=linear_reg_graph,
        suprise_earn_img=suprise_earn_img
    )

if __name__ == '__main__':
    app.run(debug=True)

