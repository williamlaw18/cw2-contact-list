
import re 
import constants.constant as constant
import webbrowser
import helper_methods.helper as helper

class Contact:
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
        self.__group_id = None
        self.__group_name = None

        # amount of times contacted:
        self.__contacted_counter = 0

 
#-------------------------- Private Methods --------------------------------

    def __add_contact_field (self, field_type):
        '''
        runs while loop to add field, using sanitise field and check field methods. it only breaks and
        moves to next field when input has been validated.
        To avoid multiple if statements, a parsed and formated version of field_type is stored and then used 
        as a prompt in the input call
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
        uses a match/case statement to run user_input against regular expressions to validate
        '''

        match field_type:
            case 'email':
                if(re.fullmatch(constant.EMAIL_REG_EX, user_input)):  
                    return True
                else:
                    print(user_input + ' Is not a valid email address')
                    return False
            case 'phone':
                if(re.fullmatch(constant.PHONE_REG_EX, user_input)):
                    return True
                else:
                    print(user_input + ' Is not a valid phone number ')
                    return False
            case 'postcode':
                if(re.fullmatch(constant.POSTCODE_REG_EX, user_input)):
                    return True
                else:
                    print(user_input + ' Is not a valid postcode')
                    return False
            case _: 
                return True
        pass
       
    def __create_email_link(self):
        webbrowser.open("mailto: " + self.__contact_details['email'])
        self.__contacted_counter += 1

    def __create_tel_link(self):
        webbrowser.open("tel: " + self.__contact_details['phone'])
        self.__contacted_counter += 1

#-------------------------- Public Methods --------------------------------

    def create_contact(self):
        '''
        In order to create a new contact, this runs through the __contact_details dictionary
        and runs the __add_contact_field method. this allows for validation of user input
        '''
        
        for contact_detail in self.__contact_details:
            self.__add_contact_field(contact_detail)

        print(self.__contact_details['first_name'].capitalize() + ' Succesfully Added!') 

    def create_contact_from_json(self, json_dict):

        #uses a loop to pass params into method based on key strings
        for key in json_dict:
            if key == 'group_id':
                self.__group_id = json_dict[key]
            else:
                self.__contact_details[key] = json_dict[key]

    def edit_contact(self):
        print('Enter the number of the field you want to edit, press Y when done')

        old_name = helper.format_values(self.__contact_details['first_name'], 'name')

        for i, detail in enumerate(self.__contact_details):
            print(i+1, helper.format_title(detail, True))
        while True:
            user_input = input()
            if user_input.lower() == 'y':
                print('Finished Editing')  
                break  
            else:
                try:
                    keys = list(self.__contact_details.keys())
                    user_selection = int(user_input) - 1
                    selected_attribute = keys[user_selection]
                    self.__add_contact_field(selected_attribute)
                    changed_value = helper.format_values(self.__contact_details[selected_attribute], selected_attribute)
                    print(f"{old_name}'s {helper.format_title(selected_attribute)} succesfully changed to: {changed_value}.")
                    print("Select the attribute you want to change to carry on editing, or press Y to exit")

                except:
                    print('Sorry, input not recognised')

    def remove_contact(self, contact_list):

        print('Are you sure you want to remove this contact?')
        user_input = input('Type "Yes" if this is correct: ')
        match user_input:
            case 'Yes':
                contact_list.remove(self)

                json_object = helper.toJSON(contact_list)
                with open("./data/contacts.json", "w") as file:
                    file.write(json_object)

                print('Contact Removed')
                return
            case _:
                return

    def display_contact(self, contact_list):
        '''
        This method displays all the user details. The join, split and capitalise methods are run on the detail key.
        This turns somthing like address_1 into Address 1 for readability in the print statement.
        '''
        for detail in self.__contact_details:
            detail_title = helper.format_title(detail, True)
            contact_detail = helper.format_values(self.__contact_details[detail], detail)
            print(detail_title + ': ' + contact_detail)

        print("Contacted: " + str(self.__contacted_counter) + " times.")
        
        print('press 1 to email, press 2 to phone, 3 to edit, 4 to remove or any other character to go back to main menu:')
        user_input = input()

        match user_input:
            case '1':
                self.__create_email_link()
                return
            case '2':
                self.__create_tel_link()
                return
            case '3':
                self.edit_contact()
                return
            case '4':
                self.remove_contact(contact_list)
                return
            case _:
                return



#-------------------------- Getters and Setters --------------------------------

    def get_group_id(self):
        return self.__group_id

    def get_group_name(self):
        return self.__group_name 

    def get_contact_details(self):
        return self.__contact_details  

    def get_contact_name(self):
        return self.__contact_details['first_name']        

    def set_group_id(self, id):
        self.__group_id = id

    def get_contacted_counter(self):
        return self.__contacted_counter    

       




     
        




    