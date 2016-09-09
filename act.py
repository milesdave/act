#!/bin/python

import os

# checks if the file is a src file by extension
def chkIfSrc(filename):
	extensions = [".c", ".cpp", ".cs", ".h", ".hpp", ".java"]
	for ext in extensions:
		if ext in filename:
			return True
	return False

# formats a line with a todo tag in it
def formatter(lineNum, line):
	toReplace = ["//", "/*", "TODO", "todo"]
	for rep in toReplace:
		line = line.replace(rep, "")
	line = line.strip()
	return str(lineNum) + ": \"" + line + "\""

# checks if a line is a comment and if it has a todo tag
def chkTodo(line):
	line = line.strip()
	# empty line
	if not line:
		return None
	tmp = line.lower()
	if line[0] == '/':
		# single line comment
		if line[1] == '/':
			if "todo" in tmp:
				return line
		# multi-line comment
		elif line[1] == '*':
			if "todo" in tmp:
				return line + "..."
	return None

# scans a file for todo tags and prints them
def scanFile(f):
	total = 0
	lineNum = 1
	todoList = []
	# check each line for a todo
	for line in f:
		todo = chkTodo(line)
		if todo:
			todoList.append(formatter(lineNum, todo))
			total += 1
		lineNum += 1
	# print todoList
	if todoList:
		print(f.name + ":")
		for todo in todoList:
			print("  " + todo)
	return total

total = 0

for filename in os.listdir(os.getcwd()):
	if chkIfSrc(filename):
		f = open(filename, "r")
		total += scanFile(f)
		f.close()

print("\nTotal: " + str(total))
