from scapy.all import*
#p=send(IP(dst="192.168.0.1")/ICMP())
dest = "192.168.0.105"
pkt = []
for i in range(1,50):
    a = IP(dst=dest) / TCP(flags="S", seq=i, sport=65000, dport=55556)
    pkt.append(a)

ans, unans = sr(pkt, filter="host {0}".format(dest), inter=0, timeout=1)

print("scapy version: {}".format(conf.version))

for pkt in ans:
    sent = pkt[0]
    received = pkt[1]
    res = (received.time - sent.sent_time) * 1000
    print(res)
