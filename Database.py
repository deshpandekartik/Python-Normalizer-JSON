#!/usr/bin/python

class Database:
	
	directory = []	# a list of dicts
	
	def __init__(self):
                pass

	def validate(self, input):
	
		print input	

	def add_to_database(self):
		pass

	def extract(self,input):	
		pass

	def validate_and_add(self, input):
		
		if self.validate(input) != False:
			self.add_to_database()
			

'''
if __name__ == '__main__':
        db = Database()
        db.validate_and_add()
'''
