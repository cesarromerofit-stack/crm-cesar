from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# 🔹 MOSTRAR CLIENTES
@app.route('/clientes')
def ver_clientes():
    zona_filtro = request.args.get('zona', '')

    conn = sqlite3.connect("clientes.db", timeout=10)
    cursor = conn.cursor()

    # Crear tabla si no existe
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


    # Filtrar o traer todos
    if zona_filtro:
        cursor.execute("SELECT * FROM clientes WHERE zona LIKE ?", ('%' + zona_filtro + '%',))
    else:
        cursor.execute("SELECT * FROM clientes")

    clientes = cursor.fetchall()

    conn.close()

    return render_template('clientes.html', clientes=clientes, zona_filtro=zona_filtro)


# 🔹 GUARDAR CLIENTE
@app.route('/guardar', methods=['POST'])
def guardar():
    try:
        nombre = request.form.get('nombre', '')
        proyecto = request.form.get('proyecto', '')
        presupuesto = request.form.get('presupuesto', '0')
        zona = request.form.get('zona', '')
        telefono = request.form.get('telefono', '')

        conn = sqlite3.connect("clientes.db", timeout=10)
        cursor = conn.cursor()

        # Crear tabla si no existe
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

        # Insertar cliente
        cursor.execute("""
        INSERT INTO clientes (nombre, proyecto, presupuesto, zona, telefono)
        VALUES (?, ?, ?, ?, ?)
        """, (nombre, proyecto, presupuesto, zona, telefono))

        conn.commit()
        conn.close()

        return redirect('/clientes')

    except Exception as e:
        return f"ERROR: {e}"


# 🔹 INICIO
@app.route('/')
def inicio():
    return render_template('index.html')

# 🔹 NUEVA VISTA
@app.route('/propiedad/<int:id>')
def propiedad(id):
    conn = sqlite3.connect("clientes.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM clientes WHERE id = ?", (id,))
    cliente = cursor.fetchone()

    conn.close()

    return render_template("propiedad.html", cliente=cliente)

# 🔹 RUN
if __name__ == '__main__':
    app.run(debug=True)