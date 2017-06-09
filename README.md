# act

*Find TODO comments in source files.*

## Description

This Python script scans source files for `TODO` or `todo` tags and displays them. By default it will search only the current working directory, but will search recursively with `-r`.

Recognised source files: `.c`, `.cpp`, `.h`, `.hpp`, `.cs`, `.java`, `.py` and `.sh`.

## Usage

```
> act.py -r
main.cpp:
  10: // TODO command line arguments
  45: int x = -1; // TODO replace this with...

script.sh:
  29: # todo: handle error cases

util.c:
   7: /* TODO this could do with a re-write */
 101: /* TODO phase this function out? */

Total: 5
```
