import socket


def startFunction():
    print("\n\n[_N-M-T_] *** WELCOME TO TCP - TRAFFIC - CLIENT ***\n\n")

    # asking for input
    print("\n[_N-M-T_] TYPE IN THE SERVER IP.")
    IP = input("SERVER IP: ")
    print("\n[_N-M-T_] TYPE IN THE MESSAGE YOU WANTED TO SEND.")
    MSG = input("MESSAGE: ")
    print("\n[_N-M-T_] TYPE IN HOW MANY TIMES YOU WANTED TO SEND.")
    while True:
        try:
            TIMES = int(input("TIMES: "))
            break
        except ValueError:
            print("\n[I N F O] THAT'S NOT AN VALID INPUT! PLEASE TRY AGAIN.\n")

    # Define const variables
    HEADER = 64
    PORT = 5050
    FORMAT = 'utf-8'
    DISCONNECT_MSG = "!DISCONNECT"
    ADDR = (IP, PORT)

    # create a TCP socket & connect to Server
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)

    def sendMessage(msg):
        message = msg.encode(FORMAT)
        msg_length = len(message)
        send_length = str(msg_length).encode(FORMAT)
        send_length += b' ' * (HEADER - len(send_length))
        client.send(send_length)
        client.send(message)
        received_msg = client.recv(2048).decode(FORMAT)
        print("[TCP FROM SERVER] RECEIVED MESSAGE:", received_msg)

    print(f"\n[_N-M-T_] SENDING {TIMES} x {MSG} to {IP} ...\n")
    for i in range(TIMES):
        sendMessage(MSG)
    sendMessage(DISCONNECT_MSG)
    print(f"\n[_N-M-T_] ...SENDING COMPLETED.")

    input("[I N F O] PLEASE PRESS ENTER TO EXIT...")
    print("\n\n[_N-M-T_] EXIT TCP - TRAFFIC - CLIENT\n\n")


if (__name__ == '__main__'):
    startFunction()
