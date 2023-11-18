from flask import Flask, render_template, request
import finnhub

app = Flask(__name__)

api_key = 'ckuqblpr01qmtr8lgnu0ckuqblpr01qmtr8lgnug'
finnhub_client = finnhub.Client(api_key=api_key)

def company_data(tick: str):
    profile_data = finnhub_client.company_profile2(symbol=tick)
    return profile_data

"""
expected output:
{
  "country": "US",
  "currency": "USD",
  "exchange": "NASDAQ/NMS (GLOBAL MARKET)",
  "ipo": "1980-12-12",
  "marketCapitalization": 1415993,
  "name": "Apple Inc",
  "phone": "14089961010",
  "shareOutstanding": 4375.47998046875,
  "ticker": "AAPL",
  "weburl": "https://www.apple.com/",
  "logo": "https://static.finnhub.io/logo/87cb30d8-80df-11ea-8951-00000000092a.png",
  "finnhubIndustry":"Technology"
}
"""

def suprise_earn(tick: str):
    pass

"""
expected output:
[
  {
    "actual": 1.88,
    "estimate": 1.9744,
    "period": "2023-03-31",
    "quarter": 1,
    "surprise": -0.0944,
    "surprisePercent": -4.7812,
    "symbol": "AAPL",
    "year": 2023
  },
  {
    "actual": 1.29,
    "estimate": 1.2957,
    "period": "2022-12-31",
    "quarter": 4,
    "surprise": -0.0057,
    "surprisePercent": -0.4399,
    "symbol": "AAPL",
    "year": 2022
  },
  {
    "actual": 1.2,
    "estimate": 1.1855,
    "period": "2022-09-30",
    "quarter": 3,
    "surprise": 0.0145,
    "surprisePercent": 1.2231,
    "symbol": "AAPL",
    "year": 2022
  }
]
"""

def financial_report(tick: str):
    pass

def predicitoin(tick: str):
    pass

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/company-data', methods=["POST"])
def receive_data():
    stock_name = request.form['stock_name']
    return render_template("result.html", stock_name=stock_name)

if __name__ == '__main__':
    app.run(debug=True)
