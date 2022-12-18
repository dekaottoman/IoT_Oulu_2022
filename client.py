import socket
import time
import random

def direction(num:int):
    if num == 0:
        return "East"
    elif num == 1:
        return "West"
    elif num == 2:
        return "North"
    elif num == 3:
        return "South"

if __name__ == "__main__":
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("localhost", 9999))

    while True:
        time.sleep(3)
        temp = random.randint(15,30)
        humi = random.randint(30,50)
        dire = random.randint(0,3)
        dire = direction(dire)

        data = str(temp) + "<D>" + str(humi) + "<D>" + str(dire)

        client.send(data.encode("utf-8"))
        msg = client.recv(1024).decode("utf-8")
        print(msg)