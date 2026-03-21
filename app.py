from flask import Flask, render_template, request, redirect
import sqlite3
clientes =[]
app = Flask(__name__)

import sqlite3

conexion = sqlite3.connect("clientes.db", check_same_thread=False)
cursor = conexion.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT,
    proyecto TEXT,
    presupuesto TEXT,
    zona TEXT,
    telefono TEXT
)
""")

conexion.commit()
@app.route('/')
@app.route('/clientes')
def ver_clientes():
    zona_filtro = request.args.get('zona')

    conn = sqlite3.connect("clientes.db")
    cursor = conn.cursor()

    if zona_filtro:
        cursor.execute("SELECT * FROM clientes WHERE zona = ?", (zona_filtro,))
    else:
        cursor.execute("SELECT * FROM clientes")

    clientes = cursor.fetchall()

    total_clientes = len(clientes)
    total_presupuesto = sum(c[3] for c in clientes) if clientes else 0

    conn.close()

    return render_template(
        'clientes.html',
        clientes=clientes,
        total_clientes=total_clientes,
        total_presupuesto=total_presupuesto
    )

@app.route('/guardar', methods=['POST'])
def guardar():
    nombre = request.form['nombre']
    proyecto = request.form['proyecto']
    presupuesto = request.form['presupuesto'].replace(",", "")
    zona = request.form['zona']
    telefono = request.form['telefono']

    presupuesto_num = int(presupuesto)

    if presupuesto_num >= 200000:
        nivel = "🔥"
    elif presupuesto_num >= 100000:
        nivel = "⚡"
    else:
        nivel = "❄️"

    clientes.append([nombre, proyecto, presupuesto, zona, telefono, nivel])

    return redirect('/clientes')

@app.route('/editar/<int:indice>', methods=['GET', 'POST'])
def editar(indice):
    if request.method == 'POST':
        clientes[indice][0] = request.form['nombre']
        clientes[indice][1] = request.form['proyecto']
        clientes[indice][2] = request.form['presupuesto'].replace(",", "")
        clientes[indice][3] = request.form['zona']
        clientes[indice][4] = request.form['telefono']
        return redirect('/clientes')

    cliente = clientes[indice]
    return render_template('editar.html', cliente=cliente, indice=indice)

@app.route('/eliminar/<int:indice>')
def eliminar(indice):
    clientes.pop(indice)
    return redirect('/clientes')

@app.route('/whatsapp/<int:indice>')
def whatsapp(indice):
    cliente = clientes[indice]

    nombre = cliente[0]
    presupuesto = cliente[2]
    zona = cliente[3]
    telefono = cliente[4]

    mensaje = f"Hola {nombre}, tengo opciones en {zona} dentro de tu presupuesto de ${presupuesto}. ¿Te gustaría verlas?"

    import urllib.parse
    mensaje_codificado = urllib.parse.quote(mensaje)

    url = f"https://wa.me/{telefono}?text={mensaje_codificado}"

    return redirect(url)

if __name__ == '__main__':
    app.run(debug=True)
    
    