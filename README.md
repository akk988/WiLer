# WiLer
Wireless Network Latency Analyzer

Tools for measuring latency in wireless networks

# scapy-Latency (SYN)
The scapy-Latency is a module for higher latency calculation at the xxxxx? layer of the OSI-Model. It's written in Python and it uses scapy to measure the latency of the network from the time and send_time. The protocol used in this model is the xxxxx? . The imported version of scapy can influence the measured latency. A TCP Pings such as TCP SYN can be used if an ICMP echo requests are blocked.  

# socket-Latency
Two programs in Python were prepared to send and receive packtes for each other, either on the same host or on two different ones

# Remote-Network-Evaluation
In a system consist of a control node (cN) and several worker nodes (wN), the network throughput can be measured on each wN from the cN. The scripts for measuring the latency and the bandwidth of the network are prepared for each wN. The cN can call these scripts over SSH and get the results. The cN analyse the results of the network properties for each device and make desicion on reconfiguring the relevant wNs based on the changed network situation, in addition it consider the defined priorities for each wN, regarding data rate the time sensitivity of the running applications. 
