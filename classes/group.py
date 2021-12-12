from classes.list_base import ListBase
import uuid

'''

This file contains the 'Group' Class. This is an exention of the ListBase class
with added fields and functionality that relates to dealing with Groups.
the module uuid is imported to create unique ids to be able to link groups to contacts
when groups and contacts are imported from json.

'''

class Group(ListBase):

	def __init__(self):
		super().__init__()
		self.group_name = None
		self.group_description = None
		self.group_id = None



#-------------------------- Private Methods --------------------------------

	def __create_group(self, group_name, group_description, group_id = None):
		self.group_name = group_name
		self.group_description = group_description

		if group_id == None:
			self.group_id = 'group' + str(uuid.uuid4())
		else:
			self.group_id = group_id	



#-------------------------- Public Methods --------------------------------

	def append_contact_from_json(self, contact):
		if contact.get_group_id() == self.group_id:
			self.append_contact(contact)


	def create_group_from_user_imput(self):
		group_name = input('Please enter group name: ').strip().lower()
		group_description = input('Enter group description: ')
		self.__create_group(group_name, group_description)
	
	def create_group_from_json(self, group):
		self.__create_group(group['group_name'], group['group_description'], group['group_id'])

	def display_group(self):
		print(f'--------- {self.group_name} --------- \n {self.group_description}' )
		self.display_contacts()

#-------------------------- Getters And Setters --------------------------------
