
import re 
import constants.constant as constant
from classes.group import Group
import webbrowser
import helper_methods.helper as helper


class Contact:

	'''
	This class holds the contact blueprint, and the relevant logic required in 
	creating, removing, displaying and editing each contact.  The details are 
	stored in the __contact_details dictionary. 
	
	'''

	def __init__(self):
		self.__contact_details = {
			'first_name': None,
			'second_name': None,
			'phone': None,
			'email' : None,
			'house_name_or_number': None,
			'address_line_1': None,
			'address_line_2': None,
			'postcode': None,
		}

		# initialise group ID to be empty.
		self.__group_ids = []

		# amount of times contacted:
		self.__contacted_counter = 0

 
#-------------------------- Private Methods --------------------------------

	def __add_contact_field (self, field_type):
		'''
		This method fills out a individual contact detail field based on the
		field type passed to it.  It uses the format_title helper function 
		on the field_type to create a user-friendly version to output
		to the user in the input prompt.  Inside a while loop, the user input
		is passed through the relevant clean-up and validation logic.  If the
		check_field method returns true, the cleaned user input is saved to 
		the correct field.

		'''

		prompt_title = helper.format_title(field_type)

		while True:
			user_input = input('Enter ' + prompt_title + ': ' )
			sanitised_input = helper.strip_lowercase(user_input)
			validated = self.__check_field(sanitised_input, field_type)

			if(validated):
				self.__contact_details[field_type] = sanitised_input
				break


	def __check_field (self, user_input, field_type):

		'''
		Called by the __add_contact_field, this method accepts both a
		user inputed field value and a field type.  Using a match/case statement
		the user input is compared against the relevant reg-ex. If there is a match
		the method returns True, if it doesn't the method returns False and prompts
		the user to the problem.

		'''

		match field_type:
			case 'email':
				if(re.fullmatch(constant.EMAIL_REG_EX, user_input)):  
					return True
				else:
					print(f"{user_input} Is not a valid email address!")
					return False
			case 'phone':
				if(re.fullmatch(constant.PHONE_REG_EX, user_input)):
					return True
				else:
					print(f"{user_input} Is not a valid phone number!")
					return False
			case 'postcode':
				if(re.fullmatch(constant.POSTCODE_REG_EX, user_input)):
					return True
				else:
					print(f"{user_input} Is not a valid postcode!")
					return False
			case _: 
				return True
		pass


	def __create_contact_link(self, contact_method):
		'''
		Based on the contact method passed to it, this method creates
		either a mailto: or tel: prefix in order to generate a contact 
		link.  It also increaments the __contacted_counter in order to
		facilitate the calculation of favorites.
		'''

		prefix = ''
		if(contact_method == 'email'):
			prefix = 'mailto:'
		else:
			prefix = 'tel:'
		webbrowser.open(prefix + self.__contact_details[contact_method])
		self.__contacted_counter += 1


	def __add_to_group(self, contact_list):
		'''
		This method holds the logic to add the contact to a group.  First it 
		checks if it exists in any groups allready by calling the get_groups()
		method on the contact_list that is passed to it.
		If it exists in a group, this group is concatinated onto a string that is
		shown to the user. It then runs the static method on the Group object that
		allows a user to either add the contact to an existing group or to create a
		brand new one.
		
		'''


		group_list = contact_list.get_groups()
		group_name_list = []
		current_group_string = f"{helper.format_title(self.__contact_details['first_name'], True)} is currently in "

		if(len(self.__group_ids) == 0):
			current_group_string += "no groups, if you would like to add to one, enter 'Y', or 'X' to go back to the menu"
		else:
			for group in group_list:
				for conact_group_id in self.__group_ids:
					if(conact_group_id == group.get_group_id()):
						group_name_list.append(group.get_name())
		
			current_group_string += ' and '.join(group_name_list) + '.'
		print(current_group_string)

		Group.static_add_to_group(self, contact_list)

