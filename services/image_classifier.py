import torch
import torch.nn as nn
from torchvision.models import efficientnet_b0
from torchvision import transforms
from PIL import Image

# Class names in EXACT training order
classes = [
    "bathroom",
    "bedroom",
    "dining",
    "gaming",
    "kitchen",
    "laundry",
    "living",
    "office",
    "terrace",
    "yard"
]

# Image preprocessing
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor()
])

# Create EfficientNetB0 architecture
model = efficientnet_b0(weights=None)

# Replace classifier layer with 10 outputs
model.classifier[1] = nn.Linear(
    model.classifier[1].in_features,
    10
)

# Load trained weights
model.load_state_dict(
    torch.load(
        "models/room1_model.pth",
        map_location=torch.device("cpu")
    )
)

# Evaluation mode
model.eval()


def predict_room(image_path):

    image_path = image_path.replace("\\", "/")

    if image_path.startswith("backend/"):
        image_path = image_path[len("backend/"):]

    image = Image.open(image_path).convert("RGB")

    image = transform(image)
    image = image.unsqueeze(0)

    with torch.no_grad():
        output = model(image)
        pred = torch.argmax(output, dim=1)

    return classes[pred.item()]