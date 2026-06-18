import ollama

def generate_description(features, price):

    prompt = f"""
    Write an attractive real estate description.

    Features:
    {features}

    Price: ₹{price}
    """

    response = ollama.chat(
        model='llama3.2',
        messages=[
            {'role': 'user', 'content': prompt}
        ]
    )

    return response['message']['content']