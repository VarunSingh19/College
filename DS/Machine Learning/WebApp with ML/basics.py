# Readiing a Covid Data of WHO...

import pandas as pd
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import matplotlib.pyplot as plt

# Disable insecure request warning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# Define the URL for data download
url = "https://covid19.who.int/WHO-COVID-19-global-data.csv"

try:
    # Download the file using requests
    response = requests.get(url, verify=False)
    response.raise_for_status()  # Check for any errors in the request
    # Save the downloaded content to a local file
    with open('WHO-COVID-19-global-data.csv', 'wb') as file:
        file.write(response.content)
except requests.exceptions.RequestException as e:
    print("Error fetching data:", e)
    exit()

# Read the data into a DataFrame
data = pd.read_csv('WHO-COVID-19-global-data.csv')

# Plotting total COVID-19 cases over time
plt.figure(figsize=(8, 6))
for country_code, country_data in data.groupby('Country_code'):
    plt.plot(country_data['Date_reported'], country_data['Cumulative_cases'], label=country_code)
plt.xlabel('Date Reported')
plt.ylabel('Cumulative Cases')
plt.title('COVID-19 Cases Over Time')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Calculate daily new cases
data['Date_reported'] = pd.to_datetime(data['Date_reported'])
data = data.sort_values(['Country_code', 'Date_reported'])
data['Daily_new_cases'] = data.groupby('Country_code')['New_cases'].diff().fillna(0)

# Plotting daily new cases over time
plt.figure(figsize=(8, 6))
for country_code, country_data in data.groupby('Country_code'):
    plt.plot(country_data['Date_reported'], country_data['Daily_new_cases'], label=country_code)
plt.xlabel('Date Reported')
plt.ylabel('Daily New Cases')
plt.title('Daily New COVID-19 Cases Over Time')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Grouping by WHO region and calculating total deaths
total_deaths_by_region = data.groupby('WHO_region')['Cumulative_deaths'].max().sort_values(ascending=False)

# Plotting total deaths by WHO region
plt.figure(figsize=(8, 6))
total_deaths_by_region.plot(kind='bar', color='skyblue')
plt.xlabel('WHO Region')
plt.ylabel('Total Deaths')
plt.title('Total COVID-19 Deaths by WHO Region')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
