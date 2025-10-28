from flask import Flask, render_template,request,jsonify
import math

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/index')
def index():
    titulo="IEVN1001"
    listado=["Python","Flask","HTML","CSS","JavaScript"]
    return render_template('index.html', titulo = titulo, listado = listado)


@app.route("/aporb")
def apor():
    return render_template('aporb.html')

@app.route("/resultado", methods=['POST'])
def resultado():
    n1=request.form.get("a")
    n2=request.form.get("b")
    return " LA MULTIPLICACION DE {} Y {} ES {}".format(n1,n2,int(n1)*int(n2))


""" @app.route("/distancia")
def distancia():
    return render_template('distancia.html')


@app.route("/dist", methods=['POST'])
def dist():
    X2 = float(request.form.get("X2"))
    X1 = float(request.form.get("X1"))
    Y2 = float(request.form.get("Y2"))
    Y1 = float(request.form.get("Y1"))

    distancia = math.sqrt((X2 - X1) ** 2 + (Y2 - Y1) ** 2)

    return "LA DISTANCIA ES sqrt(({} - {}) ** 2 + ({} - {}) ** 2) = {}".format(
        X2, X1, Y2, Y1, distancia) """

@app.route('/distancia', methods=['GET'])
def distancia():
   
    if not request.args:
        return render_template('distancia.html')

    X2 = float(request.args.get("X2"))
    X1 = float(request.args.get("X1"))
    Y2 = float(request.args.get("Y2"))
    Y1 = float(request.args.get("Y1"))

   
    distancia = math.sqrt((X2 - X1)**2 + (Y2 - Y1)**2)
    resultado = round(distancia, 2)

   
    return render_template('distancia.html', resultado=resultado)



@app.route("/figuras", methods=["GET", "POST"])
def figuras():
    AREA = request.form.get("AREA")
    RESULTADO = ""

    if request.method == "POST":
        if AREA == "CUADRADO":
            LADO = float(request.form.get("LADO", 0))
            RESULTADO = LADO * LADO

        elif AREA == "TRIANGULO":
            BASE = float(request.form.get("BASE", 0))
            ALTURA = float(request.form.get("ALTURA", 0))
            RESULTADO = (BASE * ALTURA) / 2

        elif AREA == "CIRCULO":
            RADIO = float(request.form.get("RADIO", 0))
            RESULTADO = math.pi * (RADIO ** 2)

        elif AREA == "RECTANGULO":
            BASE = float(request.form.get("BASE", 0))
            ALTURA = float(request.form.get("ALTURA", 0))
            RESULTADO = BASE * ALTURA

        elif AREA == "PENTAGONO":
            PERIMETRO = float(request.form.get("PERIMETRO", 0))
            APOTEMA = float(request.form.get("APOTEMA", 0))
            RESULTADO = (PERIMETRO * APOTEMA) / 2

    return render_template("figuras.html", AREA=AREA, RESULTADO=RESULTADO)



    

@app.route('/hola')
def func():
    return "<h1>!HOLA!</h1>"


@app.route("/user/<string:user>")
def user(user):
    return "<h1>HELLO, {}!</h1>".format(user)


@app.route("/square/<int:num>")
def square(num):
    return "<h1>The square of {} is!{}.</h1>".format(num, num**2)

@app.route("/repeat/<string:text>/<int:times>")
def repeat(text, times):
    return "<h1>" + "".join([text] * times) + "</h1>"


@app.route('/suma/<float:a>/<float:b>')
def suma(a, b):
    return "<h1>THE SUM OF {} AND {} IS {}.</h1>".format(a, b, a + b)





if __name__ == '__main__':
    app.run(debug=True)