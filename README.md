# Sage to Python preparser experiment

Inspired by issues such as
https://github.com/sagemath/sage/issues/30760
and https://github.com/sagemath/sage/issues/30501
, this project explores the usage of
[tree-sitter](https://tree-sitter.github.io/tree-sitter/)
APIs to create a more structure-aware SageMath to Python translator.

## Benefits
- tree-sitter APIs have bindings for a few
  [languages](https://tree-sitter.github.io/tree-sitter/#language-bindings)
  allowing to easily translate this to an implementation which fits the
  SageMath build system or performance requirements
- Comes with a syntax highlighter *for free* to use with editors which support
  tree-sitter (mostly niche editors, noteably neovim, but maybe VSCode with
  plugin?)
- Leverages existing python tree-sitter grammar (which dealt with f-strings
  already, so they seem to work ootb, see [Demo])


## Usage
- Clone this repo along with subrepositories (`git clone --recursive ...`)
- Create/update a python environment to have the pip packages in `requirements.txt`
- Build the "sage" (work in progress) tree-sitter parser with `./build-parser.py`
- Run with `./sage2python.py <sage file>`, to have the generated python code
  printed to stdout

## Demo
The `input.sage` file is under version control to provide a default sage file
to try, which likely shows off the features that currently work or are being
worked on.

## Comparison
The equivalent way of doing this with SageMath is
`sage --preparse <sage file>`, useful for testing expected behaviour.
