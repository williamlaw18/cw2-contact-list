import json
from csv import reader
from classes.contact import Contact
from classes.group import Group


class ImportExport:
	def __init__(self, contact_list):
		self.__contact_list = contact_list
		self.__contacts_path = './data/contacts.json'
		self.__groups_path = './data/groups.json'

#-------------------------- Public Methods --------------------------------

	def read_from_json(self):

		'''
		This method opens our contactList.json file, using the imported json library, it
		parses a list from the file, which contains two dictionaries: groups and contacts
		from these, using the create_group_from_json method and the create_contact_from_json method
		these classes are instansiated and stored in the correct place.
		'''
		   
		with open(self.__groups_path, "r") as jsonPathGroup:
			jsonPathFile = json.load(jsonPathGroup)
			imported_group_list = jsonPathFile

			for json_group in imported_group_list:
				imported_group = Group()
				imported_group.create_group_from_json(json_group)
				self.__contact_list.append_groups(imported_group)
			jsonPathGroup.close()   


		with open(self.__contacts_path, "r") as jsonPath:
			jsonFile = json.load(jsonPath)
			imported_contact_list = jsonFile
					
			for json_contact in imported_contact_list:
				imported_contact = Contact()
				imported_contact.create_contact_from_json(json_contact['_Contact__contact_details'], json_contact['_Contact__group_ids'])
				self.__contact_list.append_contact(imported_contact)

				for existing_group in self.__contact_list.get_groups():
					existing_group.append_contact_from_json(imported_contact)
			jsonPath.close()    


	def save(self):
		'''
		Passes the groups and contacts contained on the contact_list class to
		the privite export_to_json method along with the correct path
		'''
		self.__export_to_json(self.__contacts_path, self.__contact_list.get_contacts())
		self.__export_to_json(self.__groups_path, self.__contact_list.get_groups_for_json())

	def import_from_csv(self):
		"""
		This method imports contact information from a CSV file
		USE IMPORT_CONTACTS_FROM_JSON in CONTACT
		"""
		target_path = input("Enter the path and file name of the contacts file you want to import: ")
		try:
			with open(target_path, "r") as imports:
				imports = list(reader(imports))
			csv_dict = {
			    'first_name': " ",
			    'second_name': " ",
			    'phone': " ",
			    'email' : " ",
			    'house_name_or_number': " ",
			    'address_line_1': " ",
			    'address_line_2': " ",
			    'postcode': " ",
			}
			for i in range(1,len(imports)):
				for j in range(0,len(imports[0])):
					if imports[i][j] == "":
						continue
					match imports[0][j].lower():
					       case "first name": csv_dict["first_name"] = imports[i][j].lower()
					       case "last name": csv_dict["second_name"] = imports[i][j].lower()
					       case "primary phone": csv_dict["phone"] = imports[i][j].lower()
					       case "e-mail address": csv_dict["email"] = imports[i][j].lower()
					       case "home address": csv_dict["house_name_or_number"] = imports[i][j].lower()
					       case "home street": csv_dict["address_line_1"] = imports[i][j].lower()
					       case "home street 2": csv_dict["address_line_2"] = imports[i][j].lower()
					       case "home postal code": csv_dict["postcode"] = imports[i][j].lower()
					       case _: pass
					       
				new_contact = Contact()
				new_contact.create_contact_from_json(csv_dict, [])
				self.__contact_list.append_contact(new_contact)
					       
			print("Contacts Imported.")
						
		except:
			print("Import failed.")
			
	def export_to_csv(self):
		"""
		This method exports all of the contacts in the contact list to a CSV file, which any other contact managing software can import from.
		"""
		target_path = input("Enter the path of the folder you want the contacts exported to: ")
		file_name = "\\contacts.csv"
		try:
			with open(target_path+file_name, "w") as export:
				export.write("First Name,Last Name,Primary Phone,E-Mail Address,Home Address,Home Street,Home Street 2,Home Postal Code")
				for contact in self.__contact_list.get_contacts():
					details = list(contact.get_contact_details().values())
					export.write("\n")
					for detail in details:
						export.write(str(detail)+",")
			print("Contacts exported to "+target_path+file_name)
		except:
			print("Export failed.")

#-------------------------- Private Methods --------------------------------
	
	def __export_to_json(self, path, object):
		'''
		Exports the contacts or the groups passed to it to
		a json file located on the path param.
		'''

		json_object = self.__to_JSON(object)
		with open(path, "w") as file:
			file.write(json_object)


	def __to_JSON(self, object):
		return json.dumps(object, default=lambda o: o.__dict__, 
			sort_keys=False, indent=4)

