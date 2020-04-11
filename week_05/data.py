from ex_05_client_for_metrics import Client
from ex_05_client_for_metrics import ClientError
client = Client("127.0.0.1", 8888, timeout=15)
client.get("*")

import socket
sock = socket.create_connection(('127.0.0.1', 8888), 15)
sock.send(b'data from client2')
sock.recv(1024)