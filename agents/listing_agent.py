def listing_agent(state):

    if state["owner_verified"]:

        listing = {
            "price": state["price"],
            "description": state["description"],
            "poster": state["poster"],
            "status": "Listed"
        }

        state["listing"] = listing

    return state