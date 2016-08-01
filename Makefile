
WD=web
LOC=location

locpages= $(WD)/$(LOC)-wdm.html \
      $(WD)/$(LOC)-hub.html \
      $(WD)/$(LOC)-carlisle.html \
      $(WD)/$(LOC)-bethany.html \
      $(WD)/$(LOC)-indianola.html \
      $(WD)/$(LOC)-pleasanthill.html \
      $(WD)/$(LOC)-stjoseph.html \
      $(WD)/$(LOC)-trenton.html \
      $(WD)/$(LOC)-lamoni.html \
      $(WD)/$(LOC)-winterset.html \


default : $(locpages)

$(WD)/$(LOC)-wdm.html : $(WD)/$(LOC)-x.html $(WD)/wdm.spec
	./process.py $(WD)/wdm.spec  $<  $@

$(WD)/$(LOC)-hub.html : $(WD)/$(LOC)-x.html $(WD)/hub.spec
	./process.py $(WD)/hub.spec  $<  $@

$(WD)/$(LOC)-carlisle.html : $(WD)/$(LOC)-x.html $(WD)/carlisle.spec
	./process.py $(WD)/carlisle.spec  $< $@

$(WD)/$(LOC)-bethany.html : $(WD)/$(LOC)-x.html $(WD)/bethany.spec
	./process.py $(WD)/bethany.spec  $< $@

$(WD)/$(LOC)-indianola.html : $(WD)/$(LOC)-x.html $(WD)/indianola.spec
	./process.py $(WD)/indianola.spec  $< $@

$(WD)/$(LOC)-lamoni.html : $(WD)/$(LOC)-x.html $(WD)/lamoni.spec
	./process.py $(WD)/lamoni.spec  $< $@

$(WD)/$(LOC)-pleasanthill.html : $(WD)/$(LOC)-x.html $(WD)/pleasanthill.spec
	./process.py $(WD)/pleasanthill.spec $< $@

$(WD)/$(LOC)-stjoseph.html : $(WD)/$(LOC)-x.html $(WD)/stjoseph.spec
	./process.py $(WD)/stjoseph.spec $<  $@

$(WD)/$(LOC)-trenton.html : $(WD)/$(LOC)-x.html $(WD)/trenton.spec
	./process.py $(WD)/trenton.spec $< $@

$(WD)/$(LOC)-winterset.html : $(WD)/$(LOC)-x.html $(WD)/winterset.spec
	./process.py $(WD)/winterset.spec $< $@

