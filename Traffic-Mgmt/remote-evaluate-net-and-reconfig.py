## Requirements
# ssh, sshpass, iperf3, scapy
# Install sshpass on the controller node (cN) and create a file for passwords (sshpass -f) / or use directly (sshpass -p). If sshpass doesn't work: Then generate and copy ssh keys as follows
# SSH-Keygen: on controller node $ ssh-keygen copy to the node to be controlled: $ ssh-copy-id -i ~/.ssh/id_rsa.pub pi@192.168.0.101
#### sshpass

# This script does following: 
# 1. ssh to two worker nodes (wNs) and cd to the path, where scapy and iperf3 results must be saved.
# 2. run a first test for latency and bandwidth and save the results in lat1.txt and bw2.txt
# 3. calculate the new bandwidth (later also latency) for each wN
# 4. apply new qdisc config for each wN
# 5. run a second test to ensure the results

import subprocess

global cN_ip, wN1_ip, wN2_ip, wNpass, SHCK, wNpath
cN_ip = "192.168.0.104"
wN1_ip = "pi@192.168.0.103"
wN2_ip = "pi@192.168.0.101"
wNpass = "fiveg4kmu"
SHCK = "StrictHostKeyChecking=no"
wNpath = "/home/pi/Wiler"


#--------------------------------------------------------------------------------------------------------------------------------------------------------------#
def hostnames():
    print ('~~~~~~+ Methode hostnames starts +~~~~~~~')
    print ('==== Controller-Node starts . . . ====')
    print ('==== Scanning for worker nodes .. ====')
    hostname = subprocess.Popen(["sudo","sshpass", "-p", wNpass, "ssh", "-o", SHCK, wN1_ip, "sudo", "hostname"], stdout=subprocess.PIPE)
    hn = hostname.stdout.read()
    print ('== wN available:', hn)
    hostname = subprocess.Popen(["sudo","sshpass", "-p", wNpass, "ssh", "-o", SHCK, wN2_ip, "sudo", "hostname"], stdout=subprocess.PIPE)
    hn = hostname.stdout.read()
    print ('== wN available:', hn)
    # TODO: Change hostname on each wN
#--------------------------------------------------------------------------------------------------------------------------------------------------------------#

print ('===== Measureming Latency and Bandwidth from each wN ======')

def internal_latency():
    print ('~~~~~~+ Methode internal_latency starts +~~~~~~~')
    print ('== Internal Latency Test ==')
    # run scapy script on host 
    p = subprocess.Popen(["sudo","sshpass", "-p", wNpass, "ssh", "-o", SHCK, wN1_ip, "cd", wNpath, "&&", "sudo", "python", "scapyLatencyEther.py", ">", "lat-in-1.txt"],stdout=subprocess.PIPE)
    # TODO: find a better way to wait a Popen!
    p2 = p.stdout.read()
    hostlatin1 = subprocess.Popen(["sudo","sshpass", "-p", wNpass, "ssh", "-o", SHCK, wN1_ip, "cd", wNpath, "&&", "awk","'NR>1{exit} {print $2}' lat-in-1.txt"], stdout=subprocess.PIPE)
    hli1 = hostlatin1.stdout.read()
    hli1s = float(hli1[1:5])
    print ('== Internal Latency from host 1 = ', hli1s, " Sec.")

    p = subprocess.Popen(["sudo","sshpass", "-p", wNpass, "ssh", "-o", SHCK, wN2_ip, "cd", wNpath, "&&", "sudo", "python", "scapyLatencyEther.py", ">", "lat-in-2.txt"], stdout=subprocess.PIPE)
    p2 = p.stdout.read()
    hostlatin2 = subprocess.Popen(["sudo","sshpass", "-p", wNpass, "ssh", "-o", SHCK, wN2_ip, "cd", wNpath, "&&", "awk","'NR>1{exit} {print $2}' lat-in-2.txt"], stdout=subprocess.PIPE)
    hli2 = hostlatin2.stdout.read()
    hli2s = float(hli2[1:5])
    print ('== Internal Latency from host 2 = ', hli2s, " Sec.")
    

