A Streamlit-based exploratory data analysis (EDA) project that analyzes the last 30 trading days of selected stocks and compares their performance, volatility, trading activity, and relationship with market indices.

This project aims to perform Exploratory Data Analysis on the following companies:
- Apple Inc. (AAPL)
- Tesla, Inc. (TSLA)
- Reliance Industries (RELIANCE.NS)
- HDFC Bank (HDFCBANK.NS)

Instead of a CSV files, I used yfinance over here so that we can make future iterations of the project to perform such analysis for any and as many numbers of specified companies for any specified period of time.

## Features:

### 1️) Closing Price Comparison
- Compares stock price trends over the last 30 trading days.

### 2️) Trading Volume Comparison
- Visualizes activity levels.

### 3️) Daily Returns Calculation
- Computes percentage daily price changes.

### 4️) Volatility Ranking
- Measures risk using standard deviation of daily returns.

### 5️) Correlation Matrix
- Computes correlation between selected stocks.

### 6️) Growth vs Market Index
- Compares stock growth against:
  - S&P 500 (^GSPC) for US stocks
  - NIFTY 50 (^NSEI) for Indian stocks
- Analyzes market dependency.

## Libraries used:
- Streamlit
- Pandas
- Matplotlib
- yfinance

While GPT has been used and referred extensively in this project, I have learnt matplotlib and yfinance enough to make a similar project like this and am and will continue to learn pandas.
