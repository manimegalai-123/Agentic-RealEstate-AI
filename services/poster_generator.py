import os
import textwrap
import ollama
from PIL import Image, ImageDraw, ImageFont


def generate_poster(
        image_path,
        description,
        price,
        owner_name,
        phone,
        email,
        location,
        area,
        status,
        floor,
        bedrooms,
        bathrooms):

    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": f"""
Generate a short professional title for a real estate listing.

Location: {location}
Bedrooms: {bedrooms}
Bathrooms: {bathrooms}

Return only one title.
"""
            }
        ]
    )

    title = response["message"]["content"].strip()

    # Fonts
    title_font = ImageFont.truetype("arialbd.ttf", 42)
    section_font = ImageFont.truetype("arialbd.ttf", 30)
    normal_font = ImageFont.truetype("arial.ttf", 24)

    # Poster canvas
    poster = Image.new("RGB", (1200, 1500), "white")
    draw = ImageDraw.Draw(poster)

    # Property image
    img = Image.open(image_path)
    img = img.resize((1100, 550))
    poster.paste(img, (50, 30))

    # Title
    draw.text(
        (60, 620),
        title,
        fill="navy",
        font=title_font
    )

    # Price
    draw.text(
        (60, 690),
        f"₹ {price:,.0f}",
        fill="green",
        font=title_font
    )

    # Property Details
    draw.text((60, 790), "Property Details", fill="darkblue", font=section_font)

    draw.text((60, 850), f"Location : {location}", fill="black", font=normal_font)
    draw.text((60, 900), f"Area : {area} sq.ft", fill="black", font=normal_font)
    draw.text((60, 950), f"Floor : {floor}", fill="black", font=normal_font)

    draw.text((550, 850), f"Bedrooms : {bedrooms}", fill="black", font=normal_font)
    draw.text((550, 900), f"Bathrooms : {bathrooms}", fill="black", font=normal_font)
    draw.text((550, 950), f"Status : {status}", fill="red", font=normal_font)

    # Owner Details
    draw.text((60, 1060), "Owner Details", fill="darkblue", font=section_font)

    draw.text((60, 1120), f"Owner : {owner_name}", fill="black", font=normal_font)
    draw.text((60, 1170), f"Phone : {phone}", fill="black", font=normal_font)
    draw.text((60, 1220), f"Email : {email}", fill="black", font=normal_font)

    # Description
    draw.text((60, 1310), "Description", fill="darkblue", font=section_font)

    wrapped_text = textwrap.fill(description[:250], width=70)

    draw.text(
        (60, 1360),
        wrapped_text,
        fill="black",
        font=normal_font
    )

    os.makedirs("posters", exist_ok=True)

    output = f"posters/poster_{owner_name}.png"

    poster.save(output)

    return output