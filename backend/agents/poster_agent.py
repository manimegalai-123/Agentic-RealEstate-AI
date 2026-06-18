from services.poster_generator import generate_poster

def poster_agent(state):

    print("Poster agent started")

    poster_path = generate_poster(
        state["description"],
        state["price"]
    )

    state["poster"] = poster_path

    return state