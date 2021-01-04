from scapy.all import*

dest = "192.168.0.104"
pkt = []
for i in range(1,180):
    a = IP(dst=dest) / ICMP()
    pkt.append(a)

ans, unans = sr(pkt, filter="host {0}".format(dest), inter=0, timeout=1)

print("scapy version: {}".format(conf.version))

for pkt in ans:
    sent = pkt[0]
    received = pkt[1]
    res = (received.time - sent.sent_time) * 1000
    print(res)
