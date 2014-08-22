nup.pdf : guestlist.csv placecards.py
	./placecards.py guestlist.csv placecards.tex
	pdflatex placecards.tex
	pdfnup --outfile nup.pdf --nup 2x3 --no-landscape placecards.pdf
