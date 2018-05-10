#!/usr/bin/python

import sys
from Database import Database
import json

class FileHandler:

	filename = "input/data.in"	
	resultfile = "result.json"
	db = Database()

	def __init__(self,database_obj):
		self.db = database_obj
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

	def jsonDump(self):
		json_dict = {}
                json_dict["entries"] = self.db.directory
		try:
	                with open(self.resultfile, 'w') as fp:
        	                json.dump(json_dict, fp, indent=2)
		except Exception as e:
                        print e
                        sys.exit(0)
                pass

'''
if __name__ == '__main__':
	reader = FileHandler()
	reader.read_File()		
'''
