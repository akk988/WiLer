# WiLer
Wireless Network Latency Analyzer

Tools for measuring latency in wireless networks

# scapy-Latency (SYN)
The scapy-Latency is a module for higher latency calculation at the xxxxx? layer of the OSI-Model. It's written in Python and it uses scapy to measure the latency of the network from the time and send_time. The protocol used in this model is the xxxxx? . The imported version of scapy can influence the measured latency. A TCP Pings such as TCP SYN can be used if an ICMP echo requests are blocked.

# iperf3-Network-Bandwidth


# socket-Latency
Two programs in Python were prepared to send and receive packtes for each other, either on the same host or on two different ones

# Remote-Network-Evaluation
In a system consist of a control node (cN) and several worker nodes (wN), the network throughput can be measured on each wN from the cN. The scripts for measuring the latency and the bandwidth of the network are prepared for each wN. The cN can call these scripts over SSH and get the results. The cN analyse the results of the network properties for each device and make desicion on reconfiguring the relevant wNs based on the changed network situation, in addition it consider the defined priorities for each wN, regarding data rate the time sensitivity of the running applications. 

# Modul-Tool
After running the program with Python3, the user can choose a tool to test some network features.
Availabe tools are for example: TCP Traffic Test, UDP Traffic Test, IRTT, Scapy Latency Test, Ostinato, ..
In addition, a Graph of a TCPTraceRoute can be 


Requirements:
install scapy: 
  Debian: $ sudo pip3 install scapy


TODO:
  -Client und Server UDP müssen noch erstellt werden
  -Scapy-Tools müssen auf Funktionalität geschrieben werden
  -Andere Docker-Container müssen noch eingebunden werden für IRTT oder Ostinato
  -Exceptions müssen noch gecatched werden



----------------------------------------------------------------------------------
To ADD a new Network-Tool into NETWORK - MODULE - TOOL:

  - Of course the environment should be customized (in Docker + Working-Tree)
  - There are 4 steps in programm.py:
       1.) ^^Import above this a new tool^^
       2.) ^^Import above this a new tool^^
       3.) <-- increase this number to the number of available tools
       4.) ^^Import above this a new tool^^
    Search for them and add a new Tool.
----------------------------------------------------------------------------------

----------------------------------------------------------------------------------
Docker credentials
   docker build -t moduletool_X .
   -p 172.17.192.1:5050:5050/tcp
   docker run -it -p 192.168.178.25:5050:5050/tcp --name moduletool_5 moduletool_4 bash
   docker run -it -p 192.168.178.25:5050:5050/tcp moduletool_1 bash

   docker start -i moduletool_X
----------------------------------------------------------------------------------

----------------------------------------------------------------------------------
Python Socket Tutorial
  https://www.youtube.com/watch?v=3QiPPX-KeSc&t=955s
----------------------------------------------------------------------------------
