# 🤖 OpenAI Image Generator Assistant

A command-line Python script that leverages the OpenAI API and DALL-E 3 to generate high-quality, detailed images from structured text descriptions. Ideal for creating visual assets for videos, blog posts, and other creative projects.

## 🚀 Overview

This tool provides a simple yet powerful way to translate rich, descriptive text into stunning visual images. By providing a JSON object with a title, summary, and a detailed description, you can direct DALL-E 3 to generate an image that precisely matches your creative vision.

## 🌟 Features

* **🎨 High-Quality Image Generation:** Utilizes OpenAI's DALL-E 3 model to create detailed and contextually accurate images.
* **📝 Structured Input:** Takes a JSON file as input, allowing for detailed and organized image prompts.
* **🔐 Secure API Key Handling:** Uses a `.env` file to securely manage your OpenAI API key.
* **⚙️ Simple CLI Operation:** Easy to run from the command line with a single command.
* **📁 Flexible Input:** While designed for JSON files, the script can be easily adapted to take simple string inputs for quick tests.

## 🛠️ Tech Stack

* **Backend:** Python
* **AI Model:** OpenAI DALL-E 3
* **Dependencies:** `openai`, `python-dotenv`

## ✅ Prerequisites

Before you begin, ensure you have the following:

* [Python 3.9+](https://www.python.org/downloads/)
* `pip` (Python package installer)
* An **OpenAI API Key**. You can obtain one from the [OpenAI Platform](https://platform.openai.com/api-keys).

## ⚙️ Installation & Setup

Follow these steps to get the application running on your local machine.

1.  **Clone the Repository**
    ```
    git clone [https://github.com/blankv15/openai-image-generator](https://github.com/blankv15/openai-image-generator)
    cd openai-image-generator
    ```

2.  **Create and Activate a Virtual Environment**
    It's best practice to use a virtual environment to keep project dependencies isolated.
    ```
    # Create the virtual environment
    python3 -m venv .venv
    
    # Activate it (on macOS/Linux)
    source .venv/bin/activate
    
    # Or activate it (on Windows)
    .\.venv\Scripts\activate
    ```

3.  **Install Dependencies**
    Install the required Python packages using the `requirements.txt` file.
    ```
    pip install -r requirements.txt
    ```

4.  **Create and Configure Environment File**
    Create a file named `.env` in the root directory of the project. This file will store your secret API key.
    ```
    touch .env
    ```
    Open the `.env` file and add your OpenAI API key as follows:
    ```
    OPENAI_API_KEY="sk-YourSecretApiKey"
    ```

## 📖 How to Use

The script is executed via the command line and accepts a path to a JSON file containing the image description.

1.  **Prepare your Image JSON**
    Create a `.json` file with your image details. You can use the example below as a template.

2.  **Run the Script**
    Execute the `run.py` script from your terminal.
    ```
    python run.py --file path/to/your/image_info.json
    ```
    For testing purposes, the script might also be configured to accept a simple string.

### Example JSON Input

Here is an example of the detailed JSON structure the script uses to generate an image.

```json
{
  "image_title": "Wanderlust Companion: The Travel Backpack",
  "image_summary": "An image capturing the essence of a travel backpack ready for a new adventure, meticulously packed and placed at the beginning of a well-trodden dirt path in a dense, green forest. The backpack stands upright, implying the eager anticipation of the journey ahead, surrounded by nature's serenity and the promise of discovery.",
  "detailed_description": "The image showcases a robust and ergonomically designed travel backpack, standing upright on a slightly dusty, sun-speckled dirt path that slices through a verdant forest. The backpack..."
}