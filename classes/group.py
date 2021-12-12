from classes.list_base import ListBase
import uuid

'''

This file contains the 'Group' Class. This is an extenstion of the ListBase class
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

		'''
		This method fills in the class fields, based on the arguments passed to it.
		Somthing to look at is the group_id argument. if we are creating the group from
		json, a id would allready be provided. We want to assign that normally, howver, if
		a group is created from scratch, we want it to be defaulted as none, so the method
		can generate a unique one by using the uuid library. 
		
		'''

		self.group_name = group_name
		self.group_description = group_description

		if group_id == None:
			self.group_id = 'group' + str(uuid.uuid4())
		else:
			self.group_id = group_id	



#-------------------------- Public Methods --------------------------------

	def append_contact_from_json(self, contact):

		'''
		This method is called from the __read_from_json method on the main class. The aformentioned method loops through the 
		list of groups, and calls this method passing the json-generated contact to it. If the id on the contact matches
		the group id, the contact is appended to the list using the append_contact method from the parent class.
		'''

		if contact.get_group_id() == self.group_id:
			self.append_contact(contact)


	def create_group_from_user_imput(self):

		'''
		Pretty much self explanitory. takes inputs from user and passes it to the __create_group method
		
		'''

		group_name = input('Please enter group name: ').strip().lower()
		group_description = input('Enter group description: ')
		self.__create_group(group_name, group_description)
	
	def create_group_from_json(self, group):
		'''
		takes group passed from __read_from_json method on the main class and runs the __create_group method
		'''
		self.__create_group(group['group_name'], group['group_description'], group['group_id'])

	def display_group(self):
		'''
		Prints out the list of contacts in the group by calling the display_contacts method on the parent class
		'''

		print(f'--------- {self.group_name} --------- \n {self.group_description}' )
		self.display_contacts()

#-------------------------- Getters And Setters --------------------------------
