#!/bin/python

import getopt
import os
import re
import sys

def main():
	recursive = False
	try:
		opts, args, = getopt.getopt(sys.argv[1:], "r")
	except getopt.GetoptError:
		print("Usage: act [-r]\n"
			"  -r        search directories recursively")
		sys.exit(1)
	for opt, arg in opts:
		if opt in "-r":
			recursive = True
	total = read_dir(".", recursive)
	print("Total: " + str(total))

# recursively (or not) search the given directory for source files
# returns total amount of TODO comments found
def read_dir(path, recursive):
	total = 0
	for name in os.listdir(path):
		if recursive and os.path.isdir(name):
			total += read_dir(name, recursive)
		elif check_if_src(name):
			total += read_file(path + "/", name)
	return total

# checks if the given file is a source file by extension
def check_if_src(name):
	extensions = [".c", ".cpp", ".cs", ".h", ".hpp", ".java", ".py", ".sh"]
	for ext in extensions:
		if name.endswith(ext):
			return True
	return False

# scans a file for TODO tags and prints them
def read_file(path, name):
	total = 0
	line_num = 1
	todo_list = []
	src = open(path + name, "r")
	# check each line for a TODO
	for line in src:
		if check_todo(line):
			todo_list.append(formatter(line_num, line))
			total += 1
		line_num += 1
	# print TODO list
	if todo_list:
		print(name + ":")
		for todo in todo_list:
			print(todo)
		print("")
	src.close
	return total

# checks if a line has a TODO
def check_todo(line):
	if not line:
		return False
	pattern = re.compile("\\btodo\\b", re.I)
	match = re.search(pattern, line)
	if match:
		return True
	return False

# formats a line with a TODO tag in it
def formatter(lineNum, line):
	line = line.strip()
	# add colour around TODO
	tmp = line.lower()
	index = tmp.find("todo")
	line = line[:index] + "\x1b[1;31m" + line[index:index + 4] + "\x1b[0m" + line[index + 4:]
	# truncate line if it's too long
	line = (line[:70] + "...") if len(line) > 70 else line
	return str(lineNum).rjust(4) + ": " + line

if __name__ == "__main__":
	main()
