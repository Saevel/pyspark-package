dev-setup: virtualenv activate-venv dev-install

clean: clean-libs clean-venv

package: install zip


virtualenv: install-venv create-venv

install-venv:
	pip3 install virtualenv

create-venv:
	virtualenv venv

activate-venv:
	chmod 777 venv/bin/activate && source venv/bin/activate

dev-install:
	./venv/bin/pip install -Iv -r dev-requirements.txt && ./venv/bin/pip install -Iv -r requirements.txt

install:
	pip3 install -r requirements.txt -t libs

zip:
	zip libs.zip libs

clean-libs:
	rm -rf libs

clean-venv:
	rm -rf venv

