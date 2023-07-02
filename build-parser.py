#!/usr/bin/env python

from tree_sitter import Language

Language.build_library(
  # Store the library in the `build` directory
  'build/sage.so',

  # Include one or more languages
  [ 'tree-sitter-sage/' ]
)
