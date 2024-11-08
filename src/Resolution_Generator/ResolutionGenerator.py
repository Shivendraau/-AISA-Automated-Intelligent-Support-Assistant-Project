# Automatically generate resolutions for common technical issues using Generative AI models based on 
# historical data and documentation.

import openai
import os

# Set up OpenAI API key from environment variable
openai.api_key = os.getenv('OPENAI_API_KEY')

def generate_resolution(description, max_tokens=150):
    prompt = f"Given the following incident description, provide a detailed resolution:\n\n{description}\n\nResolution:"
    
    response = openai.Completion.create(
        engine="text-davinci-003",  # Use appropriate model
        prompt=prompt,
        max_tokens=max_tokens,
        n=1,
        stop=None,
        temperature=0.7,
    )
    
    resolution = response.choices[0].text.strip()
    return resolution

# Example usage
# description = "User unable to connect to VPN after recent update."
# resolution = generate_resolution(description)
# print(resolution)