Self-Seeding Sheffer Paper
==========================

Files
-----
- self_seeding_sheffer_paper.tex
- references.bib
- self_seeding_sheffer_paper.pdf
- verify_two_cycle.py

Compilation
-----------
Run the following commands in this directory:

  pdflatex -interaction=nonstopmode self_seeding_sheffer_paper.tex
  bibtexu self_seeding_sheffer_paper
  pdflatex -interaction=nonstopmode self_seeding_sheffer_paper.tex
  pdflatex -interaction=nonstopmode self_seeding_sheffer_paper.tex

The final PDF will be written to:

  self_seeding_sheffer_paper.pdf

Numerical verification
----------------------
The script

  verify_two_cycle.py

uses mpmath with 80-digit arithmetic to refine the explicit exponential
2-cycle from Section 6, check the logarithm branches, construct the
corresponding two-slice interpolation germ, and print the residuals of
all identities used in the computational subsection.

Run it with:

  ./verify_two_cycle.py

or

  python3 verify_two_cycle.py
