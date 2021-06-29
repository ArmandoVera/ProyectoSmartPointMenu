from flask import Flask, render_template
from flask_sock import Sock
import json

app=Flask(__name__,static_folder = "C:\\users\\mauricio\\desktop\\front_meseros\\static",
            template_folder = "C:\\users\\mauricio\\desktop\\front_meseros\\templates",
            static_url_path='/')
sock=Sock(app)

@app.route('/home')
def home():
    return render_template('index.html')

@sock.route('/ws')
def reverse(ws):
    while True:
        mensaje=ws.receive()
        print(mensaje)
        mensaje_json=json.loads(mensaje)
        ws.send(mensaje_json['mensaje']['cart'][0])

@sock.route('/message')
def message(ws):
    while True:
        text=ws.receive()
        print(text)
        ws.send(text[::-1])



# if __name__ == "__main__":
#     app.run(host="127.0.0.1",port=7000)