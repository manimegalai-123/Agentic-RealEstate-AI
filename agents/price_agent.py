from services.price_predictor import predict_price


def price_agent(state):

    print("Features =", state["features"])

    bedrooms = state["features"]["bedroom"]
    bathrooms = state["features"]["bathroom"]
    terrace = state["features"]["terrace"]
    yard = state["features"]["yard"]

    price = predict_price(
        location=state["location"],
        area=state["area"],
        floor=state["floor"],
        bedrooms=bedrooms,
        bathrooms=bathrooms,
        terrace=terrace,
        yard=yard,
        status=state["status"]
    )

    print("Predicted Price =", price)

    state["price"] = price

    return state