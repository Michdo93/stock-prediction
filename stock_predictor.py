import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

class StockPredictor:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.model = None
        self.train_model()

    def train_model(self):
        stock_data = pd.read_csv(self.csv_file)
        stock_data['Price_Rise'] = np.where(stock_data['Close'].shift(-1) > stock_data['Close'], 1, 0)
        stock_data = stock_data.dropna()
        X = stock_data[['Open', 'High', 'Low', 'Close']]
        y = stock_data['Price_Rise']
        X_train, _, y_train, _ = train_test_split(X, y, test_size=0.2, random_state=42)
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)
        self.model = model

    def predict(self, new_data):
        if self.model is None:
            print("Model for this stock is not trained yet.")
            return None
        prediction = self.model.predict(new_data)
        return prediction

    def make_prediction(self, new_data, stock_name):
        prediction = self.predict(new_data)
        if prediction is not None:
            if prediction == 1:
                print(f"Der Kurs von {stock_name} wird voraussichtlich steigen.")
            else:
                print(f"Der Kurs von {stock_name} wird voraussichtlich fallen.")
