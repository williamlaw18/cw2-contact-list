import helper_methods.helper as helper


class Settings:
	def __init__(self, contact_list, favorite_list):
		self.__contact_list = contact_list
		self.__favorite_list = favorite_list

#-------------------------- Public Methods --------------------------------
'''
	This method is used to navigate through the two options within the settings,
	the user can select to either go to the favourites settings or the contacts
	settings.  
 
'''

def show_settings(self):
	print("1. Contact Settings \n2. Favourite Settings \n3. Return to Menu")
	user_input = input()
	while True:
		match user_input:
				case '1':
					self.__show_settings_contacts()
					break
				case '2':
					self.__show_settings_favourites()
					break
				case '3':
					break

#-------------------------- Private Methods --------------------------------
'''
	Another match case was used within the contacts settings to see weather or not the user would 
	change the sort by settings or to clear the contacts list itself.  
 
'''
def __show_settings_contacts(self):
		print("1. Clear All Contacts \n2. Sort By \n3. Return to menu")
		user_input = input()
		while True:
			match user_input:
				case '1':
					self.__settings_clear_contacts(self.__contact_list)
					break
				case '2':
					self.__settings_sort_by()
					break
				case '3':
					break


def __show_settings_favourites(self):
	print("1. Set Favourite Threshold \n2. Clear Favourites \n3. Return to menu")
	user_input = input()
	while True:
		match user_input:
				case '1':
					self.__settings_favourites_threshold()
					break
				case '2':
					self.__settings_clear_contacts(self.__favorite_list)
					break
				case '3':
					break

'''
	When the clear contacts is initiated, all the contacts within the list are 
	cleared and a message is printed to the user for comfirmation that the 
	process was a success.
 
'''
def __settings_clear_contacts(self, list):
	list.clear_all_contacts()
	print(f"{helper.format_title(list.get_name())} successfully cleared.")

'''
	To change the favourites threshold, the user is first prompted to input the desired threshold 
	that they would like. this is then saved in the variable 'user_type' as an integer and later changed to the value 
	for the 'print(f"Threshold successfully changed to: {str(user_input)}.")'.  If the user inputs a value that is not 
 	recognised as an integer, the user will recieved a message prompting them to input a valid number.
 	
'''
def __settings_favourites_threshold(self):
	print("Please enter how many times a contact is contacted before being listed as a favourite compared to the average")
	print(f"The current threshold is: {str(self.__favorite_list.get_threshold())}.")
	while True:
		try:
			user_input = int(input())
			self.__favorite_list.set_threshold(user_input)
			print(f"Threshold successfully changed to: {str(user_input)}.")
			break
		except ValueError:
			print('Please enter a valid number')
			
'''
	When the user initiates the '__settings_sort_by(self)' a 'for' loop is used to give the index of the item within the list 
	each field taken from the 'sort_by_fields' is given a value from 1-3 for the user to pick.  A 'while' loop is then used to 
 	wait until the user input a correct value or else they will get a value error if its not 
	a valid value, or an index error if they try to access a field that does not exist.
 	
'''
def __settings_sort_by(self):
		sort_by_fields = ['first_name','second_name', 'postcode','email']
		for i,field in enumerate(sort_by_fields): 
			field_number = str(i + 1)
			print(f"{field_number}: {helper.format_title(field,True)}")
		print("Please enter the number of the field you would like to sort by")

		while True:
			try:
				userinput = int(input()) - 1
				chosen_field = sort_by_fields[userinput]
				self.__contact_list.sort_by_identifier = chosen_field
				print(f"Now sorting by: {helper.format_title(chosen_field)}")
				break
			except ValueError:
				print("Please enter a valid number")
			except IndexError:
				print('No field exists at that selection, please try again.')
