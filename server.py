import socket
from  threading import Thread
import time, random

SERVER = None
IP_ADDRESS = '127.0.0.1'
PORT = 8080

CLIENTS = {}
flashNumberList =[ i  for i in range(1, 91)]

gameOver = False
playersJoined = False

def acceptConnections():
    global CLIENTS
    global SERVER

    while True:
        player_socket, addr = SERVER.accept()
        player_name = player_socket.recv(1024).decode().strip()

        CLIENTS[player_name] = {}
        CLIENTS[player_name]["player_socket"] = player_socket
        CLIENTS[player_name]["address"] = addr
        CLIENTS[player_name]["player_name"] = player_name


def setup():
    print("\n\t\t\t\t\t*** Welcome To Tambola Game ***\n")

    global SERVER
    global PORT
    global IP_ADDRESS


    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.bind((IP_ADDRESS, PORT))

    SERVER.listen(10)

    print("\t\t\t\tSERVER IS WAITING FOR INCOMING CONNECTIONS...\n")

    acceptConnections()


setup()
