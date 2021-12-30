import json
import helper_methods.helper as helper
import string

'''
This acts as a parent class for our two types of lists. We have a ContactList which acts as our main storage of
contacts, we also have group lists which act as ways of grouping contacts. The reason why there is a parent class
is that there is a bunch of functionality that we want to share. For example, the ability to list all the contacts,
the ability to append a contact onto itself and also a search functionality.

'''

class ListBase:
	def __init__(self):
		self.contact_list = []
		self.sort_by_identifier = 'second_name'


#-------------------------- Private Methods --------------------------------

	def __sort_key(self, element):
		'''
		This method stores the first letter of the field value of what we want to sort by in 
		contact_field_value and returns the index of the alphebet of that particular letter,
		to be used in the search method
	
		'''
	

		contact_field_value = element.get_contact_details()[self.sort_by_identifier][0]
		contact_field_string_index = string.ascii_lowercase.index(contact_field_value)
		
		return contact_field_string_index 

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
				contact_name = helper.format_values(contact.get_contact_name(), 'name')
				print(f'{i + 1}: {contact_name}')
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
						chosen_contact.display_contact(self)
						break
				except ValueError:
					print('Please enter a valid number, or press x to exit')
				except IndexError:
					print('No contact exists at that selection, please try again')
			
            
            

	def append_contact(self, contact):
		self.contact_list.append(contact)
		self.__sort_contacts()

	def search(self):
		'''
		Provides functionality to search contact by various options   
		'''
		results = []
		while True:
			#print and user input to display options that the search functionailty provides
			print("1. First Name\n2. Last Name\n3. Phone Number\n4. Email\n5. House Name or Number\n6. Address Line 1\n7. Address Line 2\n8. Postcode\nOr press x to exit back to the home screen")
			search_attribute_input = input("Enter the number of the aspect you would like to search by: ").lower()
			'''
			this statement converts the user friendly input (numbers) into the "search attributes" that
			are required to interact with the list imported from the json file that contain
			the contacts in the contact book
			it also assigns variable to output to the user that looks more user friendly
			'''
			match search_attribute_input:
				case "1":
					search_attribute = "first_name"
					break
				case "2":
					search_attribute = "second_name"
					break
				case "3":
					search_attribute = "phone"
					break
				case "4":
					search_attribute = "email"
					break
				case "5":
					search_attribute = "house_name_or_number"
					break
				case "6":
					search_attribute = "address_line_1"
					break
				case "7":
					search_attribute = "address_line_2"
					break
				case "8":
					search_attribute = "postcode"
					break
				case "x":
					return
				case _:
					print("Invalid input, pleae enter number 1-8")

		#accept the search term for the desired attribute, and then remove any spaces from either end, or capitilisation
		UXattribute = helper.format_title(search_attribute)
		search_term = input("Enter the " + UXattribute + " you would like to search for: ")

		sanitised_search_term = search_term.strip().lower()
		'''
		this block of code iterates to search for each contact in the contact book
		it checks to see if the search query is a substring of the current name and then
		adds it to a list
		'''
		for contact in self.contact_list:
			if sanitised_search_term in contact.get_contact_details()[search_attribute]:  
				results.append(contact)   
			 
				'''
				This code iterates for each contact that was found that contains the substring
				it outputs alongside an identifier from 1 to n amount of contacts
				along with the rest of the details about the contact using the format: Attribute: *attribute value*
				each contact is surrounded by a series of dashes to make contacts more readabe when more than one
				is returned
				'''

		for i,result in enumerate(results):
			print("\n----------Contact: " + str(i+1) + "----------\n")
			result_contact_details = result.get_contact_details()
			for detail in result_contact_details:
				detail_title = helper.format_title(detail, True)
				print(detail_title + ': ' + helper.format_values(result_contact_details[detail], detail))
			print("\n--------------------------------\n")

		if len(results) == 0:
			print("No contacts found for search term", search_term, "with aspect", UXattribute, "Please try again or press x to exit")
			self.search()
			return
		else:
			print('Enter the number of the contact you would like to view, or press x to exit')

		while True:
			try:
				user_input = input()
				if(user_input.lower() == 'x'):
					break
				else:
					user_selection = int(user_input) -1
					chosen_contact = results[user_selection]
					chosen_contact.display_contact(self.contact_list)
					break
			except ValueError:
				print('Please enter a valid number, or press x to exit')
			except IndexError:
				print('No contact exists at that selection, please try again')


            

	def delete_contact(self, contact):
		'''
		Deletes Contact
		'''
      
	def clear_all_contacts(self):
		self.contact_list = []

