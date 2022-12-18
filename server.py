import socket
from blockchain import add_node

if __name__ == "__main__":
    folder_path = input("Enter the path to the folder containing the blockchain\t>>")

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("localhost", 9999))
    server.listen()

    client, addr = server.accept()

    while True:
        data = client.recv(1024).decode("utf-8")
        add_node(data,folder_path)
        print(data)
        client.send(("Received\t>> " + data).encode("utf-8"))