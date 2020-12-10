from scapy.all import *


def startFunction():
    print("\n\n[_N-M-T_] *** WELCOME TO (Scapy) TCP - Trace - Route - Graph ***\n\n")

    res, unans = traceroute(["www.microsoft.com", "www.cisco.com", "www.yahoo.com"], dport=[
                            80, 443], maxttl=20, retry=-2)
    res.graph(target="> /tmp/tcpTraceRoute-Graph.svg")

    print("\n\n[_N-M-T_] *** EXIT FROM (Scapy) TCP - Trace - Route - Graph ***\n\n")


if (__name__ == '__main__'):
    startFunction()
