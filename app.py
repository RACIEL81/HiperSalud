##edwin meneses y paula rincon
from flask import Flask, render_template
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/servicios')
def servicios():
    return render_template('servicios.html')

@app.route('/nosotros')
def nosotros():
    return render_template('nosotros.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

# 🔧 NUEVA RUTA PARA EL FORMULARIO DE SOLICITAR CITA
@app.route('/solicitar-cita')
def solicitar_cita():
    return render_template('solicitar_cita.html')

if __name__ == '__main__':
    # Ejecutar en 0.0.0.0 y puerto 8000 para que se exponga correctamente en GitHub Codespaces
    app.run(host='0.0.0.0', port=8000, debug=True)
