.PHONY: all clean

all:
	docker build -t netxms-libexosip-rpm-builder docker
	docker run --cap-add=SYS_ADMIN -it --rm -v ${PWD}/cache:/var/cache/mock -v ${PWD}:/build -v ${PWD}/result:/result netxms-libexosip-rpm-builder
	docker image rm netxms-libexosip-rpm-builder

clean:
	rm -f result/*
	docker image rm netxms-libexosip-rpm-builder || true
