import finnhub
import numpy as np
import matplotlib.pyplot as plt

finnhub_client = finnhub.Client(api_key="ckuqblpr01qmtr8lgnu0ckuqblpr01qmtr8lgnug")

data = (finnhub_client.company_earnings('TSLA', limit=5))


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
plt.title(f'TSLA Earnings: Actual vs Estimate')
plt.legend()

# Display the plot
plt.show()






