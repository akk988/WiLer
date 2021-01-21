#TODO:
  -Client und Server UDP müssen noch erstellt werden
  -Scapy-Tools müssen auf Funktionalität geschrieben werden
  -Andere Docker-Container müssen noch eingebunden werden für IRTT oder Ostinato
  -Exceptions müssen noch gecatched werden



----------------------------------------------------------------------------------
To ADD a new Network-Tool into NETWORK - MODULE - TOOL:

  - Of course the environment should be customized (in Docker + Working-Tree)
  - There are 4 steps in programm.py:
      # 1.) ^^Import above this a new tool^^
      # 2.) ^^Import above this a new tool^^
      # 3.) <-- increase this number to the number of available tools
      # 4.) ^^Import above this a new tool^^
    Search for them and add a new Tool.
----------------------------------------------------------------------------------

----------------------------------------------------------------------------------
Docker credentials
  # docker build -t moduletool_X .
  # -p 172.17.192.1:5050:5050/tcp
  # docker run -it -p 192.168.178.25:5050:5050/tcp --name moduletool_5 moduletool_4 bash
  # docker run -it -p 192.168.178.25:5050:5050/tcp moduletool_1 bash

  # docker start -i moduletool_X
----------------------------------------------------------------------------------

----------------------------------------------------------------------------------
Python Socket Tutorial
  https://www.youtube.com/watch?v=3QiPPX-KeSc&t=955s
----------------------------------------------------------------------------------

Installing Moduletool without Docker:
-Python3 is required
-pip3 install --pre scapy[basic]
-pip3 install -U matplotlib

run as sudo!!!!

