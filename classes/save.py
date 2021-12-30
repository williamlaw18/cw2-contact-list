
from classes.group import Group
import copy


class Save:
    def __init__(self):
        self.previous_state = {
            "group_list": [],
            "contact_list":[]
        }


    def create_snapshot(self, contact_list, group_list):
        previous_group_list = []
        previous_contact_list = []

        for contact in contact_list:
            previous_contact_list.append(self.__format_for_comparison(contact, True))

        for group in group_list:
            previous_group_list.append(self.__format_for_comparison(group, False))

        self.previous_state['group_list'] = previous_group_list
        self.previous_state['contact_list'] = previous_contact_list


    def compare_snapshot(self,contact_list, group_list):
        '''
        This method compares the current state of the contact list and group list, If there has been
        any changes, it will return true. This boolean will be used to decide wether or not to save to 
        json after each program loop. This method would start by storing the equality between each lists as 
        a boolean to make sure that the if statement is readable
        '''
        current_contact_list = []
        current_group_list = []

        for contact in contact_list:
            current_contact_list.append(self.__format_for_comparison(contact, True))

        for group in group_list:
            current_group_list.append(self.__format_for_comparison(group, False))

        is_group_equal = self.previous_state["group_list"] == current_group_list
        is_contact_equal = self.previous_state["contact_list"] == current_contact_list

        if is_group_equal and is_contact_equal:
            return False
        else:
            print('Saving Changes')
            return True
       

    def __format_for_comparison(self, item, contact_flag):

        formated_dictionary = {}

        if(contact_flag):
            formated_dictionary = copy.deepcopy(item.get_contact_details())
            formated_dictionary['group_ID'] = copy.deepcopy(item.get_group_ids())
        else:
            formated_dictionary = copy.deepcopy(item.get_group_dict())

        return formated_dictionary






        
        

    

