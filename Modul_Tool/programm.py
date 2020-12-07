from socketTools import socketTrafficMain as stm
from scapyTools import tcpTraceRouteGraph as ttrg
from scapyTools import scapyLatency as sl
from scapyTools import latencyGraph as lg
from ast import literal_eval
import os


print("\n\n\n")
print("[-----------------------------------------------------------------]")
print("[************************* W E L C O M E *************************]")
print("[*************************      T O      *************************]")
print("[************************* N E T W O R K *************************]")
print("[********************* M O D U L E - T O O L *********************]")
print("[-----------------------------------------------------------------]")
print("\n\n\n")

print("[_N-M-T_] ...PRESS ENTER FOR START...\n")
input()

while True:
    print("[_N-M-T_] HERE IS THE LIST OF OUR AVAILABLE PROGRAMS")
    print("[_N-M-T_] (0) EXIT OF MODULE - TOOL\n")
    print("[_N-M-T_] (1) TCP / UDP TRAFFIC - TOOL")
    print("[_N-M-T_] (2) IRTT")
    print("[_N-M-T_] (3) Scapy")
    print("[_N-M-T_] (4) Ostinato")
    print("[_N-M-T_] (5) Others...")
    print("[_N-M-T_] (6) (Scapy) Latency-Graph\n")
    print("[_N-M-T_] (7) (Scapy) Latency\n")
    print("[_N-M-T_] (8) (Scapy) TCPTraceRoute Graph\n")

    print("[_N-M-T_] PLEASE CHOOSE A PROGRAM WITH A NUMBER.")

    while True:
        try:
            choice = int(input("[_N-M-T_] PROGRAM-NUMBER: "))
            if choice >= 0 and choice <= 8:
                break
            else:
                print("\n[_N-M-T_] THAT'S NOT A VALID INPUT! PLEASE TRY AGAIN.\n")
        except:
            print("\n[_N-M-T_] THAT'S NOT A VALID INPUT! PLEASE TRY AGAIN.\n")

    os.system("cls")

    if choice == 0:
        print("[_N-M-T_] YOU HAVE CHOSEN EXIT OF MODULE - TOOL\n\n")
        break
    elif choice == 1:
        print("[_N-M-T_] YOU HAVE CHOSEN TCP / UDP TRAFFIC - TOOL")
        stm.mainFunction()
    elif choice == 2:
        print("[_N-M-T_] YOU HAVE CHOSEN IRTT\n\n")
        print("[_N-M-T_] CURRENTLY NOT AVAILABLE ... COMMING SOON")
    elif choice == 3:
        print("[_N-M-T_] YOU HAVE CHOSEN Scapy\n\n")
        print("[_N-M-T_] CURRENTLY NOT AVAILABLE ... COMMING SOON")
    elif choice == 4:
        print("[_N-M-T_] YOU HAVE CHOSEN Ostinato\n\n")
        print("[_N-M-T_] CURRENTLY NOT AVAILABLE ... COMMING SOON")
    elif choice == 5:
        print("[_N-M-T_] YOU HAVE CHOSEN Others...\n\n")
        print("[_N-M-T_] CURRENTLY NOT AVAILABLE ... COMMING SOON")
    elif choice == 6:
        print("[_N-M-T_] YOU HAVE CHOSEN (Scapy) Latency-Graph\n\n")
        lg.startFunction()
    elif choice == 7:
        print("[_N-M-T_] YOU HAVE CHOSEN (Scapy) Latency\n\n")
        sl.startFunction()
    elif choice == 8:
        print("[_N-M-T_] YOU HAVE CHOSEN (Scapy) TCPTraceRoute Graph\n\n")
        ttrg.startFunction()


print("\n\n[_N-M-T_] GOOD BYE!\n\n")
