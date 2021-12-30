
from classes.list_base import ListBase

class Favorites(ListBase):
    def __init__(self):
        super().__init__()
        self.__threshold = 2
        self.__name = 'Favorites'
        self.__description = 'List of contacts you have contacted the most'

    def __sort_contact_key(self, element):
        return element.get_contacted_counter()
        
    def __sort_contacts(self):
        
        #This methods sorts contacts by how many times they have been contacted 
        
        self.contact_list.sort(key = self.__sort_contact_key)

    def add_to_favorites(self, contact):
        if contact not in self.contact_list:
            self.contact_list.append(contact)
            print(contact.get_contact_name().capitalize() + ' added to favorites!' )
            self.__sort_contacts()

    def calculate_favorites(self, contact_list):

        '''
        This static method accepts a contact list as a parameter, it starts by working out the average amount of
        times contacts have been contacted, then any contact that has been contacted more than the average gets added.
        There is an option for a threshold as well, making it so that the first person to get contacted doesn't automatically
        get added to favorites.
        '''

        sum = 0
        for contact in contact_list:
            sum += contact.get_contacted_counter()
        
        if len(contact_list) > 0 :
            average_contact_amount = sum / len(contact_list)

            for contact in contact_list:
                if contact.get_contacted_counter() > average_contact_amount + self.__threshold:
                    self.add_to_favorites(contact)

    def set_threshold(self, threshold):
        self.__threshold = threshold

    def get_threshold(self):
        return self.__threshold

    


        
