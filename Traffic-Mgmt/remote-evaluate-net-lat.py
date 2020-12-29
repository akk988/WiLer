import subprocess
import time
from datetime import datetime
print("current time = ", datetime.now().time())
res = subprocess.Popen(["sudo","sshpass", "-p", "fiveg4kmu", "ssh", "-o", "StrictHostKeyChecking=no", "pi@192.168.0.103", "cd", "/home/pi/Wiler", "&&", "awk","'NR>1{exit} {print $2}' rem-lat-scap-nw-TC-rpi1.txt"], stdout=subprocess.PIPE)
res2 = res.stdout.read()

resn = float(res2[1:5])
print ("results to float: ", resn)

if resn < 0.022:
  print("== Latency Level: Low Latency ==")
elif resn < 0.09:
  print("== Latency Level: Med Latency ==")
else:
  print("== Latency Level: High Latency ==")


#o4 = (float(o3)/2)
#print ("the half of it",o4)
#print ("low latency")
#print ("end of reading")
