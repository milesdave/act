#!/bin/python

import os

def main():
	# TODO only recurse if specified
	total = read_dir(".", True)
	print("Total: " + str(total))

# recursively (or not) search the given directory for source files
# returns total amount of TODO comments found
def read_dir(path, recursive):
	total = 0 # total TODO comments
	for name in os.listdir(path):
		if recursive and os.path.isdir(name):
			total += read_dir(name, recursive)
		elif check_if_src(name):
			print(name + ":")
			total += read_file(path + "/" + name)
	return total

# checks if the given file is a source file by extension
def check_if_src(name):
	extensions = [".c", ".cpp", ".cs", ".h", ".hpp", ".java", ".py", ".sh"]
	for ext in extensions:
		if name.endswith(ext):
			return True
	return False

# scans a file for TODO tags and prints them
def read_file(name):
	total = 0
	line_num = 1
	todo_list = []
	src = open(name, "r")
	# check each line for a todo
	for line in src:
		todo = chkTodo(line)
		if todo:
			todo_list.append(formatter(line_num, todo))
			total += 1
		line_num += 1
	# print todoList
	if todo_list:
		for todo in todo_list:
			print("  " + todo)
		print("")
	src.close
	return total

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

if __name__ == "__main__":
	main()
