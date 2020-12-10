from scapy.all import *
import matplotlib.pyplot as plt


def startFunction():
    print("\n\n[_N-M-T_] *** WELCOME TO (Scapy) - Latency - Graph Tool ***\n\n")

    # asking for input
    print("\n[_N-M-T_] TYPE IN THE DESTINATION IP.")
    dest = input("DESTINATION IP: ")

    # p = send(IP(dst="192.168.0.1")/ICMP())
    p = send(IP(dest)/ICMP())

    # dest = "192.168.0.105"
    pkt = []
    for i in range(1, 50):
        a = IP(dst=dest) / TCP(flags="S", seq=i, sport=65000, dport=55556)
        pkt.append(a)

    ans, unans = sr(pkt, filter="host {0}".format(dest), inter=0, timeout=1)

    print("scapy version: {}".format(conf.version))

    lat = []
    x = []
    i = 0
    for pkt in ans:
        sent = pkt[0]
        received = pkt[1]
        res = (received.time - sent.sent_time) * 1000
        x.append(i)
        lat.append(res)
        print(res)
        i += 1

    plt.plot(x, lat)
    plt.show()

    print("\n\n[_N-M-T_] *** EXIT FROM (Scapy) - Latency - Graph - Tool ***\n\n")


if (__name__ == '__main__'):
    startFunction()
