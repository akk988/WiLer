import socket
import threading
import os


def startFunction():
    print("\n\n[_N-M-T_] *** WELCOME TO TCP - TRAFFIC - SERVER ***\n\n")

    print("\n[_N-M-T_] TYPE IN THE YOUR LISTENING IP.")
    print(
        f"\n[I N F O] YOUR HOST IP IS: {socket.gethostbyname(socket.gethostname())}")
    print(
        f"\n\n[I N F O] BECAUSE IT COULD BE ANOTHER ONE YOU COULD CHOOSE FROM HERE...")
    print(f"\n\n[I N F O] DO YOU WANTED TO OPEN YOUR AVAILABLE IP - TABLE?\n\n")

    print("[_N-M-T_] (1) Yes")
    print("[_N-M-T_] (2) No")

    print("\n[_N-M-T_] PLEASE CHOOSE AN OPTION WITH A NUMBER.")

    while True:
        try:
            option = int(input("OPTION: "))
            break
        except ValueError:
            print("\n[I N F O] THAT'S NOT AN VALID INPUT! PLEASE TRY AGAIN.\n")

        #     if choice == 1:
        #       print("[I N F O] YOU HAVE CHOSEN TCP - TRAFFIC - CLIENT")
        #     CTCP.startFunction()
        # elif choice == 2:

    try:
        os.system("ipconfig")
    except:
        os.system("ifconfig")

    SERVERIP = input("SERVER IP: ")

    HEADER = 64
    PORT = 5050
    # SERVER = socket.gethostbyname(socket.gethostname())
    # SERVER = '192.168.0.100'
    ADDR = (SERVERIP, PORT)
    FORMAT = 'utf-8'
    DISCONNECT_MSG = "!DISCONNECT"

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)

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
        print(f"[LISTENING] Server is listending on {SERVER}")
        while True:
            conn, addr = server.accept()
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.start()
            print(f"[ACTIVE CONNECTIONS] {threading.activeCount()- 1} ")

    print("[STARTING] server is starting.......")
    start()


if (__name__ == '__main__'):
    startFunction()
