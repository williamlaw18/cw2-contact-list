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
		self.sort_by_indetifier = 'second_name'


#-------------------------- Private Methods --------------------------------

	def __sort_key(self, element):
		'''
		This method stores the first letter of the field value of what we want to sort by in 
		contact_field_value and returns the index of the alphebet of that particular letter,
		to be used in the search method
	
		'''
	

		contact_field_value = element.get_contact_details()[self.sort_by_indetifier][0]
		contact_field_string_index = string.ascii_lowercase.index(contact_field_value)
		
		return contact_field_string_index 

	def __sort_contacts(self):

		'''
		This method sorts the contact list into alphabetical order 
		by using a key function (__sort_key) that returns the name of the contact and passing
		this to the inbuilt python sort method. This will be run everytime a contact is added
		'''
		self.contact_list.sort(key = self.__sort_key)
		print('sorting')



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
				# try:
					user_input = input()
					if(user_input.lower() == 's'):
						self.search()
						break
					else:
						user_selection = int(user_input) -1
						chosen_contact = self.contact_list[user_selection]
						chosen_contact.display_contact()
						break
				# except:
					print('input not recognised')
            
            

	def append_contact(self, contact):
		self.contact_list.append(contact)
		self.__sort_contacts()

	def search(self):
		'''
		Provides functionality to search contact by various options   
		'''
		results = []
		#print and user input to display options that the search functionailty provides
		print("1. First Name\n2. Last Name\n3. Phone Number\n4. Email\n5. House Name or Number\n6. Address Line 1\n7. Address Line 2\n8. Postcode")
		search_attribute_input = input("Enter the number of the attribute you would like to search by: ")
		'''
		this statement converts the user friendly input (numbers) into the "search attributes" that
		are required to interact with the list imported from the json file that contain
		the contacts in the contact book
		it also assigns variable to output to the user that looks more user friendly
		'''
		match search_attribute_input:
			case "1":
				search_attribute = "first_name"
			case "2":
				search_attribute = "last name"
			case "3":
				search_attribute = "phone"
			case "4":
				search_attribute = "email"
			case "5":
				search_attribute = "house_name_or_number"
			case "6":
				search_attribute = "address_line_1"
			case "7":
				search_attribute = "address_line_2"
			case "8":
				search_attribute = "postcode"

		#accept the search term for the desired attribute, and then remove any spaces from either end, or capitilisation
		UXattribute = helper.format_title(search_attribute).lower()
		search_term = input("Enter the " + UXattribute + " you would like to search for: ")

		sanitised_search_term = search_term.strip().lower()
		'''
		this block of code iterates to search for each contact in the contact book
		it checks to see if the search query is a substring of the current name and then
		adds it to a list
		'''
		for contact in self.contact_list:
			if sanitised_search_term in contact.get_contact_details()[search_attribute]:  
				results.append(contact.get_contact_details())   
				print(results)   
				'''
				This code iterates for each contact that was found that contains the substring
				it outputs alongside an identifier from 1 to n amount of contacts
				along with the rest of the details about the contact using the format: Attribute: *attribute value*
				each contact is surrounded by a series of dashes to make contacts more readabe when more than one
				is returned
				'''
		for i,result in enumerate(results):
			print("\n----------Contact: " + str(i+1) + "----------\n")
			for detail in result:
				detail_title = ' '.join(detail.split('_')).capitalize()
				print(detail_title + ': ' + result[detail])
			print("\n--------------------------------\n")

		contact_selection = int(input("Enter the number of contact would you like to select: "))
		return results[contact_selection - 1] #returning the result of the search to be used in a higher order function
		

            

	def delete_contact(self, contact):
		'''
		Deletes Contact
		'''
      

