import ollama
from diffusers import StableDiffusionPipeline
from PIL import Image, ImageDraw, ImageFont
import torch

# CPU
pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5"
)

pipe = pipe.to("cpu")


def generate_poster(description, price):

    # -------------------------
    # Generate title + slogan
    # -------------------------
    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": f"""
Generate:

Title:
Slogan:

for a luxury real estate advertisement.

Description:
{description}
"""
            }
        ]
    )

    text = response["message"]["content"]

    lines = text.split("\n")

    title = "Luxury Dream Home"
    slogan = ""

    for line in lines:
        if "Title:" in line:
            title = line.replace("Title:", "").strip()

        if "Slogan:" in line:
            slogan = line.replace("Slogan:", "").strip()

    # -------------------------
    # Generate image
    # -------------------------

    prompt = f"""
Luxury modern house,
beautiful garden,
high quality architecture photography,
real estate advertisement
"""

    image = pipe(prompt).images[0]

    image.save("house_ai.png")

    # -------------------------
    # Create poster
    # -------------------------

    poster = Image.new("RGB", (1080, 1350), "white")

    house = Image.open("house_ai.png")
    house = house.resize((1000, 700))

    poster.paste(house, (40, 40))

    draw = ImageDraw.Draw(poster)

    title_font = ImageFont.truetype("arialbd.ttf", 60)
    price_font = ImageFont.truetype("arialbd.ttf", 45)
    normal_font = ImageFont.truetype("arial.ttf", 30)

    draw.text(
        (80, 800),
        title,
        fill="navy",
        font=title_font
    )

    draw.text(
        (80, 900),
        f"Price : ₹ {price:,.0f}",
        fill="green",
        font=price_font
    )

    draw.text(
        (80, 1000),
        slogan,
        fill="black",
        font=normal_font
    )

    draw.text(
        (80, 1120),
        "Contact : +91 9876543210",
        fill="black",
        font=normal_font
    )

    output = "posters/poster_3.png"

    poster.save(output)

    return output