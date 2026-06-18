from services.image_classifier import predict_room
from services.feature_extractor import extract_features
from services.price_predictor import predict_price
from services.description_generator import generate_description

def process_property(image_paths):

    labels = []

    for path in image_paths:

        room = predict_room(path)

        labels.append(room)

    features = extract_features(labels)

    price = predict_price(features)

    description = "Test description"

    return {
        "labels": labels,
        "features": features,
        "predicted_price": float(price),
        "description": description

    }