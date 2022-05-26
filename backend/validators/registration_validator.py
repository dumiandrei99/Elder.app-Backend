from datetime import date
import re


class RegistrationValidator:
    
    def __is_email_valid(self, email):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

        if re.fullmatch(regex, email):
            return True
        return False
    
    def __is_date_of_birth_valid(self, date_of_birth):
        regex = r'\b(?:0[1-9]|[12][0-9]|3[01])[-/.](?:0[1-9]|1[012])[-/.](?:19\d{2}|20[01][0-9]|2020)\b'

        if re.fullmatch(regex, date_of_birth):
            return True
        return False
    
    def __is_user_too_young(self, date_of_birth):
        # transform the string date of birth to 'date' data type in order to apply the formula for age calculation
        split_date_of_birth = date_of_birth.split('/')

        year_of_birth = split_date_of_birth[2]
        month_of_birth = split_date_of_birth[1]
        day_of_birth = split_date_of_birth[0]

        date_of_birth = date(int(year_of_birth), int(month_of_birth), int(day_of_birth))

        # apply formula of age calculation, considering that int(True) returns 1 and int(False) returns 0
        today = date.today()
        users_age = today.year - date_of_birth.year - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))

        if users_age < 60:
            return True
        return False

    def validate_registration(self, data):
        
        if 'username' not in data.keys():
            response = {
                'message': 'The username field must be completed',
                'status': '231'
            }
            return response
        
        
        if 'first_name' not in data.keys():
            response = {
                'message': 'The first name field must be completed',
                'status': '232'
            }
            return response

            
        if 'last_name' not in data.keys():
            response = {
                'message': 'The last name field must be completed',
                'status': '233'
            }
            return response
        
        if 'password' not in data.keys():
            response = {
                'message': 'The password field must be completed',
                'status': '234'
            }
            return response

        if 're_password' not in data.keys():
            response = {
                'message': 'The re-password field must be completed',
                'status': '235'
            }
            return response

        
        if 'email' not in data.keys():
            response = {
                'message': 'The email field must be completed',
                'status': '236'
            }
            return response

            
        if 'date_of_birth' not in data.keys():
            response = {
                'message': 'The date of birth field must be completed',
                'status': '237'
            }
            return response

        if len(data['username']) < 5:
            response = {
                'message': 'Username must have at least 5 characters',
                'status': '238'
            }
            return response
        
        if len(data['first_name']) < 2:
            response = {
                'message': 'First name must have at least 2 characters',
                'status': '239'
            }
            return response

        if len(data['last_name']) < 2:
            response = {
                'message': 'Last name must have at least 2 characters', 
                'status': '240'
            }
            return response
            
        if len(data['password']) < 6:
            response = {
                'message': 'Password must have at least 6 characters',
                'status': '241'
            }
            return response
        
        if data['password'] != data['re_password']:
            response = {
                'message': 'Passwords not matching',
                'status': '242'
            }
            return response 

        if self.__is_email_valid(data['email']) != True:
            response = {
                'message': 'Email is not valid',
                'status': '243'
            }
            return response

        if self.__is_date_of_birth_valid(data['date_of_birth']) != True:
            response = {
                'message': 'Date of birth should follow this format: DD/MM/YYYY',
                'status': '244'
            }
            return response
        
        if self.__is_user_too_young(data['date_of_birth']):
            response = {
                'message': 'This app is for seniors only! You are too young to join our platform. Only members of at least 60 are allowed.',
                'status': '245'
            }

            return response

        return None