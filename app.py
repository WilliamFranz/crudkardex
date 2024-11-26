from flask import Flask,render_template,request,redirect,url_for
import sqlite3

app = Flask(__name__)

def init_database():
    conn = sqlite3.connect("willi.db")
    
    cursor = conn.cursor()
    cursor.execute(
        
    """
    CREATE TABLE IF NOT EXISTS personas
(
    id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    telefono TEXT NOT NULL,
    fecha_nac TEXT NOT NULL
    )   
    """
    )
    conn.commit()
    conn.close()

init_database()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/personas")
def personas():
    conn=sqlite3.connect("willi.db")
    # permite manejar los registros como diccionario
    conn.row_factory = sqlite3.Row
    
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM personas")
    personas = cursor.fetchall()
    return render_template("personas/index.html",personas = personas)

@app.route("/personas/create")
def create():
    return render_template('personas/create.html')
    
@app.route("/personas/create/save",methods=['POST'])
def personas_save():
    nombre = request.form['nombre']
    telefono = request.form['telefono']
    fecha_nac = request.form['fecha_nac']
    
    conn = sqlite3.connect('willi.db')
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO personas(nombre,telefono,fecha_nac) VALUES(?,?,?)",
                   (nombre, telefono, fecha_nac))
    
    conn.commit()
    conn.close()
    return redirect('/personas')
    
if __name__ == "__main__":
    app.run(debug=True)