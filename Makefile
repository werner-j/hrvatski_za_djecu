.PHONY: all clean view help

# Default target
all: main.pdf

# Compile the LaTeX document
main.pdf: main.tex chapters/*.tex resources/*.tex
	pdflatex main.tex
	pdflatex main.tex

# Clean auxiliary files
clean:
	rm -f *.aux *.log *.out *.toc *.lof *.lot *.fls *.fdb_latexmk
	rm -f *.synctex.gz *.bbl *.blg *.bcf *.run.xml
	rm -f chapters/*.aux resources/*.aux

# Clean everything including the PDF
cleanall: clean
	rm -f main.pdf

# View the PDF (requires a PDF viewer)
view: main.pdf
	@if command -v xdg-open > /dev/null; then \
		xdg-open main.pdf; \
	elif command -v open > /dev/null; then \
		open main.pdf; \
	elif command -v evince > /dev/null; then \
		evince main.pdf & \
	else \
		echo "No PDF viewer found. Please open main.pdf manually."; \
	fi

# Help target
help:
	@echo "Available targets:"
	@echo "  all (default) - Build the PDF"
	@echo "  clean        - Remove auxiliary files"
	@echo "  cleanall     - Remove auxiliary files and PDF"
	@echo "  view         - Open the PDF in a viewer"
	@echo "  help         - Show this help message"
