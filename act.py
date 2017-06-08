#!/bin/python

import os

def main():
	total = 0
	for filename in os.listdir("."):
		if chkIfSrc(filename):
			f = open(filename, "r")
			total += scanFile(f)
			f.close()
	print("\nTotal: " + str(total))

# checks if the file is a src file by extension
def chkIfSrc(filename):
	extensions = [".c", ".cpp", ".cs", ".h", ".hpp", ".java"]
	for ext in extensions:
		if filename.endswith(ext):
			return True
	return False

# formats a line with a todo tag in it
def formatter(lineNum, line):
	# remove actual line of code if there is any
	tmp = line.lower()
	todoStart = tmp.index("todo")
	line = line[todoStart:]
	# remove comment stuff
	toReplace = ["//", "/*", "*/", "TODO:", "todo:", "TODO", "todo"]
	for rep in toReplace:
		line = line.replace(rep, "")
	line = line.strip()
	# truncate line if it's too long
	line = (line[:50] + "...") if len(line) > 50 else line
	# add "???" if it's empty now
	line = line if line else "???"
	return str(lineNum) + ": \"" + line + "\""

# checks if a line is a comment and if it has a todo tag
def chkTodo(line):
	line = line.strip()
	# empty line
	if not line:
		return None
	if "//" in line or "/*" in line:
		tmp = line.lower()
		if "todo" in tmp:
			return line
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

if __name__ == "__main__":
	main()
