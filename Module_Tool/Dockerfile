FROM python:latest
WORKDIR /usr/src/app
COPY /src . 
RUN apt-get update --no-install-recommends --yes && \
  apt-get upgrade --no-install-recommends --yes && \
  apt-get install python-scapy --no-install-recommends --yes && \
  apt-get install python-matplotlib --no-install-recommends --yes&& \
  apt-get install graphviz --no-install-recommends --yes && \
  pip install graphviz && \
  pip install scapy && \
  pip install matplotlib
ENTRYPOINT python programm.py

# RUN apt-get update --no-install-recommends --yes
# RUN apt-get upgrade --no-install-recommends --yes
# RUN apt-get install python-scapy --no-install-recommends --yes
# RUN apt-get install python-matplotlib --no-install-recommends --yes
# RUN apt-get install graphviz --no-install-recommends --yes
# RUN pip install graphviz 
# RUN pip install scapy 
# RUN pip install matplotlib 

# docker build -t moduletool_X .
# -p 172.17.192.1:5050:5050/tcp
# docker run -it -p 172.17.192.1:5050:5050/tcp --name moduletool_5 moduletool_4 bash
# docker run -it -p 172.17.192.1:5050:5050/tcp moduletool_4 bash


# docker start -i moduletool_X