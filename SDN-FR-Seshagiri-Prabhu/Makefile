TEX = pdflatex -interaction nonstopmode
BIB = bibtex
GS = gs -q -dNOPAUSE -dBATCH -sDEVICE=pdfwrite 
 
PAPER = llncs
BIBFILE = temp.bib
BUNDLE = paper_bundle.pdf
 
all: $(COVER).pdf $(PAPER).pdf $(SUPP).pdf 
	$(GS) -sOutputFile=$(BUNDLE) $(COVER) $(PAPER).pdf
 
view: $(BUNDLE)
	open $(BUNDLE)
 
spell::
	ispell *.tex
 
clean::
	rm -fv *.out *.aux *.dvi *.ps *.toc *.lof *.log *.lot *.flg *.bbl *.blg *.idx *.ind *.ilg *.snm *.nav *.fig.bak *.vrb *.synctex.gz *.fdb_latexmk $(BUNDLE)
 
$(PAPER).pdf: $(PAPER).tex $(PAPER).bbl 
	$(TEX) $(PAPER) 
	$(TEX) $(PAPER)
 
$(PAPER).bbl: $(PAPER).tex $(BIBFILE)
	$(TEX) $(PAPER)
	$(BIB) $(PAPER)
 
$(SUPP).pdf: $(SUPP).tex $(SUPP).bbl 
	$(TEX) $(SUPP) 
	$(TEX) $(SUPP)
 
$(SUPP).bbl: $(SUPP).tex $(BIBFILE)
	$(TEX) $(SUPP)
	$(BIB) $(SUPP)
