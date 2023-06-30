from flask import Flask, render_template, request
app = Flask(__name__)

if __name__ =="__main__": #Responsable de levantar el servidor local que pone en funcionamiento la aplicación
    app.run(debug=True)

@app.route("/")
def index():
    return render_template("form.html")


@app.route("/saludo", methods=["POST"])                         
def saludar():
    nombre = request.form["nombre"]#request es un objeto y el form es un diccionario
    return render_template("saludo.html", nombre=nombre)
