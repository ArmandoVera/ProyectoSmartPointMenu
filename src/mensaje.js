var mqtt = require('mqtt')
var client = mqtt.connect('127.0.0.1:1883')

client.on('connect', function() {
    client.subscribe('presence', function(err) {
        if (!err) {
            client.publish('presence', 'Hello mqtt')
        }
    })
})

client.on('message', function(topic, message) {
    const mensaje = document.getElementById("mensaje");
    mensaje.innerHTML = `<div>${message.toString()}</div>`;
    // message is Buffer
    console.log(message.toString())
    client.end()
})