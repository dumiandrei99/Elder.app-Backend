import re

class EmailValidator:

    def __is_email_valid(self, email):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

        if re.fullmatch(regex, email):
            return True
        return False

    def validate_email(self, email):
        if self.__is_email_valid(email) != True:
            response = {
                'message': 'Email is not valid',
                'status': '243'
            }
            return response
        
        return None