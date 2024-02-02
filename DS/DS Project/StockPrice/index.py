import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

def get_stock_price(stock_symbol):
    url = f"https://finance.yahoo.com/quote/{stock_symbol}"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # print(soup)
        stock_price_element = soup.find('div', {'class': 'D(ib) Mend(20px)'}).find('span')
        if stock_price_element:
            stock_price = stock_price_element.text
            return f"The current stock price of {stock_symbol} is: {stock_price}"
        else:
            return f"Unable to find the stock price element for {stock_symbol}."
    else:
        return f"Failed to retrieve data for {stock_symbol}. Status code: {response.status_code}"
stocks = ["META", "AAPL", "GOOGL", "AMZN", "MSFT", "TSLA", "IBM", "META", "NFLX", "NVDA", "V", "PYPL", "GS", "JPM", "BA", "CSCO", "INTC", "DIS", "GE", "WMT"]
stock_data = []
for stock_symbol in stocks:
    stock_info = get_stock_price(stock_symbol)
    stock_data.append(stock_info)

with open('stock_data.txt', 'w') as file:
    for stock_info in stock_data:
        file.write(stock_info + '\n')
prices = [float(info.split(":")[-1].strip().replace(',', '').replace(' USD', '')) for info in stock_data]
plt.figure(figsize=(10, 6))
plt.bar(stocks, prices, color='blue')
plt.title('Stock Prices')
plt.xlabel('Stock Symbols')
plt.ylabel('Stock Rate')
plt.show()
print("All stock data has been saved to stock_data.txt, and the graph has been displayed.")
