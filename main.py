import json
from classes.contact import Contact
from classes.group import Group
from classes.contact_list import ContactList

class ContactBook:
    def __init__(self):
       self.__contact_list = ContactList()
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

          if(user_input == '1'):
              self.__show_menu()
          elif(user_input == '2'):
              self.__create_contact()
          elif(user_input == '3'):
              self.__show_contact_list()
          elif(user_input == "4"):
              self.__search_contact_list()
          elif(user_input == '5'):
              self.__show_groups()
          elif(user_input == '6'):
              print('quiting program')
              break
          else:
              print('Sorry, input not recognised ')
              

    def __show_menu(self): 

        '''
        This method doesn't take any arguments, it just shows the menu as a printed string
        '''
        print('1. Menu\n2. Create Contact\n3. Show Contacts\n4. Search Contacts\n5. Groups\n6. Exit')
       

    def __create_contact(self):
        
        '''
        This method instansiates a contact class, runs the create contact method on it,
        and appends the contact to the contact_list instance
        '''
        new_contact = Contact()
        new_contact.create_contact()
        self.__adding_to_group_options(new_contact)
        self.__contact_list.append_contact(new_contact)

    def __adding_to_group_options(self, contact):
        print(f'Enter Y to add {contact.get_contact_details()["name"]} to a group, or any other key to continue')
        user_input = input()
        if(user_input.lower() == 'y'):
            self.__add_to_groups(contact)
        else:
            return    


    def __add_to_groups(self, contact):
        group_list = self.__contact_list.list_groups()
        print('Select the number of the group you want to add to, or press A to create a new group')
        while True:
            try:
                user_input = input()
                if user_input.lower() == 'a':
                    new_group = Group()
                    new_group.create_group_from_user_imput()
                    new_group.append_contact(contact)
                    self.__contact_list.append_groups(new_group)
                    break
                else:
                    user_selection = int(user_input) - 1
                    group_list[user_selection].append_contact(contact)
                    print('Succesfully added to group')
                    break
            except:
                print('Input not recognised') 



    def __show_groups(self):

        '''
        This method lists out all the groups
        
        '''
        group_list = self.__contact_list.list_groups()
        print('Enter the number of the group you would like to view, or press A to add a new one')
        while True:
            try:
                user_input = input()
                if user_input.lower() == 'a':
                    new_group = Group()
                    new_group.create_group_from_user_imput()
                    self.__contact_list.append_groups(new_group)
                    break
                else:
                    user_selection = int(user_input) - 1
                    group_list[user_selection].display_group()
                    #Perhaps I could add the ability to loop through contacts and choose to add to this group
                    break
            except:
                print('input not recognised')


    def __read_from_json(self):
           
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




if __name__ == '__main__':
    ContactBook()