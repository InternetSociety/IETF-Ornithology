MEETING=125
TZ=Asia/Shanghai

SUBDIR_ELEMENTS = IETF IAB IRTF
SUBDIR_OBJECTS = $(shell find src -name "*.md")

all: book

book: book/pandoc/pdf/IETF-Ornithology.pdf


book/pandoc/pdf/IETF-Ornithology.pdf: ${SUBDIR_OBJECTS}
	( cd src ; ../CreateSummary.py > SUMMARY.md )  
	mdbook build

updateagenda:
	find src -name "*.md" -exec sed -i .bak 's/.*<IETFschedule.*>.*<\/IETFschedule>/<IETFschedule meets=false><\/IETFschedule>/' {} \;
	find src/IETF   -name "*.md"  -exec  ./AgendaUpdate.py ${MEETING} ${TZ} {} \;
	find src/IAB   -name "*.md"  -exec  ./AgendaUpdate.py ${MEETING} ${TZ} {} \;
	find src/IRTF   -name "*.md"  -exec  ./AgendaUpdate.py ${MEETING} ${TZ} {} \;

bofs:
	./ApprovedBOFs.py ${MEETING} 

clean:
	rm -Rf book

disclean: 
	rm -Rf book
	rm src/SUMMARY.md
	`find src -name "*.md" -exec sed -i .bak 's/.*<IETFschedule.*>.*<\/IETFschedule>/<IETFschedule meets=false><\/IETFschedule>/' {} \;`


clear:
	find src -name "*.md" -exec sed -i .bak 's/.*<IETFschedule.*>.*<\/IETFschedule>/<IETFschedule meets=false><\/IETFschedule>/' {} \;

summary:
	(cd src ; ../CreateSummary.py > SUMMARY.md )