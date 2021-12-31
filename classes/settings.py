import helper_methods.helper as helper


class Settings:
	def __init__(self, contact_list, favorite_list):
		self.__contact_list = contact_list
		self.__favorite_list = favorite_list
		pass


	def show_settings(self):
		print('1. Contact Settings \n2. Favourite Settings \n3. Return to menu')
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


	def __show_settings_contacts(self):
			print('1. Clear All Contacts \n2. Sort By \n3. Return to menu')
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
		print('1. Set Favourite Threshold \n2. Clear Favourites \n3. Return to menu')
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


	def __settings_clear_contacts(self, list):
		list.clear_all_contacts()
		print(f'{helper.format_title(list.get_name())} successfully cleared')
  

	def __settings_favourites_threshold(self):
		print('please enter how many times a contact is contacted before being listed as a favourite compared to the average')
		print('The current threshold is ' +  str(self.__favorite_list.get_threshold()))
		while True:
			try:
				user_input = int(input())
				self.__favorite_list.set_threshold(user_input)
				print('Threshold successfully changed to ' + str(user_input))
				break
			except ValueError:
				print('Please enter a valid number')
				
    
	def __settings_sort_by(self):
			sort_by_fields = ['first_name','second_name', 'postcode','email']
			for i,field in enumerate(sort_by_fields): #gives index of item in the list
				field_number = str(i + 1)
				print(field_number + ': ' + helper.format_title(field,True))
			print('enter the number of the fields you would like to sort by')
   
			while True:
				try:
					userinput = int(input()) - 1
					chosen_field = sort_by_fields[userinput]
					self.__contact_list.sort_by_identifier = chosen_field
					print('now sorting by ' + helper.format_title(chosen_field))
					break
				except:
					print('invalid input, please try again')
