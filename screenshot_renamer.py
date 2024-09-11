import os
from dotenv import load_dotenv
from openai import OpenAI
import time
from PIL import ImageGrab  # For capturing screenshots

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment variables
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OpenAI API key not found. Please set it in the .env file.")

client = OpenAI(api_key=api_key)

def take_screenshot():
    # Capture the screenshot and save it as temp.png
    screenshot = ImageGrab.grab()
    screenshot.save("temp_screenshot.png")
    return "temp_screenshot.png"

def image_to_text(image_path):
    with open(image_path, 'rb') as image_file:
        # Use OpenAI's API to get a text description from the image
        response = client.images.generate(image=image_file,
        prompt="Describe the image in detail.",
        n=1,
        size="1024x1024")
    # Return the description (assuming the API returns it in 'data' -> 'text')
    return response.data[0].text

def rename_file(image_path, description):
    # Create a valid filename based on the description (limit to 50 characters, replace spaces)
    valid_name = "_".join(description.split())[:50]
    new_file_path = f"{valid_name}.png"

    os.rename(image_path, new_file_path)
    return new_file_path

if __name__ == "__main__":
    print("Taking screenshot...")
    screenshot_path = take_screenshot()

    print("Getting image description from OpenAI...")
    description = image_to_text(screenshot_path)

    print(f"Renaming file based on description: {description}")
    new_file_path = rename_file(screenshot_path, description)

    print(f"Screenshot saved as: {new_file_path}")