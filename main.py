import json
import helper_methods.helper as helper
from classes.contact import Contact
from classes.group import Group
from classes.contact_list import ContactList
from classes.favorites import Favorites
from classes.settings import Settings
from classes.import_export import ImportExport
from classes.save import Save

class ContactBook:
	def __init__(self):
		self.__save = Save()
		self.__contact_list = ContactList()
		self.__favorite_list = Favorites()
		self.__settings = Settings(self.__contact_list, self.__favorite_list)
		self.__import_export = ImportExport(self.__contact_list)
		self.__import_export.read_from_json()
		self.__run_program_loop()
			
	   
	def __run_program_loop(self):
		
	
		'''
		This method runs the main program loop. This waits on the user input, which is then entered into
		a match case statement that will run the particular methods chosen by the user
	  
		'''
		
		print("Welcome to your contacts!")

		while True:

			#Uses the save class to take a snapshot of the current state of contacts/groups

			self.__save.create_snapshot(self.__contact_list.get_contacts(), self.__contact_list.get_groups())
			
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
					self.__show_settings()
				case '8':
					print('Quiting program, Goodbye!')
					break
				case _:
					print('Sorry, input not recognised ')
			
			self.__loop_reset_logic()
		


	def __show_menu(self): 

		'''
		This method doesn't take any arguments, it just shows the menu as a printed string
		'''
		print('1. Menu\n2. Create Contact\n3. Show Contacts\n4. Search Contacts\n5. Groups\n6. Show Favorites\n7. Settings\n8. Quit')
	   

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
							
	def __search_contact_list(self):
		self.__contact_list.search()

	def __show_contact_list(self):
		self.__contact_list.display_contacts()

	def __show_favorites(self):
		print('Your Favorites:')
		self.__favorite_list.display_contacts()

	def __show_settings(self):
		self.__settings.show_settings()
	
	def __loop_reset_logic(self):
		'''
		This logic runs every time the program loops, it detects if the favorites need to be updated
		and if there are any changes that need to be saved to JSON.
		'''

		self.__favorite_list.calculate_favorites(self.__contact_list.get_contacts())
		need_to_save = self.__save.compare_snapshot(self.__contact_list.get_contacts(), self.__contact_list.get_groups())
		if(need_to_save):
			self.__import_export.save_to_json()
			


if __name__ == '__main__':
	ContactBook()