# Obstructions to Self-Seeding Sheffer Operators for Calculator-Style Elementary Functions

Repository for the manuscript and compiled PDF of the note by Marouane Lamharzi Alaoui.

GitHub repository: <https://github.com/marouane53/eml-sheffer-obstructions>

## Overview

This repository contains a short research note responding to open problems from
Andrzej Odrzywolek's "All elementary functions from a single operator"
([arXiv:2603.21852v2](https://arxiv.org/abs/2603.21852)).

The paper studies whether Odrzywolek's `eml(x, y) = e^x - log(y)` construction
admits a single self-seeding binary primitive and whether a purely real tame
analog could generate the same calculator-style basis of elementary functions.

## Main Results

- Diagonal ideal obstruction: an analytic binary germ with constant diagonal
  `f(x, x) = c` generates only term germs that fix `c`, so the one-step
  constant-diagonal self-seeding strategy cannot work.
- Hardy-field obstruction: a purely real logarithmico-exponential primitive
  generates unary tail-germs that are eventually monotone, so periodic targets
  such as `sin` and `cos` cannot appear.
- Branch-correct EML clarification: under a lower-edge logarithm convention,
  the reconstructed logarithm matches the principal logarithm and the `log(-1)`
  sign comes out correctly.
- Off-diagonal fiber criterion: any multi-step constant unary term must force
  an off-diagonal analytic curve in a level set of the primitive, isolating the
  remaining geometric search space for tame self-seeding constructions.

## Repository Layout

- [paper/obstructions_sheffer.pdf](paper/obstructions_sheffer.pdf) - compiled
  manuscript
- [paper/obstructions_sheffer.tex](paper/obstructions_sheffer.tex) - LaTeX
  source with embedded bibliography

## Build

From the repository root:

```sh
cd paper
pdflatex obstructions_sheffer.tex
pdflatex obstructions_sheffer.tex
```

No BibTeX step is required because the bibliography is included directly in the
source file.

## Author

Marouane Lamharzi Alaoui  
Firassa AI  
marouane@firassa.ai

## License

The manuscript source and compiled paper in this repository are licensed under
the Creative Commons Attribution 4.0 International License. See
[LICENSE](LICENSE) for the repository notice and canonical license link.

If standalone software is added later, it is usually better to license that
code separately under a software license such as MIT or Apache-2.0.
