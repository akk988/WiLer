#TODO integrate this tool in the Module-Tool

## Requirements
# enable/install: ssh, sshpass, iperf3, on both client and server hosts 
# Run iperf3 manually on the server: $iperf3 -s OR uncomment the line of starting it remotly

import subprocess

global server_ip, client_ip, path, wNpass
server_ip = "192.168.0.10x"
client_ip = "192.168.0.10y"
wNpass = "remote-host-password"
wN1_ip = "/home/pi/myFolder

iperf3_client:

    # Uncomment to start the iperf3 server on remote host with IP= server_ip 
    #bws = subprocess.Popen(["sudo","sshpass", "-p", wNpass, "ssh", "-o", SHCK, server_ip, "&&", "sudo", "iperf3", "-s"], stdout=subprocess.PIPE)
   
    print ('== Starting iperf3 Client on localhost  ==')
    bw = subprocess.Popen(["sudo", "iperf3", "-c", server_ip, "-i","1","-t","10",">", "bandwidth-client.txt"], stdout=subprocess.PIPE)
    bw = pa.stdout.read()

    # Uncomment to start the iperf client on remote host with IP= client_ip 
    #bw = subprocess.Popen(["sudo","sshpass", "-p", wNpass, "ssh", "-o", SHCK, client_ip, "cd", wNpath, "&&", "sudo", "iperf3", "-c", server_ip, "-i","1","-t","10",">", "bw-in-1-client.txt"], stdout=subprocess.PIPE)
    

    hostbw = subprocess.Popen(["cd", wNpath, "&&", "awk","'FNR == 8 {print $7}' bw-in-1-client.txt"], stdout=subprocess.PIPE)
    
    #uncomment to read the results from remote host
    #hostbw = subprocess.Popen(["sudo","sshpass", "-p", wNpass, "ssh", "-o", SHCK, client_ip, "cd", wNpath, "&&", "awk","'FNR == 8 {print $7}' bw-in-1-client.txt"], stdout=subprocess.PIPE)

    hli1 = hostbw.stdout.read()
    
    #global h1bw
    h1bw = float(hli1[0:4])
    print ('== Bandwidth from host 1 = ', h1bw, " Mbps")