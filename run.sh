cd dockerFiles/bitcoind-master
# start the master node
make build
make master_maker

cd ../bitcoind
# start bob and alice nodes
make build
make alice_daemon
make bob_daemon
