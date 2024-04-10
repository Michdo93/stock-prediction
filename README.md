# stock-prediction
A simple Python programme that tries to make predictions about stocks.

## Pre-Installation

To make the programme run you have to install following packages via `pip`:

```
pip install pandas
pip install numpy
pip install scikit-learn
```

## Usage

You need a CSV file for each stock, which can look like this:

```
Date        Open      High      Low       Close
2024-04-01  100.00    105.00    99.50     104.20
2024-04-02  104.50    106.80    103.70    105.50
2024-04-03  105.70    107.20    104.80    106.00
...         ...       ...       ...       ...
```

The CSV file could contain data on historical share prices. Typically, this data would be in the form of a table with various columns.

The columns could be interpreted as follows:
- `Date`: The date on which the price was recorded.
- `Open`: The price at the beginning of the trading day.
- `High`: The highest price during the trading day.
- `Low`: The lowest price during the trading day.
- `Close`: The price at the end of the trading day.

`new_data` represents the price data for a new example for which a prediction is to be made. It should have the same structure as the historical data, i.e. an array with values for open, high, low and close. Here is a fictitious example of new_data:

```
new_data = np.array([[110.00, 112.50, 109.80, 111.20]])
```

This would mean that the price for the new example opened at 110.00, reached a high of 112.50, reached a low of 109.80 and closed at 111.20 at the close of trading.

At least your code can look like this:

```
from strock_predictor import StockPredictor

if __name__ == "__main__":
    vw_predictor = StockPredictor("vw.csv")
    daimler_trucks_predictor = StockPredictor("daimler_trucks.csv")

    # Vorhersage für VW
    new_data_vw = np.array([[110.00, 112.50, 109.80, 111.20]])
    vw_predictor.make_prediction(new_data_vw, "VW")

    # Vorhersage für Daimler Trucks
    new_data_daimler = np.array([[50.00, 52.00, 49.50, 51.20]])
    daimler_trucks_predictor.make_prediction(new_data_daimler, "Daimler Trucks")
```

The share prices are now also fictitious again. I have not checked the exact prices for this example. However, these are realistic values based on a rough estimate.
