from services.price_predictor import predict_price


def price_agent(state):

    price = predict_price(state["features"])

    state["price"] = float(price)

    return state