#-------------------------- Public Methods --------------------------------

	def create_contact(self):
		'''
		In order to create a new contact, this method loops through the 
		__contact_details dictionary and runs the __add_contact_field 
		method passing through the contact detail as a field_type.
		 This allows for validation of user input.
		'''
		
		for contact_detail in self.__contact_details:
			self.__add_contact_field(contact_detail)

		print(f"{self.__contact_details['first_name'].capitalize()} succesfully added!") 


	def create_contact_from_json(self, json_dict, group_ids):
		'''
		Recieving a dictionary of contact details and a list of group ids from json,
		this method uses for-in loops in order to fill out the needed details to 
		create a contact.
		'''

		for id in group_ids:
			self.__group_ids.append(id)
		
		for key in json_dict:
				self.__contact_details[key] = json_dict[key]


	def edit_contact(self):

		'''
		
		This method uses a loop to print out all the editable contact details located 
		on the self.__contact_details field.  It stores all the keys of the contact 
		details dictionary in a list which allows the user to pick the key they want 
		to change in the while loop.  This key is then passed to the
		self.__add_contact_field method which holds all the logic of entering the value 
		for that particular detail.
		
		'''

		old_name = helper.format_values(self.__contact_details['first_name'], 'name')
		keys = list(self.__contact_details.keys())

		print("Enter the number of the field you want to edit, or 'X' when done")


		for i, detail in enumerate(self.__contact_details):
			print(i+1, helper.format_title(detail, True))
		while True:
			user_input = input()
			if user_input.lower() == 'x':
				print("Finished Editing.")  
				break  
			else:
				try:
					user_selection = int(user_input) - 1
					selected_attribute = keys[user_selection]
					self.__add_contact_field(selected_attribute)
					changed_value = helper.format_values(self.__contact_details[selected_attribute], selected_attribute)
					print(f"{old_name}'s {helper.format_title(selected_attribute)} succesfully changed to: {changed_value}.")
					print("Select the attribute you want to change to carry on editing, or enter 'X' to exit.")

				except ValueError as e:
					# Called if user tries to enter a letter instead of a number.
					print("Please enter a valid number, or 'X' to exit.")
				except IndexError:
					# Called if user tries to enter a number thats outside of the range.
					print("No option exists at that selection, please try again.")


	def remove_contact(self, list_class):

		'''
		This method is called from the ListBase class in order to remove a contact.
		 As listbase is the parent class for the main contact list, the groups and 
		the favorites, the method stores which child this is in the list_type variable.
		 This is used in the match/case statement to make sure that the contact is being
		removed from the correct list and runs the relevent logic to that.

		'''

		list_type = type(list_class).__name__
		list_name = helper.format_title(list_class.get_name())

		print(f'Are you sure you want to remove {helper.format_title(self.__contact_details["first_name"], True)} from {list_name}?')

		user_input = input("Enter 'Y' to confirm. \n").lower()

		if(user_input == 'y'):
			list_class.contact_list.remove(self)

			match list_type:
				case 'ContactList':
					for group in list_class.get_groups():
						if self in group.contact_list:
							group.contact_list.remove(self)
					del(self)
				case 'Group':
					self.__group_ids.remove(list_class.get_group_id())
				case _:
					pass
					
					
			print("Contact removed.")


	def display_contact(self, contact_list):
		'''
		This method displays all the user details. The helper format_title method is 
		run on the detail key. This turns somthing like address_1 into Address 1
		for readability in the print statement. It also holds a menu so the user can
		choose what to do with the contact, running the relevant methods to edit,
		remove, add to group or create contact links.
	   
		'''
		for detail in self.__contact_details:
			detail_title = helper.format_title(detail, True)
			contact_detail = helper.format_values(self.__contact_details[detail], detail)
			print(f"{detail_title}: {contact_detail}")

		print(f"Contacted: {str(self.__contacted_counter)} times.")
		
		print("Enter '1' to email, '2' to phone, '3' to edit, '4' to add to group, '5' to remove, or 'X' to go back to the main menu:")
		user_input = input()

		match user_input:
			case '1':
				self.__create_contact_link('email')
				return
			case '2':
				self.__create_contact_link('phone')
				return
			case '3':
				self.edit_contact()
				return
			case '4':
				self.__add_to_group(contact_list)
			case '5':
				self.remove_contact(contact_list)
				return
			case _:
				return
		
#-------------------------- Getters and Setters --------------------------------

	def get_group_ids(self):
		return self.__group_ids


	def get_contact_details(self):
		return self.__contact_details  


	def get_contact_name(self):
		return self.__contact_details['first_name']  


	def set_group_id(self, id):
		self.__group_ids.append(id)
		

	def get_contacted_counter(self):
		return self.__contacted_counter    

	   




	 
		




	