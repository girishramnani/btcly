import os
import time 
import threading



def run():
    while True:
        time.sleep(1)
        os.system("bitcoin-cli -regtest generate 1")

        
t = threading.Thread(target=run)
t.start()
os.system("bitcoind -regtest -printtoconsole")
        