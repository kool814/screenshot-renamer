# Screenshot Renamer

This Python script captures a screenshot, sends it to OpenAI to get a text description, and renames the screenshot file based on the description.

## Prerequisites

- Python 3.x
- An OpenAI API key

## Installation

1. Clone the repository:
   git clone https://github.com/your-username/screenshot-renamer.git
   cd screenshot-renamer

2. Create a virtual environment and install dependencies:
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt

3. Set your OpenAI API key in a .env file:
   echo "OPENAI_API_KEY=your-openai-api-key" > .env

4. Run the script:
   python screenshot_renamer.py
