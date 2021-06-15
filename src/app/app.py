from flask import Flask, redirect, url_for, render_template ,make_response,jsonify,request
from time import sleep
from paho.mqtt import client as mqtt

app = Flask(__name__)

def mqqtcon():
    cliente=mqtt.Client()
    cliente.username_pw_set("guest","guest")
    cliente.connect("127.0.0.1",1883)
    sleep(1)
    return cliente

ordenar={
    "acceptedRecommendations": [
        { "name": "MARGARITA TAMARINDO", "category": "coctel", "type": "COPA" },
        { "name": "CERVEZA NACIONAL", "category": "alcohol", "type": "BOTELLA" }
    ],

    "cart": [
        { "name": "Tartare di Tonno alla Mediterránea", "id:": 1, "price": 259, "costo": 0, "comment": "un comentario" },
        { "name": "Margarita tamarindo", "price": 63, "costo": 0, "selectedType": "COPA" },
        { "name": "Cerveza nacional", "price": 36.96, "costo": 0, "selectedType": "BOTELLA" },
        { "name": "Carpaccio di Manzo all´Olio Tartufato", "id": 3, "price": 225, "costo": 0 },
        { "id": 1,"name": "Romana","price": 241, "costo": 0, "selectedOption": "40 cm", "comment": "comentario pizza" }
    ],
    
    "mealType": "cena",
    
    "time": "2021-06-05T23:30:39.458Z",
    "weekday": "Saturday",
    "user": { "username": "armando@libela.mx", "commensals": 4, "session": 1622935190202, "table": 4 }
}

def publish(topico,mensaje):
    cliente=mqqtcon()
    sleep(1)
    cliente.publish(topico,mensaje,2)
    sleep(1)
    

@app.route('/', methods=['POST'])
def funcion():
    diccionario=request.get_json(force=True)
    topico=diccionario['topico']
    mensaje=str(diccionario['mensaje'])
    publish(topico,mensaje)
    return make_response (jsonify(
                    {"message": "Tu orden fue enviada exitosamente"}
                ),
                200,
            )
    

                    

if __name__ == '__main__':
    app.run( debug=True)