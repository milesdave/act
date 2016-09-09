#!/bin/python

import os

# checks if the file is a src file by extension
def chkIfSrc(filename):
	extensions = [".c", ".cpp", ".cs", ".h", ".hpp", ".java"]
	for ext in extensions:
		if ext in filename:
			return True
	return False

# formats a line with a TODO in it
def formatter(lineNum, line):
	line = line.replace("//", "")
	line = line.replace("TODO", "")
	line = line.strip()
	return str(lineNum) + ": \"" + line + "\""

# scans a file for TODOs and prints them
def scanFile(f):
	total = 0
	lineNum = 1
	todoList = []

	# check each line for a TODO
	for line in f:
		if "TODO" in line:
			todoList.append(formatter(lineNum, line))
			total += 1
		lineNum += 1

	# print todoList
	if todoList:
		print(f.name + ":")
		for todo in todoList:
			print("  " + todo)

	return total

# total TODOs found
total = 0

# go through all the files in the current dir
for filename in os.listdir(os.getcwd()):
	# open the file if it's a src file
	if chkIfSrc(filename):
		f = open(filename, "r")
		total += scanFile(f)
		f.close()

print("\nTotal: " + str(total))