def external_latency():
    print ('~~~~~~+ Methode internal_latency starts +~~~~~~~')
    print ('== Internal Latency Test ==')
    # TODO: external latency test --> ping google
    # either ping google directly or prepare a script on each wN
    px = subprocess.Popen(["sudo","sshpass", "-p", wNpass, "ssh", "-o", SHCK, wN1_ip, "cd", wNpath, "&&", "sudo", "ping", "8.8.8.8", ">", "ex-lat-in-1.txt"],stdout=subprocess.PIPE)
    # TODO: find a better way to wait a Popen!
    px2 = px.stdout.read()
    hostxlatin1 = subprocess.Popen(["sudo","sshpass", "-p", wNpass, "ssh", "-o", SHCK, wN1_ip, "cd", wNpath, "&&", "awk","'NR>1{exit} {print $2}' ex-lat-in-1.txt"], stdout=subprocess.PIPE)
    hxli1 = hostxlatin1.stdout.read()
    hxli1s = float(hxli1[1:5])
    print ('== External Latency from host 1 = ', hxli1s, " Sec.")

    pxb = subprocess.Popen(["sudo","sshpass", "-p", wNpass, "ssh", "-o", SHCK, wN2_ip, "cd", wNpath, "&&", "sudo", "ping", "8.8.8.8", ">", "ex-lat-in-1.txt"],stdout=subprocess.PIPE)
    # TODO: find a better way to wait a Popen!
    pxb2 = pxb.stdout.read()
    hostbxlatin1 = subprocess.Popen(["sudo","sshpass", "-p", wNpass, "ssh", "-o", SHCK, wN2_ip, "cd", wNpath, "&&", "awk","'NR>1{exit} {print $2}' ex-lat-in-1.txt"], stdout=subprocess.PIPE)
    hbxli1 = hostbxlatin1.stdout.read()
    hbxli1s = float(hbxli1[1:5])
    print ('== External Latency from host 1 = ', hxli1s, " Sec.")
#--------------------------------------------------------------------------------------------------------------------------------------------------------------#

def bandwidth_wn_unlimited():
    print ('== Bandwidth Test ==')

    print ('== Starting iperf3 Server on cN ==')
    #try:
    #    iperf = subprocess.Popen(["iperf3", "-s"],stdout=subprocess.PIPE)
    #    iperfr = iperf.stdout.read()
    #    #break
    #except ValueError:
    #    print("iperf3 Server could be already running!")
    #p = subprocess.Popen(["sudo","sshpass", "-p", wNpass, "ssh", "-o", SHCK, "pi@192.168.0.104", "cd", "/home/akk/WiLer/Traffic-Mgmt", "&&", "./iperf3server.sh"],stdout=subprocess.PIPE)
    # TODO: find a better way to wait a Popen!
    #p2 = p.stdout.read()
    #hostlatin1 = subprocess.Popen(["sudo","sshpass", "-p", wNpass, "ssh", "-o", SHCK, wN1_ip, "cd", wNpath, "&&", "awk","'FNR == 8 {print $7}' bw-in-1-server.txt"], stdout=subprocess.PIPE)
    #hli1 = hostlatin1.stdout.read()
    #hli1s = float(hli1[1:5])
    #print ('== Internal Latency from host 1 = ', hli1s)

    #Delete old rules before measuring bandwidth
    # delete all qdisc roles
    
    qd = subprocess.Popen(["sudo","sshpass", "-p", wNpass, "ssh", "-o", SHCK, wN1_ip, "sudo", "tc", "qdisc", "delete", "dev", "wlan0", "root"], stdout=subprocess.PIPE)
    qdr = qd.stdout.read()
    # delete all qdisc roles
    qd = subprocess.Popen(["sudo","sshpass", "-p", wNpass, "ssh", "-o", SHCK, wN2_ip, "sudo", "tc", "qdisc", "delete", "dev", "wlan0", "root"], stdout=subprocess.PIPE)
    qdr = qd.stdout.read()
    #TODO: handle reading mbps or kbps !!!!!!!!

    print ('== Starting iperf3 Client on wN1 ==')
    pa = subprocess.Popen(["sudo","sshpass", "-p", wNpass, "ssh", "-o", SHCK, wN1_ip, "cd", wNpath, "&&", "sudo", "iperf3", "-c", cN_ip, "-i","1","-t","10",">", "bw-in-1-client.txt"], stdout=subprocess.PIPE)
    pa2 = pa.stdout.read()
    hostlatin1 = subprocess.Popen(["sudo","sshpass", "-p", wNpass, "ssh", "-o", SHCK, wN1_ip, "cd", wNpath, "&&", "awk","'FNR == 8 {print $7}' bw-in-1-client.txt"], stdout=subprocess.PIPE)
    hli1 = hostlatin1.stdout.read()
    global h1bw
    h1bw = float(hli1[0:4])
    print ('== Bandwidth from host 1 = ', h1bw, " Mbps")

    print ('== Starting iperf3 Client on wN2 ==')
    pb = subprocess.Popen(["sudo","sshpass", "-p", wNpass, "ssh", "-o", SHCK, wN2_ip, "cd", wNpath, "&&", "sudo", "iperf3", "-c", cN_ip, "-i","1","-t","10",">", "bw-in-2-client.txt"], stdout=subprocess.PIPE)
    pb2 = pb.stdout.read()
    hostlatin2 = subprocess.Popen(["sudo","sshpass", "-p", wNpass, "ssh", "-o", SHCK, wN2_ip, "cd", wNpath, "&&", "awk","'FNR == 8 {print $7}' bw-in-2-client.txt"], stdout=subprocess.PIPE)
    hli2 = hostlatin2.stdout.read()
    global h2bw
    h2bw = float(hli2[0:4])
    print ('== Bandwidth from host 2 = ', h2bw, " Mbps")
    # TODO: external latency test --> ping google

