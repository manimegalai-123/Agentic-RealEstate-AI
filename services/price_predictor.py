import joblib
import pandas as pd
import numpy as np

price_model = joblib.load("models/price_model.pkl")
columns = joblib.load("models/model_columns.pkl")


def predict_price(
        location,
        area,
        floor,
        bedrooms,
        bathrooms,
        terrace,
        yard,
        status):

    # Price per sq.ft according to city
    location_rates = {
        "coimbatore": 6000,
        "chennai": 9000,
        "bangalore": 12000,
        "hyderabad": 10000,
        "mumbai": 15000,
        "delhi": 11000
    }

    rate = location_rates.get(
        location.lower(),
        5000
    )

    # Base price
    price = area * rate

    # Bedroom contribution
    price += bedrooms * 8000

    # Bathroom contribution
    price += bathrooms * 3000

    # Floor contribution
    price += floor * 1000

    # Terrace bonus
    if terrace > 0:
        price += 5000

    # Yard bonus
    if yard > 0:
        price += 4000

    # Rent properties are cheaper
    if status.lower() == "rent":
        price = price * 0.1

    return round(price, 2)