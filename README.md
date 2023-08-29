# Smart-Lock-with-Face-Recognition
## **Motivation**:
Smart lock with face recognition is desired in many scenarios. It can enable contactless
opening and closing. For example, when a package is delivered to home, one may be
working remotely and in an important meeting. It will be very awkward to tell your
colleagues that your need be away from the meeting for several minutes to open the door
or gate. If the door or gate can be remotely controlled, your work won’t be interrupted.
A smart lock can also solve another problem: forgetting the key. Many people have
experienced this situation: You are locked outside the door, but the key is inside the door.
A smart lock with face recognition can open the door without its key when detecting
registered users come home. This function can make elders’ life much easier, they are
more possible to forget the key than young people. In conclusion, the project is
meaningful in terms of both business and society.

## **Technical approach**:
This system should have the following functions: Face photo collection, Face recognition,
Control lock, Remote control.
1. The Raspberry Pi will take photo of new user via the Pi camera installed on the
Raspberry Pi board.
2. With enough photo taken for a user. The Pi will train a face recognition model
based on the collected photos.
3. While running the program, the Pi use the trained model to recognize if a
registered user is captured by the camera.
4. If a registered user is recognized, the Pi will send a message to the Arduino via the
USB. Then the Arduino will control the servo to open or close the lock.
5. The remote control is implemented by wifi connection.
The hardware design is shown in the following figure:

 ![HardwareDesign](https://github.com/xiaoyu-wen-1118/Smart-Lock-with-Face-Recognition/blob/main/HardwareDesign.png) <br>
 Figure 1. The hardware design of the smart lock with face recognition

## **Code implementation**
 * The `take_photo.py` will let user take photo via the Pi-camera. When the user clicks the space, a photo is captured and saved in the dataset/ folder. Later these photos will be used to train the face recognition model.
 * The `train_model.py` will train a face recognition model using the photos captured in the previous step. The encodings.pickle is generated after executing this step.
 * Then when the `runSmartLock.py` is running, it detects faces. If a registered user (xwen20) in this project is recognized, it sends “Open the door” message to the Arduino and after 3 seconds it sends “Close the door” message to the Arduino. If no registered user found it sends “Close the Door” message to Arduino.
 * On the Arduino side, the following codes are uploaded and executed. It sets the Servo angle to 90 degrees when receiving “Open” and sets Servo angle to 0 degrees when receiving “Close”.
 * The remote control is implemented by running the `lock_serve.py` in the Pi. When it receives the “Open” message it will forward this message to Arduino to open the door. When it receives the “Close” message it will forward this message to Arduino to close the door.
 * The following `wifi_client.py` is used to send message remotely to the `lock_server.py` running on the Pi.
