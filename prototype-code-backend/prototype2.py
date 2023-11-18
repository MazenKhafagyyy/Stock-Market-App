import finnhub
finnhub_client = finnhub.Client(api_key="ckuqblpr01qmtr8lgnu0ckuqblpr01qmtr8lgnug")

print(finnhub_client.financials_reported(symbol='AAPL', freq='annual'))