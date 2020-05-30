

up: site
	rsync -av ../../web \
                  ../../index.html \
              krb70_trmaprod@ssh.phx.nearlyfreespeech.net:./

site:
	python build.py

test: site serve

serve:
	( cd ../../ ; python server.py )


