import json

class main:
    def __init__(self):
        self.__contact_list = []
        self.__groups = []


# private methods

    def __import_from_json(self):
            pass

    def __save_to_json(self):
            pass

    def __sort_key(self, element):
            return element.contact_details['name'][0]



    def __sort_contacts(self):

            '''
            This method sorts the contact list into alphabetical order 
            by using a key function (__sort_key) that returns the name of the contact and passing
            this to the inbuilt python sort method. This will be run everytime a contact is added
            '''
            self.__contact_list.sort(key = self.__sort_key)


# public methods

    def get_contacts(self):
            '''
            Prints contacts, allows you to be able to select contact to run the edit method on
            '''
            for contact in self.__contact_list:
                    print(contact.contact_details)

    def append_contact(self, contact):
            '''
            This appends a contact to the list, and then runs the sort method
            
            '''
            self.__contact_list.append(contact)
            self.__sort_contacts()

            pass

    def search(self):
            '''
            Provides functionality to search contact by various options 
            
            '''
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

            for contact in self.__contact_list:
                   if contact.contacts[search_attribute] == sanitised_search_term:
                           print(contact.contacts)

    def delete_contact(self, contact):
            '''
            Deletes Contact
            '''


    def add_group(self, group_name):
            '''
            Allows user to create a group, should this be a class??
            '''
        
	
    def delete_group(self, group):
            '''
            Allows user to delete a group
            '''
            pass






        
