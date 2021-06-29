from flask import Flask,request,redirect,jsonify,session,g
from flask.templating import render_template
from sqlalchemy import create_engine
from flask_cors import CORS, cross_origin
from flask_socketio import SocketIO
import requests
import json

app = Flask(__name__,
            static_folder = "C:\\users\\mauricio\\desktop\\front_meseros\\static",
            template_folder = "C:\\users\\mauricio\\desktop\\front_meseros\\templates",
            static_url_path='/')

app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
socketio.init_app(app, cors_allowed_origins="*")
app.secret_key = 'super secret key'


pedido_json={"topico":"Mesa1","mensaje":{
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
}}


cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
@app.route("/api/home/",methods=['GET','POST'])
def home():
    pedido=json.dumps(pedido_json)
    return render_template('index.html')

@socketio.on('onmessage')
def handle_message(data):
    print('received message: ' + data)

@app.route("/api/menu/recibe_pedido/",methods=['GET','POST'])
def get_pedido():
    pedido=request.get_json()
    # print(pedido+'recibido')
    # res=requests.post('http://localhost:7000/api/menu/envia_pedido/',json=pedido)
    return 'Pedido enviado'

@app.route("/api/menu/envia_pedido/",methods=['GET','POST'])
def send_pedido():
    pedido=request.get_json()
    # print(pedido+'enviado')
    return pedido




if __name__ == "__main__":
    socketio.run(app,port=7000)
    # app.run(host="0.0.0.0", port=7000,debug=True)