#! /usr/bin/env python
# scapy is a powerful interactive packet manipulation tool, packet generator, network scanner, network discovery, 
# packet sniffer, etc. It can for the moment replace hping, parts of nmap, arpspoof, arp-sk, arping, tcpdump, tshark, p0f, ...
# install scapy on debian with: 
# sudo pip install --pre scapy[basic]
# 

from scapy.all import *
from datetime import datetime

datetime.now().time()

def QoS_ping(host, count=180):

# 
  packet = Ether()/IP(dst=host)/ICMP()
  t=0.0
  for x in range(count):
      ans,unans=srp(packet,iface="wlan0", filter='icmp', verbose=0)
      rx = ans[0][1]
      tx = ans[0][0]
      delta = rx.time-tx.sent_time
      print "Ping, ", delta, ", Time,", datetime.now().time()
      t+=delta
  return (t/count)*1000

if __name__=="__main__":
    total = QoS_ping('192.168.0.103')
    print "TOTAL", total

