#!/usr/bin/python

import sys

from Database import Database
from FileHandler import FileHandler

if __name__ == '__main__':

	if len(sys.argv) != 2:
		print "Invalid Parameters: <Specify data input file in argument>"
		sys.exit(0)
	else:
		filename = sys.argv[1]

	db_obj = Database()
	handler_obj = FileHandler(db_obj,filename)

	# read file and populate directory
	handler_obj.read_File()
	
	# sort the directory based on firstname and lastname basis
	db_obj.sortDirectory()

	# finally dump result to json result file
	handler_obj.jsonDump()
