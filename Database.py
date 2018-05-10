#!/usr/bin/python

from operator import itemgetter

class Database:
	
	directory = []	# a list of dicts
	errors = []
	
	def __init__(self):
                pass

	# validate for format
	def validate_format(self, field):
		# Lastname, Firstname, (703)-742-0996, Blue, 10013

		# field should be a phone number		
		field = field.replace("-","")
		field = field.replace(" ","")
		field = field.replace("(","")
		field = field.replace(")","")

		# should be a 10 digit mobile number
		if len(field) == 10 and field.isdigit():
			return True
		
		return False

	def validate(self, input, line_no):


		input = input.split(",")
		
		# should contain 5 fields
		if len(input) <= 4 :
			self.errors.append(line_no)
			return False
		
		# 3 formats allowed	
		# Lastname, Firstname, (703)-742-0996, Blue, 10013
		# Firstname Lastname, Red, 11237, 703 955 0373
		# Firstname, Lastname, 10013, 646 111 0101, Green
			
		field_1 = input[0].strip()
		field_2 = input[1].strip()
		field_3 = input[2].strip()
		field_4 = input[3].strip()
		field_5 = input[4].strip()

		entry = {}

		##########
		# Format 1
		if self.validate_format(field_3) == True:
			# validate for format 1, filed_2 should be a mobile number
	
			if len(field_5) != 5 or not field_5.isdigit():
				self.errors.append(line_no)
                                return False

			entry["color"] = field_4
			entry["firstname"] = field_2
			entry["lastname"] = field_1
                        entry["phonenumber"] = field_3
                        entry["zipcode"] = field_5

			pass
		##########
                # Format 2
		elif self.validate_format(field_5) == True:
			# validate for format 2, filed_5 should be a mobile number

			if len(field_4) != 5 or not field_4.isdigit():
				self.errors.append(line_no)
				return False


                        entry["color"] = field_3
                        entry["firstname"] = field_1
                        entry["lastname"] = field_2
                        entry["phonenumber"] = field_5
                        entry["zipcode"] = field_4

			pass
		#########
                # Format 3
		elif self.validate_format(field_4) == True:
			# validate for format 3, filed_4 should be a mobile number

			if len(field_3) != 5 or not field_3.isdigit():
				self.errors.append(line_no)
                                return False

                        entry["color"] = field_5
                        entry["firstname"] = field_1
                        entry["lastname"] =  field_2
                        entry["phonenumber"] =  field_4
                        entry["zipcode"] = field_3
			
			pass
		else:
			# does not match any of the 3 formats
			self.errors.append(line_no)
			return False

		print self.sortbyKeys(entry)
		return entry

	def sortbyKeys(self, adict):

		#sortedD = sorted(dict.items(), key=lambda x: x[0])	
		keys = adict.keys(  )
    		keys.sort(  )
    		return [adict[key] for key in keys]

		return sortedD
		pass

	def add_to_database(self, dict_entry):
		self.directory.append(dict_entry)
		pass

	def validate_and_add(self, input, line_no):
	
		dict_entry = self.validate(input, line_no)	
		if dict_entry != False:
			self.add_to_database(dict_entry)

	def sortDirectory(self):
		self.directory = sorted(self.directory, key=itemgetter('firstname', 'lastname'))
	
'''
if __name__ == '__main__':
        db = Database()
        db.validate_and_add()
'''
