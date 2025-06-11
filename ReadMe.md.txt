# 📈 Portfolio Optimization with YFinance and Python

This project demonstrates how to use Python to perform **portfolio optimization** on a set of stocks using historical price data. It includes:

- Downloading stock price data with `yfinance`
- Calculating daily returns, mean returns, and the covariance matrix
- Simulating 1,000 random portfolios to visualize the risk/return trade-off
- Identifying the **maximum Sharpe ratio** and **minimum volatility** portfolios
- Optimizing the portfolio using `scipy.optimize.minimize` with constraints

---

## 🛠️ Technologies Used

- Python
- yfinance – for fetching historical stock data
- pandas and numpy – for data handling
- matplotlib – for plotting the results
- scipy.optimize – for portfolio optimization

---

## 📊 Stocks Used

This analysis includes the following tickers:

- Johnson & Johnson (`JNJ`)
- Amazon (`AMZN`)
- JPMorgan Chase (`JPM`)
- Apple (`AAPL`)
- Exxon Mobil (`XOM`)

Historical data is downloaded for the period from **2020-01-01** to **2024-12-31**.

---

## 📈 Workflow Overview

1. **Download Price Data**  
   Use `yfinance` to fetch historical closing prices for selected stocks.

2. **Calculate Daily Returns**  
   Compute percentage change in prices to get daily returns.

3. **Estimate Statistics**  
   - Mean returns  
   - Covariance matrix of returns

4. **Simulate 1,000 Portfolios**  
   - Generate random weight combinations  
   - Calculate expected return, volatility, and Sharpe ratio for each  
   - Identify the portfolio with max Sharpe ratio and min volatility

5. **Visualize Efficient Frontier**  
   - Plot risk vs. return  
   - Highlight optimal portfolios

6. **Optimize Portfolio**  
   - Use `scipy.optimize.minimize` to find the weight combination that maximizes Sharpe ratio  
   - Apply constraints:  
     - Sum of weights = 1  
     - No weight > 40% (0.40) for any stock

7. **Display Optimized Results**  
   - Optimized weights  
   - Portfolio return and volatility

---

## 📊 Visualization

The plot includes:

- 1,000 simulated portfolios (colored by Sharpe ratio)  
- 🔴 Red star = Portfolio with **max Sharpe ratio**  
- 🔵 Blue star = Portfolio with **min volatility**

![Efficient Frontier](assets/efficient_frontier.png)

---

## ✅ Sample Output

```
Optimized Portfolio Weights: [0.20, 0.15, 0.30, 0.25, 0.10]
Optimized Portfolio Return: 0.00091
Optimized Portfolio Volatility: 0.01345
```

---

## 🚀 How to Run

### Clone the repository
```
git clone https://github.com/yourusername/portfolio-optimizer.git
cd portfolio-optimizer
```

### Install dependencies
```
pip install yfinance pandas numpy matplotlib scipy
```

### Run the script  
The script uses a clean `main()` function structure.
```
python portfolio_optimization.py
```

📌 Note: This version uses a self-contained `main()` function and performs simulation + optimization.  
Future updates will modularize the code and add CLI/config support.

---

## 🔧 TODO (Planned Improvements)

- Refactor into separate modules  
- Add input flexibility via CLI or config  
- Include unit tests  
- Add export to CSV/PDF

---

## 📁 File Overview

```
portfolio-optimizer/
├── portfolio_optimization.py     # Main script (initial version)
├── README.md                     # Project documentation
├── requirements.txt              # Dependencies
├── assets/
│   └── efficient_frontier.png    # Output plot (automatically generated)
```

---

## 📄 License

This project is licensed under the **MIT License**. You are free to use, modify, and distribute it.
