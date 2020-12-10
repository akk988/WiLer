from socketTools import ServerTCP as STCP
from socketTools import ServerUDP as SUDP
from socketTools import ClientTCP as CTCP
from socketTools import ClientUDP as CUDP
import os


def mainFunction():
    while True:
        print("\n\n[_N-M-T_] WELCOME TO TCP / UDP TRAFFIC - TOOL\n\n")
        print("[_N-M-T_] HERE IS THE LIST OF YOUR OPTIONS")
        print("[_N-M-T_] (1) TCP - TRAFFIC - CLIENT")
        print("[_N-M-T_] (2) UDP - TRAFFIC - CLIENT")
        print("[_N-M-T_] (3) TCP - TRAFFIC - SERVER")
        print("[_N-M-T_] (4) UDP - TRAFFIC - SERVER")
        print("[_N-M-T_] (5) EXIT OF TCP - TRAFFIC - SENDER\n")

        print("[_N-M-T_] PLEASE CHOOSE AN OPTION WITH A NUMBER.")

        while True:
            try:
                choice = int(input("[_N-M-T_] OPTION-NUMBER: "))
                if choice > 0 and choice < 6:
                    break
                else:
                    print(
                        "\n[I N F O] THAT'S NOT AN VALID INPUT! PLEASE TRY AGAIN.\n")
            except ValueError:
                print("\n[_N-M-T_] THAT'S NOT AN VALID INPUT! PLEASE TRY AGAIN.\n")

        os.system("clear")

        # ELSE

        if choice == 1:
            print("[I N F O] YOU HAVE CHOSEN TCP - TRAFFIC - CLIENT")
            CTCP.startFunction()
        elif choice == 2:
            print("[I N F O] YOU HAVE CHOSEN UDP - TRAFFIC - CLIENT\n\n")
            CUDP.startFunction()
        elif choice == 3:
            print("[I N F O] YOU HAVE CHOSEN TCP - TRAFFIC - SERVER\n\n")
            STCP.startFunction()
        elif choice == 4:
            print("[I N F O] YOU HAVE CHOSEN UDP - TRAFFIC - SERVER\n\n")
            SUDP.startFunction()
        elif choice == 5:
            print("[I N F O] YOU HAVE CHOSEN EXIT OF TCP - TRAFFIC - SENDER\n\n")
            break

    input("[I N F O] PLEASE PRESS ENTER TO EXIT...")
    print("\n\n[_N-M-T_] EXIT TCP / UDP TRAFFIC - TOOL\n\n")


if (__name__ == '__main__'):
    mainFunction()
