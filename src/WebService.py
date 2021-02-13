

from flask import Flask, request

app =  Flask(__name__)

@app.route('/')
def helloworld():
    return '!!Hola, Clase de CDK'

@app.route('/saludo/<persona>')
def saludoDinamico(persona):
    return 'Hola %s, bienvenido!!!' % persona

@app.route('/cuadrado/<num>')
def calculaCuadrado(num):
    resp = float(num) * float(num)
    return 'Respuesta %f' %resp

@app.route('/test', methods=['POST', 'GET'])
def recibeParams():

    textReturn = "Metodo no aceptado"
    if request.method == "POST":
        data = request.get_json()
        try:
            mascota = data['mascota']
            textReturn ='Se recivio %s'% mascota
        except:
            textReturn ="Ocurrio un error"
    return textReturn;

@app.route('/cubo/', methods=['POST'])
def calculaCubo():
    data = request.get_json()
    num = data['num']
    resp = num * num * num
    return 'Respuesta %f' %resp


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3001, debug=False)
