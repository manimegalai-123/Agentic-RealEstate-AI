from services.description_generator import generate_description


def description_agent(state):

    description = generate_description(
        state["features"],
        state["price"]
    )

    state["description"] = description

    return state