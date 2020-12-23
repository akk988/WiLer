import subprocess

print ('#1 Controller-Node starts . . .')

latencyN1Ist = 10
latencyN1Soll = 15

# read latency of Node-01

print ('The network latency on Node-01 is %s.' % latencyN1Ist)

print ('#2 Reading the hostname from Node-01 . . . ')
result = subprocess.check_output('sshpass -f pass-n1 ssh pi@172.21.5.148 hostname', shell=True)
print (result)

print ('Reading the current network latency from Node-01 . . . ')
result2 = subprocess.check_output('sshpass -f pass-n1 ssh pi@172.21.5.148 ping -c 1 google.com', shell=True)
print (result2)
print ('The latency on Node-01 is %s.' % result2)
# compare / evaluate latency of Node-01

# change / adapt latency of Node-01
print ('#3 Changing the latency (increasing + 100ms)')
subprocess.check_output('sshpass -f pass-n1 ssh -t pi@172.21.5.148 sudo tc qdisc add dev wlan0 root netem delay 100ms
', shell=True)
print ('Reading the current network latency from Node-01 . . . ')
result2 = subprocess.check_output('sshpass -f pass-n1 ssh pi@172.21.5.148 ping -c 1 google.com', shell=True)
print (result2)
print ('The latency on Node-01 is %s.' % result2)

print ('#4 Changing the latency (removing - 100ms)')
subprocess.check_output('sshpass -f pass-n1 ssh -t pi@172.21.5.148 sudo tc qdisc del dev wlan0 root', shell=True)

result3 = subprocess.check_output('sshpass -f pass-n1 ssh pi@172.21.5.148 ping -c 1 google.com', shell=True)
print (result3)
print ('The latency on Node-01 is %s.' % result3)

# check new latency

# Latency of the system:
# 1. cyclic test the Node-01
# 2. wireshark the network!