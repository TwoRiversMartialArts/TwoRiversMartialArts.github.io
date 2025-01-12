
# UPLOAD=ssh.phx.nearlyfreespeech.net
UPLOAD=ssh.nyc1.nearlyfreespeech.net

up: site
	rsync -av ../../web \
                  ../../*.html \
              krb70_trmaprod@$(UPLOAD):./

site:
	/usr/bin/python build.py

gh: site
	git commit -a --amend -m "update"
	git push -f origin master

test: site serve

serve:
	( cd ../../ ; python server.py )


