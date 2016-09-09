#!/bin/python

import os

# checks if the file is a src file by extension
def chkIfSrc(filename):
	extensions = [".c", ".cpp", ".cs", ".h", ".hpp", ".java"]
	for ext in extensions:
		if ext in filename:
			return True
	return False

# total TODOs found
total = 0

# go through all the files in the current dir
for filename in os.listdir(os.getcwd()):
	# open the file if it's a src file
	if chkIfSrc(filename):
		f = open(filename, "r")
		lineNum = 1
		print(filename + ":")

		# scan for TODOs
		for line in f:
			if "TODO" in line:
				print("  " + line, end="")
				total += 1
			lineNum += 1

		f.close()

# final output
print("\nTotal: " + str(total))
