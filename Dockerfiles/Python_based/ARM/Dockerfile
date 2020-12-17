# For AMD64 

FROM python:latest
WORKDIR /usr/src/app
# COPY /src . 
RUN apt-get update --no-install-recommends --yes && \
  apt-get upgrade --no-install-recommends --yes && \
  apt-get install python-scapy --no-install-recommends --yes && \
  apt-get install python-matplotlib --no-install-recommends --yes && \
  apt-get install graphviz --no-install-recommends --yes && \
  pip install graphviz && \
  pip install scapy && \
  pip install matplotlib
RUN apt-get install wget && apt-get install git && \
  wget https://golang.org/dl/go1.15.6.linux-armv6l.tar.gz && \
  tar -C /usr/local -xzf go1.15.6.linux-armv6l.tar.gz && \
  export PATH=$PATH:/usr/local/go/bin && \
  GOPATH=/tmp go get -u github.com/heistp/irtt/cmd/irtt && \
  cp /tmp/bin/irtt /usr/local/go/bin
ENV PATH="$PATH:/usr/local/go/bin"
# ENTRYPOINT python programm.py
