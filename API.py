import base64
import logging
import os

from dotenv import load_dotenv
from flask import Flask, jsonify, request
from openai import OpenAI


# Initialize Flask app
app = Flask(__name__)

# Setup logging
logging.basicConfig(
    filename="logfile.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# Load environment variables for OpenAI API key
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    logging.error("API key is not set.")
    raise ValueError("API key is not set.")

# Initialize OpenAI
client = OpenAI(api_key=api_key)

@app.route("/analyze", methods=["POST"])
def analyze_home_issue():
    # Extract data from the JSON payload
    data = request.get_json()
    
    # Ensure necessary fields are present
    issue_type = data.get("issue_type")
    location = data.get("location")
    leak_type = data.get("leak_type")
    description = data.get("description")

    if not issue_type:
        return jsonify({"error": "No issue type found"}), 400

    # Generate the prompt based on provided parameters
    prompt = generate_prompt(issue_type=issue_type, location=location, leak_type=leak_type, description=description)

    # Get GPT-4 response (example using OpenAI's client)
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": "You are an intelligent assistant specializing in diagnosing home issues and analyzing damage, such as electrical faults and water leaks. Based on the available information, you can provide accurate diagnoses and recommendations for repairs.",
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
        temperature=0.0,
    )

    diagnosis_response = response.choices[0].message.content

    # Return the GPT-4 diagnosis and suggestions
    return jsonify({"diagnosis": diagnosis_response})


# English version of the generate_prompt function

def generate_prompt(issue_type, location=None, leak_type=None, description=None):
    # Base prompt with optional description details
    base_prompt = "Please analyze the following home issue based on the information provided by the client:"

    # Detailed prompt for electricity issues
    if issue_type == "electric":
        prompt = (
            f"{base_prompt} It appears there is an electrical problem."
            f" {description or 'Please provide additional details about the issue.'}"
            " Can you provide an analysis of the problem, potential causes, and recommended actions to fix this electrical issue?"
        )
    
    # Detailed prompt for leak issues with location and leak type
    elif issue_type == "leak":
        prompt = f"{base_prompt} "
        if location and leak_type:
            prompt += (
                f"A {leak_type} leak has been reported at the {location}. "
                f"{description or 'Please provide an analysis of the leak type and potential causes.'} "
                "Additionally, suggest appropriate steps to address this type of leak."
            )
        elif location:
            prompt += (
                f"A leak has been reported at the {location}. "
                f"{description or 'Please provide an analysis of the potential damage.'} "
                "Please clarify whether the leak is internal or external and provide an analysis and the best methods for repair."
            )
        else:
            prompt += (
                f"A leak has been reported, but the location is unspecified. "
                f"{description or 'Please provide further details.'} "
                "Please analyze the possible source and cause of the leak and recommend actions to address it."
            )
    
    # Generic prompt if issue type is unknown
    else:
        prompt = (
            f"{base_prompt} The issue type has not been specified. "
            f"{description or 'Please provide additional information to identify the problem.'} "
            "Please provide general guidelines for checking potential electrical issues or leaks in the home."
        )

    return prompt








# Run the Flask app
if __name__ == "__main__":
    if not os.path.exists("uploads"):
        os.makedirs("uploads")
    app.run(host="0.0.0.0", port=5000)


"""
API Explanation:
Endpoint: /analyze (POST)
Users can send an image file via a POST request.
The API analyzes the image using the model and returns the diagnosis and suggested treatments from GPT-4.
Image Handling: The uploaded image is saved in the uploads directory.
Response: A JSON object with the detected disease and GPT-4 diagnosis in Arabic is returned.

Run the API using:
python api.py

The API will be available at http://localhost:5000/analyze.

"""
