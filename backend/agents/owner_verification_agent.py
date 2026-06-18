def owner_verification_agent(state):

    print("Owner verification started")

    # temporary verification
    state["owner_verified"] = True

    return state