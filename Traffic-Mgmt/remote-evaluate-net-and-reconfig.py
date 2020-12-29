## sshpass
# Install sshpass on the controller node
# Create a file for passwords (sshpass -f) / or use directly (sshpass -p) 
# If sshpass doesn't work: Then generate and compy ssh keys as follows
# on controller node $ ssh-keygen
# copy to the node to be controlled: $ ssh-copy-id -i ~/.ssh/id_rsa.pub pi@192.168.0.101
#### sshpass
## The Problem with sshpass: https://askubuntu.com/questions/282319/how-to-use-sshpass --> -o StrictHostKeyChecking=no
##Your error-code may differ and looking at the code linked above may give you some insight.
##If your issue is an invalid host-key you should think twice about overriding the error with a CLI option. Your machine could be compromised or you may be subject to a MITM attack! If you are 100% certain that this is not the case and if you have no means to keep the verified host-keys up-to date, you can use a command like this:

# This script does following: 
# 1. ssh to two worker nodes and cd to the path, where scapy and iperf3 results must be saved.
# 2. run a first test for latency and bandwidth and save the results in lat1.txt and bw2.txt
# 3. calculate the new bandwidth (later also latency) for each wN
# 4. apply new qdisc config for each wN
# 5. run a second test to ensure the results

import subprocess

print ('== Controller-Node starts . . . ==')
print ('== Scanning for worker nodes !!! ==')

hostname = subprocess.Popen(["sudo","sshpass", "-p", "fiveg4kmu", "ssh", "-o", "StrictHostKeyChecking=no", "pi@192.168.0.103", "sudo", "hostname"], stdout=subprocess.PIPE)
hn = hostname.stdout.read()
print ('== wN available:', hn)
hostname = subprocess.Popen(["sudo","sshpass", "-p", "fiveg4kmu", "ssh", "-o", "StrictHostKeyChecking=no", "pi@192.168.0.101", "sudo", "hostname"], stdout=subprocess.PIPE)
hn = hostname.stdout.read()
print ('== wN available:', hn)
# TODO: Change hostname on each wN

print ('===== Test 1: Latency and Bandwidth from each worker node ======')
print ('== Internal Latency Test ==')

# run scapy script on host 
p = subprocess.Popen(["sudo","sshpass", "-p", "fiveg4kmu", "ssh", "-o", "StrictHostKeyChecking=no", "pi@192.168.0.103", "cd", "/home/pi/Wiler", "&&", "sudo", "python", "scapyLatencyEther.py", ">", "lat-in-1.txt"],stdout=subprocess.PIPE)
# TODO: find a better way to wait a Popen!
p2 = p.stdout.read()
hostlatin1 = subprocess.Popen(["sudo","sshpass", "-p", "fiveg4kmu", "ssh", "-o", "StrictHostKeyChecking=no", "pi@192.168.0.103", "cd", "/home/pi/Wiler", "&&", "awk","'NR>1{exit} {print $2}' lat-in-1.txt"], stdout=subprocess.PIPE)
hli1 = hostlatin1.stdout.read()
hli1s = float(hli1[1:5])
print ('== Internal Latency from host 1 = ', hli1s)

p = subprocess.Popen(["sudo","sshpass", "-p", "fiveg4kmu", "ssh", "-o", "StrictHostKeyChecking=no", "pi@192.168.0.101", "cd", "/home/pi/Wiler", "&&", "sudo", "python", "scapyLatencyEther.py", ">", "lat-in-2.txt"], stdout=subprocess.PIPE)
p2 = p.stdout.read()

hostlatin2 = subprocess.Popen(["sudo","sshpass", "-p", "fiveg4kmu", "ssh", "-o", "StrictHostKeyChecking=no", "pi@192.168.0.101", "cd", "/home/pi/Wiler", "&&", "awk","'NR>1{exit} {print $2}' lat-in-2.txt"], stdout=subprocess.PIPE)
hli2 = hostlatin2.stdout.read()
hli2s = float(hli2[1:5])
print ('== Internal Latency from host 2 = ', hli2s)
# TODO: external latency test --> ping google

print ('== Bandwidth Test ==')

p = subprocess.Popen(["sudo","sshpass", "-p", "fiveg4kmu", "ssh", "-o", "StrictHostKeyChecking=no", "pi@192.168.0.103", "cd", "/home/pi/Wiler", "&&", "sudo", "./iperf3server.sh"],stdout=subprocess.PIPE)
# TODO: find a better way to wait a Popen!
#p2 = p.stdout.read()
#hostlatin1 = subprocess.Popen(["sudo","sshpass", "-p", "fiveg4kmu", "ssh", "-o", "StrictHostKeyChecking=no", "pi@192.168.0.103", "cd", "/home/pi/Wiler", "&&", "awk","'FNR == 8 {print $7}' bw-in-1-server.txt"], stdout=subprocess.PIPE)
#hli1 = hostlatin1.stdout.read()
#hli1s = float(hli1[1:5])
#print ('== Internal Latency from host 1 = ', hli1s)

p = subprocess.Popen(["sudo","sshpass", "-p", "fiveg4kmu", "ssh", "-o", "StrictHostKeyChecking=no", "pi@192.168.0.101", "cd", "/home/pi/Wiler", "&&", "sudo", "iperf3", "-c", "192.168.0.103", "-i","1","-t","10",">", "bw-in-2-client.txt"], stdout=subprocess.PIPE)
p2 = p.stdout.read()

hostlatin2 = subprocess.Popen(["sudo","sshpass", "-p", "fiveg4kmu", "ssh", "-o", "StrictHostKeyChecking=no", "pi@192.168.0.101", "cd", "/home/pi/Wiler", "&&", "awk","'FNR == 8 {print $7}' bw-in-2-client.txt"], stdout=subprocess.PIPE)
hli2 = hostlatin2.stdout.read()
hli2s = float(hli2[1:5])
print ('== Bandwidth from host 2 = ', hli2s)
# TODO: external latency test --> ping google

#hostname = subprocess.Popen(["sudo","sshpass", "-p", "fiveg4kmu", "ssh", "-o", "StrictHostKeyChecking=no", "pi@192.168.0.103", "cd", "/home/pi/Wiler", "&&", "awk","'NR>1{exit} {print $2}' lat.txt"], stdout=subprocess.PIPE)

#subprocess.Popen(["sudo","sshpass", "-p", "fiveg4kmu", "ssh", "-o", "StrictHostKeyChecking=no", "pi@192.168.0.103", "sudo", "tc", "qdisc", "delete", "dev", "wlan0", "root"])