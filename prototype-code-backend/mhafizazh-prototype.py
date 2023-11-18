import finnhub
from datetime import datetime, timedelta
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Current datetime
current_datetime = datetime.now()

# Datetime one year ago
one_year_ago = current_datetime - timedelta(days=365)

# Convert both to Unix timestamps
current_timestamp = int(current_datetime.timestamp())
one_year_ago_timestamp = int(one_year_ago.timestamp())

finnhub_client = finnhub.Client(api_key="ckuqblpr01qmtr8lgnu0ckuqblpr01qmtr8lgnug")

data = finnhub_client.stock_candles('AAPL', 'D', one_year_ago_timestamp, current_timestamp)

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
plt.show()


