from flask import Flask, render_template, request, jsonify
from openai import OpenAI
import os

GEMINI_API_KEY = "your_actual_api_key"

client = OpenAI(
    api_key=GEMINI_API_KEY,
    base_url="your base_url"
)

app = Flask(__name__)

def build_prompt(user_question):
    base_prompt = """
You are NutriGuide, a helpful, friendly AI Nutrition Chatbot. Your core features are:
1. Conversationally answering any nutrition or healthy eating question.
2. Giving meal suggestions personalized to user needs.
3. Providing basic nutrition screening (malnutrition risk—ask simple friendly questions).

Be clear, concise, and practical. If user mentions allergies, health condition, or dietary preference, tailor advice.

User: {}
NutriGuide:"""
    return base_prompt.format(user_question)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data["message"]

    prompt = build_prompt(user_message)

    try:
        completion = client.chat.completions.create(
            model="gemini-2.5-flash",
            messages=[
                {"role": "system", "content": "You are NutriGuide, an expert AI nutritionist chat assistant."},
                {"role": "user", "content": user_message}
            ]
        )
        answer = completion.choices[0].message.content
    except Exception as e:
        answer = "Sorry, I'm having trouble answering right now."

    return jsonify({"reply": answer})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))

    app.run(host="0.0.0.0", port=port)
