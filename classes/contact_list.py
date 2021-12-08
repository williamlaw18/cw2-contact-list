class main:
    def __init__(self, json_file):
        self.__contact_list = []
        self.__groups = []
        self.__json_file = json_file


# private methods

    def __import_from_json(self):
            pass

    def __save_to_json(self):
            pass

    def __sort_key(self, element):
            return element.contacts['name'][0]



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
                    print(contact.contacts['name'].capitalize())

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


        
