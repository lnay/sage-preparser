# Sage to Python preparser experiment

Inspired by issues such as
https://github.com/sagemath/sage/issues/30760
and https://github.com/sagemath/sage/issues/30501
, this project explores the usage of
[tree-sitter](https://tree-sitter.github.io/tree-sitter/)
APIs to create a more structure-aware SageMath to Python translator with the
benefit of also getting a syntax highlighter for editors which support
tree-sitter.


## Demo:
- Clone this repo along with subrepositories (`git clone --recursive ...`)
- Build the "sage" (work in progress) tree-sitter parser with `./build-parser.py`
- Run with `./sage2python.py <sage file>`, to have the generated python code
  printed to stdout

The `input.sage` file is under version control to provide a default sage file
to try, which likely shows off the features that currently work or are being
worked on.
