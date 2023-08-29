import socket
import json
import serial
import time
serial1 = serial.Serial('/dev/ttyACM0',9600)

HOST = "192.168.0.180" # IP address of your Raspberry PI
PORT = 65432          # Port to listen on (non-privileged ports are > 1023)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    try:
        while 1:
            print("Start server")
            client, clientInfo = s.accept()
            print("server recv from: ", clientInfo)
            data = client.recv(1024)      # receive 1024 Bytes of message in binary format        
            if data != b"":
                # Decode the data
                dataStr = str(data.decode("utf-8"))
                if dataStr[0] == 'O':
                    print("Open the Door.")
                    serial1.write(b'9')
                    time.sleep(3)
                    serial1.write(b'0')
                client.sendall(data)

    except: 
        print("Closing socket")
        client.close()
        s.close()    

