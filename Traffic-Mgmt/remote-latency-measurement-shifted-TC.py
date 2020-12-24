import subprocess

import time

from datetime import datetime

print("Current Time = ", datetime.now().time())
print ('# scapy Latency Remote Tester #')
print ('# python script is prepared on the remote nodes for measuring the latency with scapy #')

# read latency of Node-01
# change / adapt latency of Node-01
#print ('# Changing the latency (50ms)')
# Any tc role must be deleted before adding a new role

subprocess.Popen(["sudo","sshpass", "-p", "fiveg4kmu", "ssh", "-o", "StrictHostKeyChecking=no", "pi@192.168.0.103", "sudo", "tc", "qdisc", "delete", "dev", "wlan0", "root"])
time.sleep(0.5)

subprocess.Popen(["sudo","sshpass", "-p", "fiveg4kmu", "ssh", "-o", "StrictHostKeyChecking=no", "pi@192.168.0.103", "sudo", "tc", "qdisc", "add", "dev", "wlan0", "root", "tbf", "rate", "10mbit", "burst", "32kbit", "latency", "50ms"])

time.sleep(0.5)

print ('Running the python script on Node 01 ')

# Using shlex.split --> ['sshpass', '-p', 'fiveg4kmu', 'ssh', '-o', 'StrictHostKeyChecking=no', 'pi@192.168.0.103', 'cd /home/pi/Wiler && sudo python scapyLatencyEther.py > rem-lat-scap-nw-nt-rpi1.txt']
# Using subprocess.Popen BECAUSE --> By default, subprocess.Popen does not stop processing of a Python program if its command has not finished executing. 

subprocess.Popen(["sudo","sshpass", "-p", "fiveg4kmu", "ssh", "-o", "StrictHostKeyChecking=no", "pi@192.168.0.103", "cd", "/home/pi/Wiler", "&&", "sudo", "python", "scapyLatencyEther.py", ">", "rem-lat-scap-nw-TC-rpi1.txt"])

print("Current Time = ", datetime.now().time())
print("Waiting 5 seconds before running the next command")
time.sleep(5.0)


print ('Running the python script on Node 02 ')
#print ('# Changing the latency (increasing + 100ms)')
# Any tc role must be deleted before adding a new role

subprocess.Popen(["sudo","sshpass", "-p", "fiveg4kmu", "ssh", "-o", "StrictHostKeyChecking=no", "pi@192.168.0.101", "sudo", "tc", "qdisc", "delete", "dev", "wlan0", "root"])

time.sleep(0.5)
subprocess.Popen(["sudo","sshpass", "-p", "fiveg4kmu", "ssh", "-o", "StrictHostKeyChecking=no", "pi@192.168.0.101", "sudo", "tc", "qdisc", "add", "dev", "wlan0", "root", "tbf", "rate", "10mbit", "burst", "32kbit", "latency", "200ms"])

time.sleep(0.5)

#result2 = subprocess.check_output('sshpass -p "fiveg4kmu" ssh -o StrictHostKeyChecking=no pi@192.168.0.101 "cd /home/pi/prio-TC-Tests && sudo python scapyLatencyEther.py > rem-lat-scap-nw-nt-rpi3.txt"', shell=True)
#subprocess.Popen(["sudo","sshpass", "-p", "fiveg4kmu", "ssh", "-o", "StrictHostKeyChecking=no", "pi@192.168.0.101", "cd /home/pi/prio-TC-Tests && sudo python scapyLatencyEther.py > rem-lat-scap-nw-nt-rpi3.txt"])

subprocess.Popen(["sudo","sshpass", "-p", "fiveg4kmu", "ssh", "-o", "StrictHostKeyChecking=no", "pi@192.168.0.101", "cd", "/home/pi/prio-TC-Tests", "&&", "sudo", "python", "scapyLatencyEther.py", ">", "rem-lat-scap-nw-TC-rpi3.txt"])

print("Current Time = ", datetime.now().time())
print("Waiting 5 seconds before running the next command")
time.sleep(5.0)

print ('Running the python script on Node 03 ')
#subprocess.Popen(["sudo","sshpass", "-p", "fiveg4kmu", "ssh", "-o", "StrictHostKeyChecking=no", "pi@192.168.0.100", "cd", "/home/pi/WiLer/scapy", "&&", "sudo", "python", "scapyLatencyEther.py", ">", "rem-lat-scap-nw-nt-rpi4.txt"])
print ('The latency test is done!')
