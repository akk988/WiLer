# Run the script with Python3

# Install sshpass on the controller node

# Create a file for passwords (sshpass -f) / or use directly (sshpass -p) 

# If sshpass doesn't work: Then generate and compy ssh keys as follows

# on controller node $ ssh-keygen

# copy to the node to be controlled: $ ssh-copy-id -i ~/.ssh/id_rsa.pub pi@192.168.0.101



# This may be caused by the host-key checks done by ssh. It looks like sshpass keeps silent on invalid host keys (no output on neither stderr nor stdout) and exists with status-code 6. At the time of this writing, this was revision 50, and the matching constant in the code is RETURN_HOST_KEY_UNKNOWN, which hints to that error.



#### sshpass

## The Problem with sshpass: https://askubuntu.com/questions/282319/how-to-use-sshpass --> -o StrictHostKeyChecking=no

##Your error-code may differ and looking at the code linked above may give you some insight.

##If your issue is an invalid host-key you should think twice about overriding the error with a CLI option. Your machine could be compromised or you may be subject to a MITM attack! If you are 100% certain that this is not the case and if you have no means to keep the verified host-keys up-to date, you can use a command like this:



import subprocess



print ('# scapy Latency Remote Tester #')

print ('# python script is prepared on the remote nodes for measuring the latency with scapy #')



# read latency of Node-01



print ('Running the python script on Node 01 ')

print ('Time is:  ')

#result1 = subprocess.check_output('sshpass -p "fiveg4kmu" ssh -o StrictHostKeyChecking=no pi@192.168.0.103 "cd /home/pi/Wiler && sudo python scapyLatencyEther.py > rem-lat-scap-nw-nt-rpi1.txt"', shell=True)

# Using shlex.split --> ['sshpass', '-p', 'fiveg4kmu', 'ssh', '-o', 'StrictHostKeyChecking=no', 'pi@192.168.0.103', 'cd /home/pi/Wiler && sudo python scapyLatencyEther.py > rem-lat-scap-nw-nt-rpi1.txt']

# subprocess.run(['sshpass', '-p', 'fiveg4kmu', 'ssh', '-o', 'StrictHostKeyChecking=no', 'pi@192.168.0.103', 'cd /home/pi/Wiler && sudo python scapyLatencyEther.py > rem-lat-scap-nw-nt-rpi1.txt'], check=False)

# Using subprocess.Popen BECAUSE --> By default, subprocess.Popen does not stop processing of a Python program if its command has not finished executing. 

subprocess.Popen(["sudo","sshpass", "-p", "fiveg4kmu", "ssh", "-o", "StrictHostKeyChecking=no", "pi@192.168.0.103", "cd /home/pi/Wiler && sudo python scapyLatencyEther.py > rem-lat-scap-nw-nt-rpi1.txt"])



print ('Running the python script on Node 02 ')

print ('Time is:  ')

#result2 = subprocess.check_output('sshpass -p "fiveg4kmu" ssh -o StrictHostKeyChecking=no pi@192.168.0.101 "cd /home/pi/prio-TC-Tests && sudo python scapyLatencyEther.py > rem-lat-scap-nw-nt-rpi3.txt"', shell=True)

subprocess.Popen(["sudo","sshpass", "-p", "fiveg4kmu", "ssh", "-o", "StrictHostKeyChecking=no", "pi@192.168.0.101", "cd /home/pi/prio-TC-Tests && sudo python scapyLatencyEther.py > rem-lat-scap-nw-nt-rpi3.txt"])



print ('Running the python script on Node 03 ')

print ('Time is:  ')

#result3 = subprocess.check_output('sshpass -p "fiveg4kmu" ssh -o StrictHostKeyChecking=no pi@192.168.0.100 "cd /home/pi/WiLer/scapy && sudo python scapyLatencyEther.py > rem-lat-scap-nw-nt-rpi4.txt"', shell=True)

#subprocess.run('sshpass -p "fiveg4kmu" ssh -o StrictHostKeyChecking=no pi@192.168.0.100 "cd /home/pi/WiLer/scapy && sudo python scapyLatencyEther.py > rem-lat-scap-nw-nt-rpi4.txt"', shell=True, check=True)

subprocess.Popen(["sudo","sshpass", "-p", "fiveg4kmu", "ssh", "-o", "StrictHostKeyChecking=no", "pi@192.168.0.100", "cd /home/pi/WiLer/scapy && sudo python scapyLatencyEther.py > rem-lat-scap-nw-nt-rpi4.txt"])



#print (result1)

#print (result2)

#print (result3)



print ('The latency test is done!')
