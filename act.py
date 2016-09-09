#!/bin/python

import os

# checks if the file is a src file by extension
def chkIfSrc(filename):
	extensions = [".c", ".cpp", ".cs", ".h", ".hpp", "java"]
	for ext in extensions:
		if ext in filename:
			return True
	return False

# total TODOs found
total = 0

# go through all the files in the current dir
for filename in os.listdir(os.getcwd()):
	print(filename + ": " + str(chkIfSrc(filename)))

# final output
print("\nTotal: " + str(total))
