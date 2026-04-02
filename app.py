from flask import Flask, render_template

app = Flask(__name__)

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

if __name__ == "__main__":
    app.run(debug=True)