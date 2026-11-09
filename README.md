
# Stock Portfolio Tracker

A simple Python-based Stock Portfolio Tracker that allows users to add stocks, manage share quantities, and calculate the total portfolio value using predefined stock prices.

## Features

- Displays available stocks and their prices.
- Allows users to add multiple stocks in one session.
- Accepts stock quantities.
- Calculates individual stock values.
- Calculates the total portfolio value.
- Handles invalid stock symbols.
- Validates incorrect and negative quantities.
- Combines quantities when the same stock is added multiple times.
- Displays a portfolio summary.

## Technologies Used

- Python 3
- VS Code

## Available Stocks

| Stock Symbol | Price |
|---|---:|
| AAPL | $180 |
| TSLA | $250 |
| GOOGL | $140 |
| MSFT | $400 |
| AMZN | $170 |

## How to Run

1. Clone or download this repository.
2. Open the project folder in VS Code.
3. Open the terminal.
4. Run the following command:

```bash
python main.py
```

5. Enter stock symbols and quantities.
6. Type `DONE` to finish and view the portfolio summary.

## Sample Calculation

| Stock | Quantity | Total Value |
|---|---:|---:|
| AAPL | 5 | $900 |
| TSLA | 2 | $500 |
| GOOGL | 3 | $420 |
| MSFT | 1 | $400 |

**Total Portfolio Value: $2,220**

## Project Structure

```text
CodeAlpha_StockPortfolioTracker/
│
├── main.py
├── README.md
└── .gitignore
```

## Author

Developed as part of the CodeAlpha Python Programming Internship.

## Note

This project uses predefined sample stock prices for portfolio calculations. It does not fetch live market prices.
