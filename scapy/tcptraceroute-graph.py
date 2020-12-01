from scapy.all import*

res, unans = traceroute(["www.microsoft.com","www.cisco.com","www.yahoo.com"],dport=[80,443],maxttl=20,retry=-2)
res.graph(target="> /tmp/tcpTraceRoute-Graph.svg")
