

up: site
	rsync -av ../../web \
                  ../../*.html \
              krb70_trmaprod@ssh.phx.nearlyfreespeech.net:./

site:
	python build.py

gh: site
	git commit -a --amend -m "update"
	git push -f origin master

test: site serve

serve:
	( cd ../../ ; python server.py )


