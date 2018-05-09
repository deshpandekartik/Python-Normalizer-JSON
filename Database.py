#!/usr/bin/python

class Database:
	
	directory = []	# a list of dicts
	
	def __init__(self):
                pass

	# validate for format 1
	def validate_format(self, field):
		# Lastname, Firstname, (703)-742-0996, Blue, 10013

		# field_2 should be a phone number		
		check = field.replace("-","")
		check = field.replace(" ","")
		check = field.replace("(","")
		check = field.replace(")","")

		# should be a 10 digit mobile number
		if len(check) == 10:
			return True
		
		return False

	def validate(self, input):
	
		input = input.split(",")
		
		# should contain 5 fields
		if len(input) <= 4 :
			return False
		
		# 3 formats allowed	
		# Lastname, Firstname, (703)-742-0996, Blue, 10013
		# Firstname Lastname, Red, 11237, 703 955 0373
		# Firstname, Lastname, 10013, 646 111 0101, Green
			
		field_1 = input[0]
		field_2 = input[1]
		field_3 = input[2]
		field_4 = input[3]
		field_5 = input[4]

		entry = {}
		if self.validate_format(field_2) == True:
			# validate for format 1, filed_2 should be a mobile number

			entry["color"] =
			entry["firstname"] =
			entry["lastname"] =
                        entry["phonenumber"] =
                        entry["zipcode"] =

			pass
		elif self.validate_format(field_5) == True:
			# validate for format 2, filed_5 should be a mobile number

                        entry["color"] =
                        entry["firstname"] =
                        entry["lastname"] =
                        entry["phonenumber"] =
                        entry["zipcode"] =


			pass
		elif self.validate_format(field_4) == True:
			# validate for format 1, filed_4 should be a mobile number

                        entry["color"] =
                        entry["firstname"] = 
                        entry["lastname"] = 
                        entry["phonenumber"] = 
                        entry["zipcode"] =
			
			pass
		else:
			# does not match any of the 3 formats
			return False


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
