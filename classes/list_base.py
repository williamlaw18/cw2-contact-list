import json

'''
This acts as a parent class for our two types of lists. We have a ContactList which acts as our main storage of
contacts, we also have group lists which act as ways of grouping contacts. The reason why there is a parent class
is that there is a bunch of functionality that we want to share. For example, the ability to list all the contacts,
the ability to append a contact onto itself and also a search functionality.

'''

class ListBase:
	def __init__(self):
		self.contact_list = []


#-------------------------- Private Methods --------------------------------

	def __sort_key(self, element):
		return element.get_contact_details()['name'][0]

	def __sort_contacts(self):

		'''
		This method sorts the contact list into alphabetical order 
		by using a key function (__sort_key) that returns the name of the contact and passing
		this to the inbuilt python sort method. This will be run everytime a contact is added
		'''
		self.contact_list.sort(key = self.__sort_key)



#-------------------------- Public Methods --------------------------------

	def display_contacts(self):
		'''
		Prints contacts, allows you to be able to select contact to run the edit method on
		'''
		if len(self.contact_list) == 0:
			print ('No Contacts Found')
		else:
            
			for i,contact in enumerate(self.contact_list):
				print(f'{i + 1}: {contact.get_contact_details()["name"]}')
			print("Enter the number of the contact you want to view/edit, or press s to search ")    
			while True:
				try:
					user_input = input()
					if(user_input.lower() == 's'):
						self.search()
						break
					else:
						user_selection = int(user_input) -1
						chosen_contact = self.contact_list[user_selection]
						chosen_contact.display_user()
						break
				except:
					print('input not recognised')
            
            

	def append_contact(self, contact):
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
			if contact.get_contact_details()[search_attribute] == sanitised_search_term:
				results.append(contact.get_contact_details())
                           
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
      
#-------------------------- Getters and Setters --------------------------------
	def get_groups(self):
		return self.__groups()