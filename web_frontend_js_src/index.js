var server_port = 65432;
var server_addr = "192.168.0.180";   // the IP address of your Raspberry PI

function send_data(input){
    const net = require('net');
    const client = net.createConnection({ port: server_port, host: server_addr }, () => {
        // 'connect' listener.
        console.log('connected to server!');
        // send the message
        client.write(`${input}`);
    });
    
    // get the data from the server
    // client.on('data', (data) => {
    //     const obj = JSON.parse(data)
    //     client.end();
    //     client.destroy();
    // });

    client.on('end', () => {
        console.log('disconnected from server');
    });    
}
function open(){
    send_data("Open");
}
function close(){
    send_data("Close");
}
