from datetime import datetime, timedelta
import finnhub


finnhub_client = finnhub.Client(api_key="ckuqblpr01qmtr8lgnu0ckuqblpr01qmtr8lgnug")

# Get the current datetime
current_datetime = datetime.now()

# Datetime one year ago
one_year_ago = current_datetime - timedelta(days=365)

# Format the dates for the API call
from_date = one_year_ago.strftime("%Y-%m-%d")
to_date = current_datetime.strftime("%Y-%m-%d")

# Get company news for Apple (AAPL) from one year ago to today
news = finnhub_client.company_news('AAPL', _from=from_date, to=to_date)
news = news[:4]

for i in range(0, len(news)):
    del news[i]["category"]
    del news[i]["datetime"]
    del news[i]["id"]
    del news[i]["related"]
    del news[i]["source"]

print(news)