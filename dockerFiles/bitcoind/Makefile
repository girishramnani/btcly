DOCKER_RUN=docker run -t
DOCKER_ALICE=$(DOCKER_RUN) -p 18444:18444 -p 18332:18332 --name=alice --hostname=alice
DOCKER_BOB  =$(DOCKER_RUN) -p 19444:18444 -p 19332:18332 --name=bob --hostname=bob

IMG=bitcoind:latest

RUN_DAEMON=bitcoind -regtest -rpcallowip=192.168.1.0/24 -printtoconsole
RUN_SHELL=bash

build:
	docker build -t $(IMG) .

alice_rm:
	docker rm -f  alice || true

bob_rm:
	docker rm -f  bob || true

alice_daemon: alice_rm
	$(DOCKER_ALICE) -d=true $(IMG) $(RUN_DAEMON)

alice_shell: alice_rm
	$(DOCKER_ALICE) -i $(IMG) $(RUN_SHELL)

bob_daemon: bob_rm
	$(DOCKER_BOB) -d=true $(IMG) $(RUN_DAEMON)

bob_shell: bob_rm
	$(DOCKER_BOB) -i $(IMG) $(RUN_SHELL)