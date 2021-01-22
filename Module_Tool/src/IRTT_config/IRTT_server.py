import os


def startFunction():
    print("\u001b[32m")
    print("\n\n[_N-M-T_] *** WELCOME TO  I R T T - SERVER***\n\n")
    print("\u001b[37m")

    print("\n[_N-M-T_] PRESS ENTER TO START THE SERVER AT PORT 4000")
    input()
    os.system("irtt server")

    print("\u001b[32m")
    print("\n[_N-M-T_] ...SENDING COMPLETED.")
    input("[I N F O] PLEASE PRESS ENTER TO EXIT...")
    print("\n\n[_N-M-T_] EXIT  I R T T - CLIENT \n\n")
    print("\u001b[32m")

if (__name__ == '__main__'):
    startFunction()