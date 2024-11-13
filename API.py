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
                "content": "أنت مساعد ذكي مختص بتشخيص مشكلات المنازل وتحليل الأضرار مثل أعطال الكهرباء وتسريبات المياه. يمكنك تقديم تشخيص دقيق وتوصيات للإصلاح بناءً على المعلومات المتاحة.",
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


def generate_prompt(issue_type, location=None, leak_type=None, description=None):
    # Base prompt with optional description details
    base_prompt = "يرجى تحليل الأضرار التالية في المنزل بناءً على المعلومات المقدمة من العميل:"

    # Detailed prompt for electricity issues
    if issue_type == "electric":
        prompt = (
            f"{base_prompt} يبدو أن هناك مشكلة في الكهرباء."
            f" {description or 'يرجى تقديم مزيد من التفاصيل حول المشكلة.'}"
            " هل يمكنك تقديم تحليل للمشكلة وأسبابها المحتملة وتحديد الإجراءات اللازمة لإصلاح الأعطال الكهربائية المحتملة؟"
        )
    
    # Detailed prompt for leak issues with location and leak type
    elif issue_type == "leak":
        prompt = f"{base_prompt} "
        if location and leak_type:
            prompt += (
                f"تم الإبلاغ عن تسريب {leak_type} في موقع {location}. "
                f"{description or 'يرجى تقديم تحليل لنوع التسريب وأسبابه المحتملة.'} "
                "يرجى أيضاً تقديم الخطوات المناسبة لمعالجة هذا النوع من التسريب."
            )
        elif location:
            prompt += (
                f"تم الإبلاغ عن تسريب في موقع {location}. "
                f"{description or 'يرجى تقديم تحليل للأضرار المحتملة.'} "
                "يرجى توضيح ما إذا كان التسريب داخليًا أو خارجيًا، وتقديم تحليل وأفضل طرق المعالجة."
            )
        else:
            prompt += (
                f"تم الإبلاغ عن تسريب ولكن لم يتم تحديد الموقع بدقة. "
                f"{description or 'يرجى تقديم مزيد من التفاصيل.'} "
                "يرجى تقديم تحليل للتسريب المحتمل وأسبابه، وتحديد الإجراءات المطلوبة للتعامل معه."
            )
    
    # Generic prompt if issue type is unknown
    else:
        prompt = (
            f"{base_prompt} لم يتم تحديد نوع المشكلة بدقة. "
            f"{description or 'يرجى تقديم معلومات إضافية لتحديد المشكلة.'} "
            "يرجى تقديم إرشادات عامة للتحقق من أعطال كهربائية أو تسريبات داخل المنزل."
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
