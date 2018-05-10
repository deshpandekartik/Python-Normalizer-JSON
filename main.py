#!/usr/bin/python

from Database import Database
from FileHandler import FileHandler

if __name__ == '__main__':

	db_obj = Database()
	handler_obj = FileHandler(db_obj)

	# read file and populate directory
	handler_obj.read_File()
	
	# sort the directory based on firstname and lastname basis
	db_obj.sortDirectory()

	# finally dump result to json result file
	handler_obj.jsonDump()
