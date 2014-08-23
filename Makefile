nup.pdf : guestlist.csv placecards.py Makefile
	./placecards.py guestlist.csv placecards.tex
	pdflatex placecards.tex
#	pdfnup --outfile nup.pdf --nup 2x3 --no-landscape --frame true --papersize '{8.5in,11in}' placecards.pdf
	pdfnup --outfile nup.pdf --nup 3x2 --frame true --papersize '{8.5in,11in}' placecards.pdf
