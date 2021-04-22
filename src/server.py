from flask import Flask
server = Flask(__name__)

@server.route("/")
def hello():
    return "Hola planificación y gestión de infraestructuras TIC \n\n Por Sergio Cámara"

if __name__ == "__main__":
   server.run(host='0.0.0.0')
