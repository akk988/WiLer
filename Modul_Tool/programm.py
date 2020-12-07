from socketTools import socketTCP as TCP
from ast import literal_eval
import os


print("\n\n\n")
print("[-----------------------------------------------------------------]")
print("[************************* W E L C O M E *************************]")
print("[*************************      T O      *************************]")
print("[********************* M O D U L E - T O O L *********************]")
print("[-----------------------------------------------------------------]")
print("\n\n\n")

print("[_M-T_] ...PRESS ENTER FOR START...\n")
input()

while True:
    print("[_M-T_] HERE IS THE LIST OF OUR AVAILABLE PROGRAMS")
    print("[_M-T_] (1) TCP / UDP TRAFFIK - SENDER")
    print("[_M-T_] (2) IRTT")
    print("[_M-T_] (3) Scapy")
    print("[_M-T_] (4) Ostinato")
    print("[_M-T_] (5) Others...")
    print("[_M-T_] (6) EXIT OF MODULE - TOOL\n")

    print("[_M-T_] PLEASE CHOOSE A PROGRAM WITH A NUMBER.")

    while True:
        try:
            choice = int(input("[_M-T_] PROGRAM-NUMBER: "))
            if choice > 0 and choice <= 6:
                break
            else:
                print("\n[_M-T_] THAT'S NOT A VALID INPUT! PLEASE TRY AGAIN.\n")
        except:
            print("\n[_M-T_] THAT'S NOT A VALID INPUT! PLEASE TRY AGAIN.\n")

    os.system("cls")

    if choice == 1:
        print("[_M-T_] YOU CHOOSE TCP / UDP TRAFFIK - SENDER")
        TCP.startFunction()
    elif choice == 2:
        print("[_M-T_] YOU CHOOSE IRTT\n\n")
    elif choice == 3:
        print("[_M-T_] YOU CHOOSE Scapy\n\n")
    elif choice == 4:
        print("[_M-T_] YOU CHOOSE Ostinato\n\n")
    elif choice == 5:
        print("[_M-T_] YOU CHOOSE Others...\n\n")
    elif choice == 6:
        print("[_M-T_] YOU CHOOSE EXIT OF MODULE - TOOL\n\n")
        break


print("\n\n[_M-T_] GOOD BYE!\n\n")
