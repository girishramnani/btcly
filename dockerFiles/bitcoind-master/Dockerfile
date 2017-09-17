FROM ubuntu:16.04

RUN apt-get -y update
RUN apt-get install -y python-software-properties 
RUN apt-get install -y software-properties-common

RUN add-apt-repository ppa:bitcoin/bitcoin
RUN apt-get update
RUN apt-get install -y bitcoind

RUN mkdir ~/.bitcoin
RUN echo "rpcuser=test\nrpcpassword=test\n" > ~/.bitcoin/bitcoin.conf
ADD make_blocks.py /home/make_blocks.py
RUN echo "alias rt='bitcoin-cli -regtest'" >> ~/.bashrc

CMD ["python","/home/make_blocks.py"]

