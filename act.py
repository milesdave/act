#!/bin/python

import os

def main():
	# TODO only recurse if specified
	total = read_dir(".", True)
	print("\nTotal: " + str(total))

# recursively (or not) search the given directory for source files
def read_dir(path, recursive):
	total = 0 # total TODO comments
	for name in os.listdir(path):
		if recursive and os.path.isdir(name):
			total += read_dir(name, recursive)
		else:
			if check_if_src(name):
				f = open(path + "/" + name, "r")
				total += scanFile(f)
				f.close()
	return total

# checks if the given file is a source file by extension
def check_if_src(name):
	extensions = [".c", ".cpp", ".cs", ".h", ".hpp", ".java", ".py", ".sh"]
	for ext in extensions:
		if name.endswith(ext):
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
