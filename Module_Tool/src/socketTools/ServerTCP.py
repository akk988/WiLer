import socket
import threading
import os


def welcome_function():
    print("\n\n[_N-M-T_] *** WELCOME TO TCP - TRAFFIC - SERVER ***\n\n")

    # print("\n[_N-M-T_] TYPE IN THE YOUR LISTENING IP.")
    print(
        f"[I N F O] YOUR HOST IP IS: {socket.gethostbyname(socket.gethostname())}")
    print(f"[I N F O] IT COULD BE THAT YOUR IP ADDRESS DIFFERS FROM THIS ONE")
    print(f"[I N F O] DO YOU WANT TO OPEN YOUR AVAILABLE IP - TABLE?\n\n")

    print("[_N-M-T_] (1) Yes")
    print("[_N-M-T_] (2) No")

    print("\n[_N-M-T_] PLEASE CHOOSE AN OPTION WITH A NUMBER.")

    while True:
        try:
            option = int(input("OPTION: "))
            if option >= 1 and option <= 2:
                break
            else:
                print("\n[I N F O] THAT'S NOT AN VALID INPUT! PLEASE TRY AGAIN.\n")
        except ValueError:
            print("\n[I N F O] THAT'S NOT AN VALID INPUT! PLEASE TRY AGAIN.\n")

    if option == 1:
        print("[I N F O] LOADING YOUR IP-DATA...")
        os.system("ipconfig")  # for windows
        os.system("ifconfig")  # for linux
        os.system("ip addr show lo")

    print("[_N-M-T_] PLEASE INSERT NOW YOUR IP")
    return input("SERVER IP: ")


def startFunction():
    serving = True
    while serving:
        SERVERIP = welcome_function()
        HEADER = 64
        PORT = 5050
        # SERVER = socket.gethostbyname(socket.gethostname())
        # SERVER = '192.168.0.100'
        ADDR = (SERVERIP, PORT)
        FORMAT = 'utf-8'
        DISCONNECT_MSG = "!DISCONNECT"
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        def handle_client(conn, addr):
            print(f"[NEW CONNECTION] {addr} connected.")

            connected = True
            while connected:
                msg_length = conn.recv(HEADER).decode(FORMAT)
                if msg_length:
                    msg_length = int(msg_length)
                    msg = conn.recv(msg_length).decode(FORMAT)
                    if msg == DISCONNECT_MSG:
                        connected = False
                        print("[DISCONNECTING]")

                    print(f"[{addr}] {msg}")
                    conn.send("MSG received".encode(FORMAT))
            conn.close

        def start():
            server.listen()
            print(f"[LISTENING] Server is listening on {SERVERIP}")
            while True:
                conn, addr = server.accept()
                thread = threading.Thread(
                    target=handle_client, args=(conn, addr))
                thread.start()
                print(f"[ACTIVE CONNECTIONS] {threading.activeCount()- 1} ")

        try:
            server.bind(ADDR)
            print("[STARTING] Server is starting...")
            start()
        except OSError:
            print("\n[_N-M-T_] CONNECTING TO SERVER FAILED.")
            input("PRESS ENTER TO TRY AGAIN")
            os.system("cls")  # for windows
            # os.system("clear")    #for linux


if (__name__ == '__main__'):
    startFunction()
