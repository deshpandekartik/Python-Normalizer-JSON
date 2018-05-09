#!/usr/bin/python

import sys
from Database import Database

class FileParser:

	filename = "input/data.in"	
	db = Database()

	def __init__(self):
		pass

	# remove new line characters and trims the line
	def streamline(self,input):
		return input.strip();
	
	def read_File(self):

		try:		
			with open(self.filename) as file:
				for line in file:
					line = self.streamline(line)
					self.db.validate_and_add(line)
		except Exception as e:
			print e
			sys.exit(0)
		pass	

	
if __name__ == '__main__':
	reader = FileParser()
	reader.read_File()		
