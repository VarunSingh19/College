library(rvest)
library(ggplot2)

get_stock_price <- function(stock_symbol) {
  url <- paste0("https://finance.yahoo.com/quote/", stock_symbol)
  webpage <- read_html(url)
  
  stock_price_element <- html_nodes(webpage, xpath = '//div[contains(@class, "D(ib) Mend(20px)")]//span')
  
  if (length(stock_price_element) > 0) {
    stock_price <- html_text(stock_price_element)
    return(paste("The current stock price of", stock_symbol, "is:", stock_price))
  } else {
    return(paste("Unable to find the stock price element for", stock_symbol, "."))
  }
}

stocks <- c("META", "AAPL", "GOOGL", "AMZN", "MSFT", "TSLA", "IBM", "META", "NFLX", "NVDA", "V", "PYPL", "GS", "JPM", "BA", "CSCO", "INTC", "DIS", "GE", "WMT")
stock_data <- vector("character", length = length(stocks))

for (i in seq_along(stocks)) {
  stock_data[i] <- get_stock_price(stocks[i])
}

writeLines(stock_data, "stock_data.txt")

prices <- as.numeric(gsub("[^0-9.]+", "", sapply(strsplit(stock_data, ":"), function(x) x[2])))
bar_colors <- ifelse(prices > 0, "blue", "red")

barplot(prices, names.arg = stocks, col = bar_colors, main = "Stock Prices", xlab = "Stock Names", ylab = "Stock Rate")
print("All stock data has been saved to stock_data.txt, and the graph has been displayed.")

# To view the contents of the 'stock_data.txt' file, you can use the 'readLines()' function:
file_path <- "stock_data.txt"
stock_data_content <- readLines(file_path)
print(stock_data_content)

