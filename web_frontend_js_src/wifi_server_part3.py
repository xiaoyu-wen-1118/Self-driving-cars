import socket
import picar_4wd as fc
import json
from gpiozero import CPUTemperature
from picar_4wd.speed import Speed

HOST = "192.168.0.180" # IP address of your Raspberry PI
PORT = 65432          # Port to listen on (non-privileged ports are > 1023)
power = 20

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    try:
        reply = {}
        reply["direction"] = "Stop"
        speed4 = Speed(25)
        speed4.start()
        while 1:
            client, clientInfo = s.accept()
            print("server recv from: ", clientInfo)
            data = client.recv(1024)      # receive 1024 Bytes of message in binary format
            # Get CPU temperature
            cpu = CPUTemperature()
            reply["temperature"] = cpu.temperature
            # Get speed
            print("speed is", speed4())
            reply["speed"] = speed4()
            # Get obstacle distance
            distance = fc.get_distance_at(0)
            reply["distance"] = distance
        
            if data != b"":
                # Decode the data
                dataStr = str(data.decode("utf-8"))
                print("Receive:", dataStr)
                if dataStr.isdecimal():
                    new_power = int(dataStr)
                    if new_power > 0 and new_power <= 100:
                        power = new_power
                        print("Set power to", power)
                elif dataStr[0] == 'F':
                    print("Go Forward")
                    fc.forward(power)
                    reply["direction"] = "Forward"
                elif dataStr[0] == 'B':
                    print("Go Backward")
                    fc.backward(power)
                    reply["direction"] = "Backward"
                elif dataStr[0] == 'L':
                    print("Turn Left")
                    fc.turn_left(power)
                    reply["direction"] = "Left"
                elif dataStr[0] == 'R':
                    print("Turn Right")
                    fc.turn_right(power)
                    reply["direction"] = "Right"
                elif dataStr[0] == 'S':
                    print("Stop")
                    fc.stop()
                    reply["direction"] = "Stop"
            
            # Echo back to client
            replymsg = bytes(json.dumps(reply), "utf-8")
            #print("replymsg is", replymsg)
            client.sendall(replymsg)

    except: 
        print("Closing socket")
        speed4.deinit()
        fc.stop()
        client.close()
        s.close()    

