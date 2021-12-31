import json
from classes.list_base import ListBase


'''
This is the ContactList Class, this is only expected to be instanciated once, and that is on the main
program load.  This extends from ListBase, takes all the contact storage, search functionality and adds 
the ability to store groups.

'''

class ContactList(ListBase):
	def __init__(self):
		super().__init__()
		self.__groups = []
		self.__name = 'Contact List'


#-------------------------- Public Methods --------------------------------

	def append_groups(self, group):
		'''This method simply allows external classes to append a group to the __groups list.'''
		self.__groups.append(group)


	def list_groups(self):

		'''
		This method prints out the self.__groups field (the list of groups we have)
		and returns the list, so that items can be accessed on it from outside this 
		class.
            
		'''
		print('Groups:')
		if len(self.__groups) == 0:
			print('No groups found!')
		else:
			for i,group in enumerate(self.__groups):
				print(f'{i+1}: {group.get_name()}')

		return self.__groups	

      
#-------------------------- Getters and Setters --------------------------------
	def get_groups(self):
		return self.__groups

	def get_groups_for_json(self):
		'''
		This returns a list of groups without the: contact_list field
		to create a cleaner json export.
		
		'''
		group_list = []
		for group in self.__groups:
			group_dict = {
				"_Group__group_name": group.get_name(),
				"_Group__group_description": group.get_group_description(),
				"_Group__group_id": group.get_group_id()
			}
			group_list.append(group_dict)

		return group_list


	def get_contacts(self):
		return self.contact_list
		

	def get_name(self):
		return self.__name