from flask import Flask, render_template
import finnhub

app = Flask(__name__)

api_key = 'ckuqblpr01qmtr8lgnu0ckuqblpr01qmtr8lgnug'
finnhub_client = finnhub.Client(api_key=api_key)

def company_data(tick: str) -> dict:
    pass

def suprise_earn(tick: str) -> dict:
    pass

def financial_report(tick: str) -> dict:
    pass

def predicitoin(tick: str):
    pass

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/company-data', methods=["POST"])
def receive_data():
    return render_template("result.html")

if __name__ == '__main__':
    app.run(debug=True)
