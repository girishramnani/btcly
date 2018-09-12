# btcly
Playground for btc dev

## Architecture

This project builds a 3 node bitcoin network on regtest network. There is a special bitcoin master commits blocks every 1s.

## How to Run

To run the network just `bash run.sh`. The RPC username ad password is `test`.

There are make commands to shell into all the node, to shell into bob or alice

```

cd dockerFiles/bitcoind

make bob_shell
#or
make alice_shell

```
similarly for `master` node

```

cd dockerFiles/bitcoind-master
make master_shell

```

