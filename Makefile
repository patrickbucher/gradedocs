PDF_PARAMS=-s --pdf-engine=xelatex -V lang=de -V fontsize=12pt -V papersize=a4 -V documentclass=scrartcl
FONT_PARAMS=-V mainfont="Vollkorn" -V sansfont="Lato" -V monofont="Fira Code"

.SUFFIXES: .md .pdf
.md.pdf:
	pandoc $(PDF_PARAMS) $(FONT_PARAMS) $< -o $@