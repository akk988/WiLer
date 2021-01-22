import os


def startFunction():
    print("\u001b[32m")
    print("\n\n[_N-M-T_] *** WELCOME TO  I R T T - CLIENT ***\n\n")
    print("\u001b[37m")

    print("\n[_N-M-T_] TYPE IN THE SERVER IP.")
    IP = input("SERVER IP: ")

    os.system(f"irtt client -i 20ms -l 172 -d 1m --fill=rand --sfill=rand -q {IP}:4000")

    print("\u001b[32m")
    print("\n[_N-M-T_] ...SENDING COMPLETED.")
    input("[I N F O] PLEASE PRESS ENTER TO EXIT...")
    print("\n\n[_N-M-T_] EXIT  I R T T - CLIENT \n\n")
    print("\u001b[32m")

if (__name__ == '__main__'):
    startFunction()