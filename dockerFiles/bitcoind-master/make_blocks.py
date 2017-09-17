import os
import time 
import threading



def run():
    while True:
        time.sleep(1)
        os.system("bitcoin-cli -regtest generate 1")

        
t = threading.Thread(target=run)
t.start()
os.system("bitcoind -regtest -rpcallowip=172.17.0.0/16 -printtoconsole")
        