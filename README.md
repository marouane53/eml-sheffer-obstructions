# From fixed points to two-cycles: obstructions and orbit lifts for analytic self-seeding Sheffer operators

Repository for the manuscript bundle by Marouane Lamharzi Alaoui on
self-seeding Sheffer operators, analytic orbit lifts, and the EML
construction.

GitHub repository: <https://github.com/marouane53/eml-sheffer-obstructions>

## Main Manuscript

The canonical paper in this repository is the revised manuscript in
[`paper/`](paper/). It extends the earlier obstruction note and now includes:

- the diagonal ideal obstruction for constant-diagonal analytic germs
- the Hardy-field obstruction for purely real logarithmico-exponential
  primitives
- fixed-point lift constructions that recover prescribed unary germs
- disconnected finite-orbit and diagonal two-cycle lift results
- one-slice, two-slice, and four-slice interpolation theorems
- an explicit numerically verified complex exponential 2-cycle
- a branch-correct appendix for the core EML identities

## Repository Layout

- [`paper/self_seeding_sheffer_paper.pdf`](paper/self_seeding_sheffer_paper.pdf)
  - compiled PDF of the current main manuscript
- [`paper/self_seeding_sheffer_paper.tex`](paper/self_seeding_sheffer_paper.tex)
  - LaTeX source for the current main manuscript
- [`paper/references.bib`](paper/references.bib)
  - bibliography for the current main manuscript
- [`paper/verify_two_cycle.py`](paper/verify_two_cycle.py)
  - numerical verification script for the explicit exponential 2-cycle from
    Section 6
- [`paper_obstructions_note/obstructions_sheffer.pdf`](paper_obstructions_note/obstructions_sheffer.pdf)
  - compiled PDF of the earlier shorter obstruction note
- [`paper_obstructions_note/obstructions_sheffer.tex`](paper_obstructions_note/obstructions_sheffer.tex)
  - LaTeX source for the earlier shorter obstruction note

## Build

Build the current main manuscript from the repository root with:

```sh
cd paper
pdflatex -interaction=nonstopmode self_seeding_sheffer_paper.tex
bibtexu self_seeding_sheffer_paper
pdflatex -interaction=nonstopmode self_seeding_sheffer_paper.tex
pdflatex -interaction=nonstopmode self_seeding_sheffer_paper.tex
```

Build the earlier note with:

```sh
cd paper_obstructions_note
pdflatex obstructions_sheffer.tex
pdflatex obstructions_sheffer.tex
```

## Verification

The revised manuscript includes a numerical verification script that uses
`mpmath` with 80-digit precision to refine the explicit exponential 2-cycle,
check the logarithm branches, and verify the residual identities used in the
computational subsection.

Run it with:

```sh
python3 paper/verify_two_cycle.py
```

## Author

Marouane Lamharzi Alaoui  
Firassa AI  
marouane@firassa.ai

## License

The manuscript sources and compiled PDFs in this repository are licensed under
the Creative Commons Attribution 4.0 International License. See
[LICENSE](LICENSE) for the repository notice and canonical license link.
