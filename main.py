import json
from classes.contact import Contact
from classes.group import Group
from classes.contact_list import ContactList
from classes.favorites import Favorites

class ContactBook:
	def __init__(self):
		self.__contact_list = ContactList()
		self.__favorite_list = Favorites()
		self.__read_from_json()
		self.__run_program_loop()
				
	   
	def __run_program_loop(self):
	
		'''
		This method runs the main program loop. This waits on the user input, which is then entered into
		an if/else statement that will run the particular methods chosen by the user
	  
		'''

		while True:
			print('Enter the number of the feature you want, or press 1 to see the menu')
			user_input = input()

			match user_input:
				case '1':
					self.__show_menu()
				case '2':
					self.__create_contact()
				case '3':
					self.__show_contact_list()
				case '4':	
					self.__search_contact_list()
				case '5':
					self.__show_groups()
				case '6':
					self.__show_favorites()	
				case '7':
					print('Quiting program, Goodbye!')
					break
				case _:
					print('Sorry, input not recognised ')
			
			self.__loop_reset_logic()
		


	def __show_menu(self): 

		'''
		This method doesn't take any arguments, it just shows the menu as a printed string
		'''
		print('1. Menu\n2. Create Contact\n3. Show Contacts\n4. Search Contacts\n5. Groups\n6. Show Favorites\n7. Quit')
	   

	def __create_contact(self):
		
		'''
		This method instansiates a contact class, runs the create contact method on it,
		and appends the contact to the contact_list instance
		'''
		new_contact = Contact()
		new_contact.create_contact()
		Group.static_add_to_group(new_contact, self.__contact_list)
		self.__contact_list.append_contact(new_contact)


	def __show_groups(self):
		Group.static_display_and_add_groups(self.__contact_list)
		

	def __read_from_json(self):

		'''
		This method opens our contactList.json file, using the imported json library, it
		parses an array from the file, which contains two dictionaries: groups and conttacts
		from these, using the create_group_from_json method and the create_contact_from_json method
		these classes are instansiated and stored in the correct place.
		'''
		   
		with open("./data/contactList.json", "r") as jsonPath:
			jsonFile = json.load(jsonPath)
			imported_group_list = jsonFile[0]['groups']
			imported_contact_list = jsonFile[0]['contacts']

			for json_group in imported_group_list:
				imported_group = Group()
				imported_group.create_group_from_json(json_group)
				self.__contact_list.append_groups(imported_group)
					
			for json_contact in imported_contact_list:
				imported_contact = Contact()
				imported_contact.create_contact_from_json(json_contact)
				self.__contact_list.append_contact(imported_contact)
				for existing_group in self.__contact_list.get_groups():
					existing_group.append_contact_from_json(imported_contact)
			jsonPath.close()    

						
	def __search_contact_list(self):
		self.__contact_list.search()
	def __show_contact_list(self):
		self.__contact_list.display_contacts()

	def __show_favorites(self):
		print('Your Favorites:')
		self.__favorite_list.display_contacts()
	
	def __loop_reset_logic(self):
		self.__favorite_list.calculate_favorites(self.__contact_list.get_contacts())


if __name__ == '__main__':
	ContactBook()