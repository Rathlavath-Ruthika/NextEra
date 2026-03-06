from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import requests
import re
app = Flask(__name__)
CORS(app)

GROQ_API_KEY = "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"
GROQ_MODEL = "llama-3-70b-versatile"
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"

def call_groq(prompt):
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {GROQ_API_KEY}"}
    body = {"model": GROQ_MODEL, "messages": [{"role": "user", "content": prompt}], "temperature": 0.7}
    
    try:
        response = requests.post(GROQ_URL, json=body, headers=headers)
        data = response.json()
        result = data["choices"][0]["message"]["content"]

        # Clean asterisks and extra markdown
        result = re.sub(r"\*{1,3}", "", result)
        return result
    except:
        return "API error. Please try again."

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/generate_campaign", methods=["POST"])
def generate_campaign():
    product = request.form.get("product")
    audience = request.form.get("audience")
    platform = request.form.get("platform")

    prompt = f"Generate a detailed marketing campaign. Product: {product}. Target Audience: {audience}. Platform: {platform}. Include: Campaign Idea, Ad Copy, Hashtags."

    output = call_groq(prompt)
    return jsonify({"result": output})


@app.route("/generate_pitch", methods=["POST"])
def generate_pitch():
    product = request.form.get("product")
    customer = request.form.get("customer")

    prompt = f"Create a compelling AI sales pitch. Product: {product}. Customer Persona: {customer}. Include: 30-second pitch, Value proposition."

    output = call_groq(prompt)
    return jsonify({"result": output})


@app.route("/lead_score", methods=["POST"])
def lead_score():
    name = request.form.get("name")
    budget = request.form.get("budget")
    need = request.form.get("need")
    urgency = request.form.get("urgency")

    prompt = f"Score this lead (0-100) based on Budget, Need, and Urgency. Lead Name: {name}. Budget: {budget}. Need: {need}. Urgency: {urgency}."

    output = call_groq(prompt)
    return jsonify({"result": output})
if __name__ == "__main__":
    app.run(debug=True,host="127.0.0.1",port=5000)