from flask import Flask, render_template, request, jsonify
from openai import OpenAI

app = Flask(__name__)

# 🔥 CONFIG BOT (puedes comentar esto si no lo usas)
client = OpenAI(api_key="TU_API_KEY_AQUI")

# =========================
# 🌐 RUTAS WEB (CRM)
# =========================

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/clientes")
def clientes():
    return render_template("clientes.html")


@app.route("/pipeline")
def pipeline():
    return render_template("pipeline.html")


@app.route("/propiedad/<int:id>")
def propiedad(id):
    return render_template("propiedad.html", id=id)


# =========================
# 🤖 RUTA DEL BOT (OPCIONAL)
# =========================

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    mensaje = data.get("mensaje")

    respuesta = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "Eres un asesor inmobiliario experto en Punta Cana."
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


# =========================
# 🚀 RUN APP
# =========================

if __name__ == "__main__":
    app.run(debug=True)