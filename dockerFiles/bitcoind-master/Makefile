DOCKER_RUN=docker run -t
DOCKER_MASTER=$(DOCKER_RUN) -p 20444:18444 -p 20332:18332 --name=btc-master --hostname=master

IMG=bitcoind-master:latest

RUN_MAKER=python /home/make_blocks.py
RUN_SHELL=bash
build:
	docker build -t $(IMG) .

master_rm:
	docker rm -f  btc-master || true

master_maker: master_rm
	$(DOCKER_MASTER) -d=true $(IMG) 

master_shell: master_rm
	$(DOCKER_MASTER) -i $(IMG) $(RUN_SHELL)
