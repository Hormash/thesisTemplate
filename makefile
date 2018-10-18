TEX=latex
ARCHIVO=main

default: all

generardvi:
	$(TEX) $(ARCHIVO).tex
	@echo "\n\n#####GENERANDO BIBLIOGRAFIA#######"
	bibtex $(ARCHIVO).aux
	$(TEX) $(ARCHIVO).tex
	@echo "\n\n#####GENERANDO ARCHIVO FINAL#######"
	$(TEX) $(ARCHIVO).tex

clear:
	@echo "\n\n#####LIMPIANDO ARCHIVOS TEMPORALES#######"
	find . -name "*.aux" -type f -delete
	find . -name "*.log" -type f -delete
	find . -name "*.out" -type f -delete
	find . -name "*.bbl" -type f -delete
	find . -name "*.blg" -type f -delete
	find . -name "*.blg" -type f -delete
	find . -name "*.idx" -type f -delete
	find . -name "*.toc" -type f -delete
	rm $(ARCHIVO).dvi

topdf:
	@echo "\n\n#####GENERANDO PDF#######"
	dvipdfm $(ARCHIVO).dvi

transformaImagenes:
	@echo "\n\n#####TRANSFORMANDO IMAGENES#####"
	cd original_images; python convert.py

all: transformaImagenes generardvi topdf clear
