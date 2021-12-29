import json
from classes.list_base import ListBase

'''
This is the ContactList Class, this is only expected to be instanciated once, and that is on the main
program load. This extends from ListBase, takes all the contact storage, search functionality and adds 
the ability to store groups

'''

class ContactList(ListBase):
	def __init__(self):
		super().__init__()
		self.__groups = []

#-------------------------- Private Methods --------------------------------

#Empty for now

#-------------------------- Public Methods --------------------------------

	def append_groups(self, group):
		'''
		this method simply allows external classes to append a group to it's group list
		'''
		self.__groups.append(group)

	def list_groups(self):

		'''
		this method prints out the self.__groups field (the list of groups we have)
		and returns the list, so that items can be accessed on it from outside this 
		class.
            
		'''
		print('Groups:')
		if len(self.__groups) == 0:
			print('No Groups found')
		else:
			for i,group in enumerate(self.__groups):
				print(f'{i+1}: {group.get_group_name()}')

		return self.__groups	
      
#-------------------------- Getters and Setters --------------------------------
	def get_groups(self):
		return self.__groups

	def get_contacts(self):
		return self.contact_list