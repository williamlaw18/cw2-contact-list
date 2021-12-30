import json
from classes.contact import Contact
from classes.group import Group


class ImportExport:
	def __init__(self, contact_list):
		self.__contact_list = contact_list
		self.__contacts_path = './data/contacts.json'
		self.__groups_path = './data/groups.json'


	def read_from_json(self):

		'''
		This method opens our contactList.json file, using the imported json library, it
		parses a list from the file, which contains two dictionaries: groups and conttacts
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
		self.__export_to_json(self.__contacts_path, self.__contact_list.get_contacts())
		self.__export_to_json(self.__groups_path, self.__contact_list.get_groups())
	

	def __export_to_json(self, path, object):
		json_object = self.__to_JSON(object)
		with open(path, "w") as file:
			file.write(json_object)


	def __to_JSON(self, object):
		return json.dumps(object, default=lambda o: o.__dict__, 
			sort_keys=False, indent=4)

