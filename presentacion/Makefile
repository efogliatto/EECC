filename=presenta_enief2017

all:
	pdflatex ${filename}.tex

pdflatex:
	pdflatex ${filename}.tex

bibtex:
	bibtex ${filename}||true

read:
	evince ${filename}.pdf &

clean:
	rm -f *.aux *.bbl *.blg *.log *.nlo *.out *.ilg *.nls *.toc *.loc *.pdf *.soc *.nav *.snm *.vrb
