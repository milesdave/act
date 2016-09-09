# act

*Find TODO comments in source files.*

## Description

This Python script scans source files in the current directory for TODO tags and displays them.

Works with:
- C, C++, C# and Java source files,
- `todo` or `TODO` tags in single-line or multi-line comments.

Copy the script to somewhere in your `$PATH` to use anywhere.

## Usage

```
> act.py
main.cpp:
  10: "command line arguments"
  45: "replace this function with..."
main.hpp:
  29: "handle error cases"
util.cpp:
  7: "this could do with a re-write"
  101: "phase this function out?"

Total: 5
```
