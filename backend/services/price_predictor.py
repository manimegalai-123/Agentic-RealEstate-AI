import joblib
import pandas as pd

price_model = joblib.load("models/price_model.pkl")
columns = joblib.load("models/model_columns.pkl")


def predict_price(feature_dict):

    x = pd.DataFrame([feature_dict])

    x = x.reindex(columns=columns, fill_value=0)

    price = price_model.predict(x)[0]

    return round(price, 2)