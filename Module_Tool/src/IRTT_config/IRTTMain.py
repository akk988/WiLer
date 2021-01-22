from IRTT_config import IRTT_server
from IRTT_config import IRTT_client
import os


def mainFunction():
    while True:
        print("\u001b[32m")
        print("\n\n[_N-M-T_] WELCOME TO IRTT - TOOL\n\n")
        print("\u001b[32m")
        print("[_N-M-T_] HERE IS THE LIST OF YOUR OPTIONS")
        print("[_N-M-T_] (1) IRTT - CLIENT")
        print("[_N-M-T_] (2) IRTT - SERVER")
        print("[_N-M-T_] (3) EXIT OF IRTT - TOOL\n")

        print("[_N-M-T_] PLEASE CHOOSE AN OPTION WITH A NUMBER.")

        while True:
            try:
                choice = int(input("[_N-M-T_] OPTION-NUMBER: "))
                if choice > 0 and choice < 4:
                    break
                else:
                    print(
                        "\n[I N F O] THAT'S NOT AN VALID INPUT! PLEASE TRY AGAIN.\n")
            except ValueError:
                print("\n[_N-M-T_] THAT'S NOT AN VALID INPUT! PLEASE TRY AGAIN.\n")

        os.system("clear")

        # ELSE

        if choice == 1:
            print("[I N F O] YOU HAVE CHOSEN IRTT - CLIENT")
            IRTT_client.startFunction()
        elif choice == 2:
            print("[I N F O] YOU HAVE CHOSEN IRTT - SERVER\n\n")
            IRTT_server.startFunction()
        elif choice == 3:
            print("[I N F O] YOU HAVE CHOSEN EXIT IRTT - TOOL\n\n")
            break

    print("\u001b[32m")
    input("[I N F O] PLEASE PRESS ENTER TO EXIT...")
    print("\n\n[_N-M-T_] EXIT IRTT - TOOL\n\n")
    print("\u001b[32m")

if (__name__ == '__main__'):
    mainFunction()