import json

class main:
	def __init__(self):
		self.contact_list = []
		self.groups = []

	def __import_from_json(self):
		pass

	def __save_to_json(self):
		pass

	def __sort_key(self, element):
		return element.contact_details['name'][0]

	def __sort_contacts(self):

		'''
		This method sorts the contact list into alphabetical order 
		by using a key function (__sort_key) that returns the name of the contact and passing
		this to the inbuilt python sort method. This will be run everytime a contact is added
		'''
		self.contact_list.sort(key = self.__sort_key)


# public methods

	def get_contacts(self):
		'''
		Prints contacts, allows you to be able to select contact to run the edit method on
		'''
		if len(self.contact_list) == 0:
			print ('No Contacts Found')
		else:
			print("Enter the number of the contact you want to view/edit")    
			for i,contact in enumerate(self.contact_list):
				print(f'{i + 1}: {contact.contact_details["name"]}')
			user_input = int(input()) - 1
			chosen_contact = self.contact_list[user_input]
			chosen_contact.display_user()



	def append_contact(self, contact):
		'''
		This appends a contact to the list, and then runs the sort method
		WILL, are you adding the save to JSON functionality here?
            
		'''
		self.contact_list.append(contact)
		self.__sort_contacts()

	def search(self):
		'''
		Provides functionality to search contact by various options 
            
		'''
		results = []
		print("1. Name\n2. Phone\n3. Address Line 1\n4. Address Line 2\n5. Postcode\n6. Email")
		search_attribute_input = input("Enter the number of the attribute you would like to search by: ")

		match search_attribute_input:
			case "1":
				search_attribute = "name"
			case "2":
				search_attribute = "phone"
			case "3":
				search_attribute = "address_1"
			case "4":
				search_attribute = "address_2"
			case "5":
				search_attribute = "postcode"
			case "6":
				search_attribute = "email"

		search_term = input("Enter the " + search_attribute + " you would like to search for: ")

		sanitised_search_term = search_term.strip().lower()

		for contact in self.contact_list:
			if contact.contact_details[search_attribute] == sanitised_search_term:
				results.append(contact.contact_details)
                           
				for i,result in enumerate(results):

					print("----------Contact: " + str(i+1) + "----------")
					for detail in result:
						detail_title = ' '.join(detail.split('_')).capitalize()
						print(detail_title + ': ' + result[detail])
					print("\n--------------------------------")

				contact_selection = ("Enter the number of contact would you like to select: ")
            

	def delete_contact(self, contact):
		'''
		Deletes Contact
		'''
    
	def show_groups(self):

		'''
		This Method displays a list of groups, If no groups exist, It will offer up the functionality to 
		create a new one.
            
		'''

		print('Groups:')
		if len(self.groups) == 0:
			print('No Groups found')
		else:
			for i,group in enumerate(self.groups):
				print(f'{i+1}: {group.name}')

			print('Enter the number of the group you want to view, or enter A to add a new group')

			while True:
				user_input = input().lower()
				if user_input == 'a':
					self.add_group()
					break
				else:
					selected_group_index = int(user_input) - 1
					if selected_group_index < len(self.groups):
						selected_group = self.groups[selected_group_index]
						selected_group.get_contacts()
						break
					else:
						print('input not recognised, try again')


	def add_to_group_functionality(self, contact):

		print('Do you want to add this contact to a group? Y or N')
		while True:
			user_input = input().lower() 
			if user_input == 'y':
				if len(self.groups) == 0:
					print('No groups found, press A to add a group, or any other key to exit')
					user_input = input().lower()
					if user_input == 'a':
						new_group = self.add_group()
						new_group.append_contact(contact)
						print(f'{contact.contact_details["name"]} succesfully added to {new_group.name}')
					else:
						return
				else:
					print('Enter the number of the group you would like to add to')
					for i,group in enumerate(self.groups):
						print(f'{i+1}: {group.name} \n {group.group_description}') 
					while True:
						user_input = int(input()) - 1
						if user_input < len(self.groups):
							selected_group = self.groups[user_input]
							selected_group.append_contact(contact)
							print(f'{contact.contact_details["name"]} added to {selected_group.name}')
							break
						else:
							print('input not recognised')             
							break
			elif user_input == 'n':
				print('Contact Succesfully created')
				break
                   

        
	def add_group(self):
		'''
		Allows user to create a group
		'''
		new_group = group()
		new_group.create_group()
		self.groups.append(new_group)
		return new_group
        
	
	def delete_group(self, group):
            '''
            Allows user to delete a group
            '''
            pass



        
class group(main):

	'''
	This is the group class that extends the contact list class, this allows us to keep the
	features of being able to delete, remove and show the list of contacts
        '''
	def __init__(self):
		super().__init__()
		self.name = ''
		self.group_description = ''

	def create_group(self):
		group_name = input('Please enter group name: ').strip().lower()
		group_description = input('Enter group description: ')
		self.name = group_name
		self.group_description = group_description

              
        