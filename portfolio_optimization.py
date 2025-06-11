# # Note: This script is a simplified public version for educational/demo purposes.
# # For custom portfolios, different constraints, or integrations, please contact.
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize
import os

# --- Step 1: Download historical data ---
tickers = ['JNJ', 'AMZN', 'JPM', 'AAPL', 'XOM']
data = yf.download(tickers, start='2020-01-01', end='2024-12-31')['Close']
returns = data.pct_change().dropna()
returns = returns[tickers]  # Ensure correct order

# --- Step 2: Calculate statistics ---
mean_returns = returns.mean()
cov_matrix = returns.cov()

# --- Step 3: Simulate 1000 random portfolios ---
num_portfolios = 1000
results = np.zeros((3, num_portfolios))
for i in range(num_portfolios):
    weights = np.random.random(len(tickers))
    weights /= np.sum(weights)

    portfolio_return = np.dot(weights, mean_returns)
    portfolio_volatility = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
    sharpe_ratio = portfolio_return / portfolio_volatility

    results[0, i] = portfolio_return
    results[1, i] = portfolio_volatility
    results[2, i] = sharpe_ratio

# --- Step 4: Identify optimal portfolios ---
max_sharpe_idx = np.argmax(results[2])
min_volatility_idx = np.argmin(results[1])

# --- Step 5: Plot efficient frontier ---
os.makedirs("assets", exist_ok=True)

plt.figure(figsize=(10, 6))
plt.scatter(results[1], results[0], c=results[2], cmap='viridis', marker='o', s=10)
plt.scatter(results[1, max_sharpe_idx], results[0, max_sharpe_idx], color='red', marker='*', s=200, label='Max Sharpe Ratio')
plt.scatter(results[1, min_volatility_idx], results[0, min_volatility_idx], color='blue', marker='*', s=200, label='Min Volatility')
plt.xlabel('Volatility (Risk)')
plt.ylabel('Expected Return')
plt.title('1000 Portfolio Simulations')
plt.colorbar(label='Sharpe Ratio')
plt.legend()
plt.tight_layout()
plt.savefig("assets/efficient_frontier.png", dpi=300)
plt.show()

# --- Step 6: Optimize portfolio using scipy ---
def objective(weights, mean_returns, cov_matrix, risk_free_rate=0.02):
    ret = np.dot(weights, mean_returns)
    vol = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
    return -((ret - risk_free_rate) / vol)

constraints = [{'type': 'eq', 'fun': lambda w: np.sum(w) - 1}]
constraints += [{'type': 'ineq', 'fun': lambda w, i=i: 0.40 - w[i]} for i in range(len(tickers))]
bounds = [(0, 1)] * len(tickers)
initial_guess = [1.0 / len(tickers)] * len(tickers)

result = minimize(objective, initial_guess, args=(mean_returns, cov_matrix), method='SLSQP', bounds=bounds, constraints=constraints)
optimized_weights = result.x
optimized_return = np.dot(optimized_weights, mean_returns)
optimized_volatility = np.sqrt(np.dot(optimized_weights.T, np.dot(cov_matrix, optimized_weights)))

print("\n✅ Optimized Portfolio Weights:")
for t, w in zip(tickers, optimized_weights):
    print(f"{t}: {w:.4f}")
print(f"\n📈 Expected Return: {optimized_return:.4f}")
print(f"📉 Expected Volatility: {optimized_volatility:.4f}")

# # --- Optional: Save results to CSV (disabled by default) ---
# def save_optimized_results(tickers, weights, ret, vol, filename="output/optimized_results.csv"):
    
#     os.makedirs("output", exist_ok=True)
#     df = pd.DataFrame({"Ticker": tickers, "Weight": weights})
#     df.loc[len(df.index)] = ["Expected Return", ret]
#     df.loc[len(df.index)] = ["Expected Volatility", vol]
#     df.to_csv(filename, index=False)
#     print(f"\n💾 Results saved to: {filename}")

# #Uncomment to export results:
# save_optimized_results(tickers, optimized_weights, optimized_return, optimized_volatility)