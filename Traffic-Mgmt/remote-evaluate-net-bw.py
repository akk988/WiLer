import subprocess
import time
from datetime import datetime
print("current time = ", datetime.now().time())
res = subprocess.Popen(["sudo","sshpass", "-p", "fiveg4kmu", "ssh", "-o", "StrictHostKeyChecking=no", "pi@192.168.0.103", "cd", "/home/pi/Wiler","&&", "awk","'FNR == 8 {print $7}' bw.txt"], stdout=subprocess.PIPE)
res2 = res.stdout.read()
print ("read results: ", res2)
resn = float(res2[0:4])
print ("results to float: ", resn)

if resn < 1:
  print("== Bandwidth Level: Low BW ==")
elif resn < 2:
  print("== Bandwidth Level: Med BW ==")
else:
  print("== Bandwidth Level: High BW ==")

