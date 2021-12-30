import json
from classes.list_base import ListBase
import helper_methods.helper as helper
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
		self.__group_name = None
		self.__group_description = None
		self.__group_id = None



#-------------------------- Private Methods --------------------------------

	def __create_group(self, group_name, group_description, group_id = None):

		'''
		This method fills in the class fields, based on the arguments passed to it.
		Somthing to look at is the group_id argument. if we are creating the group from
		json, a id would allready be provided. We want to assign that normally, howver, if
		a group is created from scratch, we want it to be defaulted as none, so the method
		can generate a unique one by using the uuid library. 
		
		'''

		self.__group_name = group_name
		self.__group_description = group_description

		if group_id == None:
			self.__group_id = 'group' + str(uuid.uuid4())
		else:
			self.__group_id = group_id	



#-------------------------- Public Methods --------------------------------

	def append_contact_from_json(self, contact):

		'''
		This method is called from the __read_from_json method on the main class. The aformentioned method loops through the 
		list of groups, and calls this method passing the json-generated contact to it. If the id on the contact matches
		the group id, the contact is appended to the list using the append_contact method from the parent class.
		'''

		if contact.get_group_id() == self.__group_id:
			self.append_contact(contact)


	def create_group_from_user_input(self):

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
		self.__create_group(group['_Group__group_name'], group['_Group__group_description'], group['_Group__group_id'])

	def display_group(self):
		'''
		Prints out the list of contacts in the group by calling the display_contacts method on the parent class
		'''

		print(f'--------- {self.__group_name} --------- \n {self.__group_description}' )
		self.display_contacts()


#-------------------------- Getters --------------------------------

	def get_group_name(self):
		return self.__group_name
	def get_group_id(self):
		return self.__group_id
	def get_group_description(self):
		return self.__group_description

#-------------------------- Static Methods --------------------------------

	@staticmethod
	def static_add_to_group(contact, contact_list):
		
		'''
		When called from the __create_contact method, this allows the user to choose if they want to add the new 
		contact to a group.
		'''

		contact_name = helper.format_values(contact.get_contact_name(), 'name')
		print(f'Enter Y to add {contact_name} to a group, or any other key to continue')
		user_input = input()
		if(user_input.lower() == 'y'):
			
			group_list = contact_list.list_groups()
			print('Select the number of the group you want to add to, or press A to create a new group')
			while True:
				try:
					user_input = input()
					if user_input.lower() == 'a':
						new_group = Group()
						new_group.create_group_from_user_input()
						contact.set_group_id(new_group.get_group_id())
						new_group.append_contact(contact)
						contact_list.append_groups(new_group)

						json_object = helper.toJSON(contact_list.get_groups())
						with open("./data/groups.json", "w") as file:
							file.write(json_object)
						break
					else:
						user_selection = int(user_input) - 1
						selected_group = group_list[user_selection]
						contact.set_group_id(selected_group.get_group_id())
						group_list[user_selection].append_contact(contact)
						print('Succesfully added to group')
						break
				except ValueError:
					print('Please enter a valid number, or press A to make a new group')
				except IndexError:
					print('No group exists at that selection, please try again')

		else:
			return 

	@staticmethod
	def static_display_and_add_groups(contact_list):
		'''
		This method is called directly from the menu, it lists all the groups, and gives the option to either add
		a new group (by calling create_group_from_user_input) or viewing the contents of an existing one by selecting
		a number
		
		'''
		group_list = contact_list.list_groups()
		print('Enter the number of the group you would like to view, or press A to add a new one')
		while True:
			try:
				user_input = input()
				if user_input.lower() == 'a':
					new_group = Group()
					new_group.create_group_from_user_input()
					contact_list.append_groups(new_group)

					json_object = helper.toJSON(contact_list.get_groups())
					with open("./data/groups.json", "w") as file:
						file.write(json_object)
					break
				else:
					user_selection = int(user_input) - 1
					group_list[user_selection].display_group()
					break
			except ValueError:
				print('Please enter a valid number, or press A to add a new group')
			except IndexError:
				print('No group exists at that selection, please try again')
