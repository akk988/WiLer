import socket

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MSG = "!DISCONNECT"
SERVER = "172.21.64.1"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
  message = msg.encode(FORMAT)
  msg_length = len(message)
  send_length = str(msg_length).encode(FORMAT)
  send_length += b' ' * (HEADER - len(send_length))
  client.send(send_length)
  client.send(message)
  received_msg = client.recv(2048).decode(FORMAT)
  print(received_msg)

send("Hello my Friend!")
send(DISCONNECT_MSG)