def feature_agent(state):

    labels = state["labels"]

    features = {
        "bathroom": labels.count("bathroom"),
        "bedroom": labels.count("bedroom"),
        "dining": labels.count("dining"),
        "gaming": labels.count("gaming"),
        "kitchen": labels.count("kitchen"),
        "laundry": labels.count("laundry"),
        "living": labels.count("living"),
        "office": labels.count("office"),
        "terrace": labels.count("terrace"),
        "yard": labels.count("yard")
    }

    state["features"] = features

    return state