#--------------------------------------------------------------------------------------------------------------------------------------------------------------#

print ('== Bandwidth Configuration ==')

def calc_new_bandwidth():
    print ('== Calculatung the new network configs ==')
    medBW = (h1bw + h2bw)/2
    print ('== The middle Bandwidth is: ', medBW, " Mbps")
    # The incriment is important, to insure the limit does not decrease continuosly
    global BWL
    BWL = int((0.8 * medBW))#[0:3])
    print ('== The calculated large Bandwidth is: ', BWL, " Mbps")
    global BWM
    BWM = int((0.5 * medBW))#[0:3])
    print ('== The calculated medium Bandwidth is: ', BWM, " Mbps")
    global BWS
    BWS = int((0.3 * medBW))#[0:3])
    print ('== The calculated medium Bandwidth is: ', BWS, " Mbps")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------#
def reconfig_bw_limit():
    print ('== Reconfiguring bandwidth limit on wN1 ==')
    BWLstr = str(BWL)
    bwlimit1 = subprocess.Popen(["sudo","sshpass", "-p", wNpass, "ssh", "-o", SHCK, wN1_ip, "sudo", "tc", "qdisc", "add", "dev", "wlan0", "root", "tbf", "rate", "{}mbit".format(BWLstr), "burst", "32kbit", "latency", "200ms"], stdout=subprocess.PIPE)
    hli1 = bwlimit1.stdout.read()
    print ('== Bandwidth of host 1 setted to ', BWL, ' Mbps')
    BWSstr = str(BWS)
    bwlimit1 = subprocess.Popen(["sudo","sshpass", "-p", wNpass, "ssh", "-o", SHCK, wN2_ip, "sudo", "tc", "qdisc", "add", "dev", "wlan0", "root", "tbf", "rate", "{}mbit".format(BWSstr), "burst", "32kbit", "latency", "200ms"], stdout=subprocess.PIPE)
    hli1 = bwlimit1.stdout.read()
    print ('== Bandwidth of host 2 setted to ', BWS, ' Mbps')

#--------------------------------------------------------------------------------------------------------------------------------------------------------------#
def bandwidth_wn_limited():
    print ('== Bandwidth Test (limited) ==')

    #TODO: handle reading mbps or kbps !!!!!!!!

    print ('== Starting iperf3 Client on wN1 ==')
    pa = subprocess.Popen(["sudo","sshpass", "-p", wNpass, "ssh", "-o", SHCK, wN1_ip, "cd", wNpath, "&&", "sudo", "iperf3", "-c", cN_ip, "-i","1","-t","10",">", "bw-in-1-client.txt"], stdout=subprocess.PIPE)
    pa2 = pa.stdout.read()
    hostlatin1 = subprocess.Popen(["sudo","sshpass", "-p", wNpass, "ssh", "-o", SHCK, wN1_ip, "cd", wNpath, "&&", "awk","'FNR == 8 {print $7}' bw-in-1-client.txt"], stdout=subprocess.PIPE)
    hli1 = hostlatin1.stdout.read()
    global h1bw
    h1bw = float(hli1[0:4])
    print ('== Bandwidth from host 1 = ', h1bw, " Mbps")

    print ('== Starting iperf3 Client on wN2 ==')
    pb = subprocess.Popen(["sudo","sshpass", "-p", wNpass, "ssh", "-o", SHCK, wN2_ip, "cd", wNpath, "&&", "sudo", "iperf3", "-c", cN_ip, "-i","1","-t","10",">", "bw-in-2-client.txt"], stdout=subprocess.PIPE)
    pb2 = pb.stdout.read()
    hostlatin2 = subprocess.Popen(["sudo","sshpass", "-p", wNpass, "ssh", "-o", SHCK, wN2_ip, "cd", wNpath, "&&", "awk","'FNR == 8 {print $7}' bw-in-2-client.txt"], stdout=subprocess.PIPE)
    hli2 = hostlatin2.stdout.read()
    global h2bw
    h2bw = float(hli2[0:4])
    print ('== Bandwidth from host 2 = ', h2bw, " Mbps")


hostnames()
internal_latency()
external_latency()
bandwidth_wn_unlimited()
calc_new_bandwidth()
reconfig_bw_limit()
bandwidth_wn_limited()

#hostname = subprocess.Popen(["sudo","sshpass", "-p", wNpass, "ssh", "-o", SHCK, wN1_ip, "cd", wNpath, "&&", "awk","'NR>1{exit} {print $2}' lat.txt"], stdout=subprocess.PIPE)

#subprocess.Popen(["sudo","sshpass", "-p", wNpass, "ssh", "-o", SHCK, wN1_ip, "sudo", "tc", "qdisc", "delete", "dev", "wlan0", "root"])