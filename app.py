from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Crear base de datos si no existe
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


# VER CLIENTES
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
    total_presupuesto = sum(int(c[3]) for c in clientes) if clientes else 0

    conn.close()

    return render_template(
        'clientes.html',
        clientes=clientes,
        total_clientes=total_clientes,
        total_presupuesto=total_presupuesto,
        zona_filtro=zona_filtro
    )


# GUARDAR CLIENTE
@app.route('/guardar', methods=['POST'])
def guardar():
    nombre = request.form['nombre']
    proyecto = request.form['proyecto']
    presupuesto = request.form['presupuesto']
    zona = request.form['zona']
    telefono = request.form['telefono']

    conn = sqlite3.connect("clientes.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO clientes (nombre, proyecto, presupuesto, zona, telefono)
    VALUES (?, ?, ?, ?, ?)
    """, (nombre, proyecto, presupuesto, zona, telefono))

    conn.commit()
    conn.close()

    return redirect('/clientes')


if __name__ == '__main__':
    app.run(debug=True)
    # cambio
    
    