MEETING=127
TZ=America/Los_Angeles

SUBDIR_ELEMENTS = IETF IAB IRTF
SUBDIR_OBJECTS = $(shell find src -name "*.md")

all: book 

book: book/pandoc/pdf/IETF-Ornithology.pdf


book/pandoc/pdf/IETF-Ornithology.pdf: ${SUBDIR_OBJECTS} src/Appendix/agenda.md 
	( cd src ; ../CreateSummary.py > SUMMARY.md )  
	mdbook build

updateagenda:
	find src -name "*.md" -exec sed -i .bak 's/.*<IETFschedule.*>.*<\/IETFschedule>/<IETFschedule meets=false><\/IETFschedule>/' {}   \; | tee groupsmeeting.txt
	find src/IETF   -name "*.md"  -exec  ./AgendaUpdate.py ${MEETING} ${TZ} {}  \; | tee -a groupsmeeting.txt
	find src/IAB   -name "*.md"  -exec  ./AgendaUpdate.py ${MEETING} ${TZ} {}  \; | tee -a groupsmeeting.txt
	find src/IRTF   -name "*.md"  -exec  ./AgendaUpdate.py ${MEETING} ${TZ} {}  \; | tee -a groupsmeeting.txt	
	python ./create_agendaURL.py ${MEETING}  groupsmeeting.txt  > src/Appendix/agenda.md
	rm groupsmeeting.txt
	touch updateagenda


archiveagenda:
	find src/archive -name "*.md" -exec sed -i .bak 's/.*<IETFschedule.*>.*<\/IETFschedule>/<IETFschedule meets=false><\/IETFschedule>/' {}   \; | tee archivemeeting.txt
	find src/archive/IETF   -name "*.md"  -exec  ./AgendaUpdate.py ${MEETING} ${TZ} {}  \; | tee -a archivemeeting.txt
	find src/archive/IAB   -name "*.md"  -exec  ./AgendaUpdate.py ${MEETING} ${TZ} {}  \; | tee -a archivemeeting.txt
	find archive/IRTF   -name "*.md"  -exec  ./AgendaUpdate.py ${MEETING} ${TZ} {}  \; | tee -a archivemeeting.txt
	touch archiveagenda


src/Appendix/agenda.md: updateagenda

bofs:
	./ApprovedBOFs.py ${MEETING} 
	
clean:
	rm -Rf book updateagenda src/Appendix/agenda.md archiveagenda archivemeeting.txt

distclean: 
	rm -Rf book
	rm src/SUMMARY.md
	`find src -name "*.md" -exec sed -i .bak 's/.*<IETFschedule.*>.*<\/IETFschedule>/<IETFschedule meets=false><\/IETFschedule>/' {} \;`


clear:
	find src -name "*.md" -exec sed -i .bak 's/.*<IETFschedule.*>.*<\/IETFschedule>/<IETFschedule meets=false><\/IETFschedule>/' {} \;

summary:
	(cd src ; ../CreateSummary.py > SUMMARY.md )