from flask import Flask
server = Flask(__name__)

@server.route("/")
def hello():
    return "<h1>Hola Planificación y Gestión de infraestructuras TIC</h1> </br></br> <h2>Por <strong>Sergio Cámara</strong></h2>"

if __name__ == "__main__":
   server.run(host='0.0.0.0')
