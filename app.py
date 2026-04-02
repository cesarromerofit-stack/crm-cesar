from flask import Flask, render_template, request, jsonify
from openai import OpenAI
import os

app = Flask(__name__)

# 🔐 API KEY (usa variable de entorno)
client = OpenAI(api_key="AC0RwLBSiTXXnsitySq7RQnI2BIios_G5PWdJLEmDStZfrZ5beBnIJzkfJ06w3oJV6ZBA83X6dT3BlbkFJXEnTihRwWnjuRa2AozbUP_mVuDP6k7FkeNlDGCnF0BPMjTGskQSD4QkBHDFcyKUR7ml2onHxMA")

# HOME
@app.route("/")
def home():
    return render_template("index.html")

# CHAT IA
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    mensaje = data.get("mensaje")

    respuesta = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "Eres una asesora experta en diseño de interiores elegante. Responde profesional, breve y atractiva. Invita al cliente a contactar por WhatsApp."
            },
            {
                "role": "user",
                "content": mensaje
            }
        ]
    )

    return jsonify({
        "respuesta": respuesta.choices[0].message.content
    })

if __name__ == "__main__":
    app.run(debug=True)