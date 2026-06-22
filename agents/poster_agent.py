from services.poster_generator import generate_poster

def poster_agent(state):

    print("Poster agent started")

    poster_path = generate_poster(

    image_path=state["images"][0],

    description=state["description"],

    price=state["price"],

    owner_name=state["owner_name"],

    phone=state["phone"],

    email=state["email"],

    location=state["location"],

    area=state["area"],

    floor=state["floor"],

    status=state["status"],

    bedrooms=state["features"]["bedroom"],

    bathrooms=state["features"]["bathroom"]
)
    state["poster"] = poster_path

    return state