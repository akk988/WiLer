import subprocess
import time
from datetime import datetime

print("Current Time = ", datetime.now().time())

print ('# scapy Latency Remote Tester #')

print ('# python script is prepared on the remote nodes for measuring the latency with scapy #')

# read latency of Node-01
print ('Running the python script on Node 01 ')

#result1 = subprocess.check_output('sshpass -p "fiveg4kmu" ssh -o StrictHostKeyChecking=no pi@192.168.0.103 "cd /home/pi/Wiler && sudo python scapyLatencyEther.py > rem-lat-scap-nw-nt-rpi1.txt"', shell=True)
# Using shlex.split --> ['sshpass', '-p', 'fiveg4kmu', 'ssh', '-o', 'StrictHostKeyChecking=no', 'pi@192.168.0.103', 'cd /home/pi/Wiler && sudo python scapyLatencyEther.py > rem-lat-scap-nw-nt-rpi1.txt']
# subprocess.run(['sshpass', '-p', 'fiveg4kmu', 'ssh', '-o', 'StrictHostKeyChecking=no', 'pi@192.168.0.103', 'cd /home/pi/Wiler && sudo python scapyLatencyEther.py > rem-lat-scap-nw-nt-rpi1.txt'], check=False)

# Using subprocess.Popen BECAUSE --> By default, subprocess.Popen does not stop processing of a Python program if its command has not finished executing. 

#subprocess.Popen(["sudo","sshpass", "-p", "fiveg4kmu", "ssh", "-o", "StrictHostKeyChecking=no", "pi@192.168.0.103", "cd /home/pi/Wiler && sudo python scapyLatencyEther.py > rem-lat-scap-nw-nt-rpi1.txt"])

subprocess.Popen(["sudo","sshpass", "-p", "fiveg4kmu", "ssh", "-o", "StrictHostKeyChecking=no", "pi@192.168.0.103", "cd", "/home/pi/Wiler", "&&", "sudo", "python", "scapyLatencyEther.py", ">", "rem-lat-scap-nw-nt-rpi1.txt"])

print("Current Time = ", datetime.now().time())

print("Waiting 5 seconds before running the next command")

time.sleep(4.0)





print ('Running the python script on Node 02 ')



#result2 = subprocess.check_output('sshpass -p "fiveg4kmu" ssh -o StrictHostKeyChecking=no pi@192.168.0.101 "cd /home/pi/prio-TC-Tests && sudo python scapyLatencyEther.py > rem-lat-scap-nw-nt-rpi3.txt"', shell=True)

#subprocess.Popen(["sudo","sshpass", "-p", "fiveg4kmu", "ssh", "-o", "StrictHostKeyChecking=no", "pi@192.168.0.101", "cd /home/pi/prio-TC-Tests && sudo python scapyLatencyEther.py > rem-lat-scap-nw-nt-rpi3.txt"])

subprocess.Popen(["sudo","sshpass", "-p", "fiveg4kmu", "ssh", "-o", "StrictHostKeyChecking=no", "pi@192.168.0.101", "cd", "/home/pi/prio-TC-Tests", "&&", "sudo", "python", "scapyLatencyEther.py", ">", "rem-lat-scap-nw-nt-rpi3.txt"])



print("Current Time = ", datetime.now().time())

print("Waiting 5 seconds before running the next command")

time.sleep(4.0)

print ('Running the second python script on Node 02 ')
subprocess.Popen(["sudo","sshpass", "-p", "fiveg4kmu", "ssh", "-o", "StrictHostKeyChecking=no", "pi@192.168.0.101", "cd", "/home/pi/prio-TC-Tests", "&&", "sudo", "python", "scapyLatencyEther.py", ">", "rem-lat-scap-nw-nt-rpi3-2.txt"])
print ('Running the third python script on Node 02 ')
subprocess.Popen(["sudo","sshpass", "-p", "fiveg4kmu", "ssh", "-o", "StrictHostKeyChecking=no", "pi@192.168.0.101", "cd", "/home/pi/prio-TC-Tests", "&&", "sudo", "python", "scapyLatencyEther.py", ">", "rem-lat-scap-nw-nt-rpi3-3.txt"])
print ('Running the second python script on Node 01 ')
subprocess.Popen(["sudo","sshpass", "-p", "fiveg4kmu", "ssh", "-o", "StrictHostKeyChecking=no", "pi@192.168.0.103", "cd", "/home/pi/Wiler", "&&", "sudo", "python", "scapyLatencyEther.py", ">", "rem-lat-scap-nw-nt-rpi1-2.txt"])







print ('Running the python script on Node 03 ')

#result3 = subprocess.check_output('sshpass -p "fiveg4kmu" ssh -o StrictHostKeyChecking=no pi@192.168.0.100 "cd /home/pi/WiLer/scapy && sudo python scapyLatencyEther.py > rem-lat-scap-nw-nt-rpi4.txt"', shell=True)

#subprocess.run('sshpass -p "fiveg4kmu" ssh -o StrictHostKeyChecking=no pi@192.168.0.100 "cd /home/pi/WiLer/scapy && sudo python scapyLatencyEther.py > rem-lat-scap-nw-nt-rpi4.txt"', shell=True, check=True)

#subprocess.Popen(["sudo","sshpass", "-p", "fiveg4kmu", "ssh", "-o", "StrictHostKeyChecking=no", "pi@192.168.0.100", "cd /home/pi/WiLer/scapy && sudo python scapyLatencyEther.py > rem-lat-scap-nw-nt-rpi4.txt"])

subprocess.Popen(["sudo","sshpass", "-p", "fiveg4kmu", "ssh", "-o", "StrictHostKeyChecking=no", "pi@192.168.0.100", "cd", "/home/pi/WiLer/scapy", "&&", "sudo", "python", "scapyLatencyEther.py", ">", "rem-lat-scap-nw-nt-rpi4.txt"])



#print (result1)

#print (result2)

#print (result3)



print ('The latency test is done!')
