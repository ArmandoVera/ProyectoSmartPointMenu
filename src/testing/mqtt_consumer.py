from paho.mqtt import client 

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-ip", "--host", help="IP address")
parser.add_argument("-rp", "--rabbitport", help="RabbitMQ port")
args = parser.parse_args()

host_ip = args.host if args.host else "127.0.0.1"
rabbit_port = int(args.rabbitport) if args.rabbitport else 1883


def ante_conexion_exitosa(client, userdata, flags, rc):
    print("Connection to the broker successfull")
    print("[X] Waiting for logs. Press CTRL+C to exit.")
    client.subscribe("e94b4260-4b3e-40ed-b09e-29ef740ff158/#")
    #client.publish("e94b4260-4b3e-40ed-b09e-29ef740ff158", "consumer has joined to the chat")

def on_message(mosq, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))

def on_publish(mosq, obj, mid):
    print("mid: " + str(mid))

cliente = client.Client()
cliente.on_connect = ante_conexion_exitosa
cliente.on_message = on_message
cliente.on_publish = on_publish

cliente.username_pw_set("guest","guest")
cliente.connect(host_ip, rabbit_port, 60)
cliente.loop_forever()