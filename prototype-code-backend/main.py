import finnhub

finnhub_client = finnhub.Client(api_key="clchjghr01qk5dvql6cgclchjghr01qk5dvql6d0")
def company_data(tick: str):
    profile_data = finnhub_client.company_profile2(symbol=tick)
    return profile_data


profile_data = company_data("AAPL")   # AAPL is the ticker for Apple Inc. as an example
for key, value in profile_data.items():
        print(f"{key}: {value}")

