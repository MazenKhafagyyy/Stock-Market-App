from flask import Flask, render_template, request
import finnhub
from datetime import datetime, timedelta

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

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/company-data', methods=["POST"])
def receive_data():
    stock_name = request.form['stock_name']
    stock_prices = prices(stock_name)
    company_data = company_datas(stock_name)
    print(stock_prices)
    return render_template(
        "result.html",
        company_data=company_data,
        stock_name=stock_name,
        stock_prices=stock_prices
    )

if __name__ == '__main__':
    app.run(debug=True)

