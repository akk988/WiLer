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
# wget https://golang.org/dl/go1.15.6.linux-armv6l.tar.gz -o golang.tar.gz
# tar -C /usr/local -xzf golang.tar.gz
# tar -C /usr/local -xzf go1.15.6.linux-armv6l.tar.gz
# tar -C /usr/local -xzf go1.15.6.linux-amd64.tar.gz
# export PATH=$PATH:/usr/local/go/bin


# apt-get install wget && apt-get install git
# wget https://golang.org/dl/go1.15.6.linux-amd64.tar.gz
# tar -C /usr/local -xzf go1.15.6.linux-amd64.tar.gz
# export PATH=$PATH:/usr/local/go/bin
# go get -u github.com/heistp/irtt/cmd/irtt

# go version