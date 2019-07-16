all: quntoken/
.PHONY: all


quntoken/: quntoken.tar.gz
	@echo 'Unpacking quntoken...'
	@tar -xzf $^
	@rm -f $^
	@mv $@/lib/* $@
	@rm -r $@/bin $@/lib
	@touch $@/__init__.py
	@echo -e 'Done.\n'


quntoken.tar.gz:
	@echo 'Download quntoken...'
	@wget -q https://github.com/DavidNemeskey/quntoken/releases/download/v1.2.1/quntoken_Linux_x86_64_v1.2.1.tar.gz -O $@
	@echo -e 'Done.\n'


clean:
	@rm -rf quntoken/
	@rm -rf __pycache__/
.PHONY: clean
