from services.image_classifier import predict_room


def classification_agent(state):

    labels = []

    for image_path in state["images"]:
        labels.append(predict_room(image_path))

    state["labels"] = labels

    return state