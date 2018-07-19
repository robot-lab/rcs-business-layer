import socket
import json
import time
from random import randint
from datetime import datetime
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect(('localhost', 9090))

while True:
    if randint(0, 100) % 2 == 1:
        name = "fanuc"
    else:
        name = "telega"
    dataToSend = {"flag": 0, "name": str(name), "command": str(datetime.now()).replace(':', ';')}
    dataJson = json.dumps(dataToSend)
    sock.send(dataJson.encode())
    time.sleep(0.04)


