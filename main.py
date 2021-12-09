import json

from classes import contact
from classes import contact_list



class ContactBook:
    def __init__(self):
       self.__contact_list = contact_list.main()
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
          elif(user_input == '4'):
              print('quiting program')
              break
          else:
              print('Sorry, input not recognised ')
              

    def __show_menu(self): 
        '''
        This method doesn't take any arguments, it just shows the menu as a printed string
        '''
        print('1. Menu 2. Create Contact 3.Show Contacts 4. Quit')
       

    def __create_contact(self):

        '''
        This method instansiates a contact class, runs the create contact method on it,
        and appends the contact to the contact_list instance
        '''
        new_contact = contact.main()
        new_contact.create_contact()
        self.__contact_list.append_contact(new_contact)

     
    def __read_from_json(self):
            print('hello from this sexy method')
            with open("./data/contactList.json", "r") as jsonPath:
                    jsonFile = json.load(jsonPath)
                    for json_contact in jsonFile:
                        new_contact = contact.main()
                        new_contact.create_contact_from_json(json_contact)
                        self.__contact_list.append_contact(new_contact)

                        


    def __show_contact_list(self):
      self.__contact_list.get_contacts()


ContactBook()