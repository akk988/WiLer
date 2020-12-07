import os
import socket


def startFunction():
    print("\n\n[_M-T_] ... WELCOME TO TCP - TRAFFIK - SENDER\n\n")

    # asking for input
    print("\n[_M-T_] TYPE IN THE SERVER IP.")
    IP = input("SERVER IP: ")
    print("\n[_M-T_] TYPE IN THE MESSAGE YOU WANTED TO SEND.")
    MSG = input("MESSAGE: ")
    print("\n[_M-T_] TYPE IN HOW MANY TIMES YOU WANTED TO SEND.")
    TIMES = input("TIMES: ")

    # Define const variables
    HEADER = 64
    PORT = 5050
    FORMAT = 'utf-8'
    DISCONNECT_MSG = "!DISCONNECT"
    # SERVER = "172.23.160.1"
    ADDR = (IP, PORT)

    # # create a TCP socket & connect to Server
    # client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # client.connect(ADDR)

    # def send(msg):
    #     message = msg.encode(FORMAT)
    #     msg_length = len(message)
    #     send_length = str(msg_length).encode(FORMAT)
    #     send_length += b' ' * (HEADER - len(send_length))
    #     client.send(send_length)
    #     client.send(message)
    #     received_msg = client.recv(2048).decode(FORMAT)
    #     print(received_msg)

    # for i in range(TIMES):
    # send("Hello my Friend!")

    # send(DISCONNECT_MSG)

    input()
    print("\n\n[_M-T_] EXIT TCP - TRAFFIK - SENDER\n\n")


if (__name__ == '__main__'):
    startFunction()
