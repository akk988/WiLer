FROM golang:1.15.4
WORKDIR /usr/src/app
# COPY /src . 
RUN apt-get update && \
  apt-get upgrade --no-install-recommends --yes && \
  apt-get install python3 --no-install-recommends --yes && \
  apt-get install python2.7 --no-install-recommends --yes && \
  apt-get install python-pip --no-install-recommends --yes && \
  apt-get install python-scapy --no-install-recommends --yes && \
  apt-get install python-matplotlib --no-install-recommends --yes && \
  apt-get install graphviz --no-install-recommends --yes && \
  pip install graphviz && \
  pip install scapy && \
  pip install matplotlib
RUN go get -u github.com/heistp/irtt/cmd/irtt
# ENTRYPOINT python programm.py
