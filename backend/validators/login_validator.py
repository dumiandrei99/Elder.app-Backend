class LoginValidator: 

    def validate_login(self, data):
        if 'username' not in data.keys():
            response = {
                'message': 'The username field must be completed',
                'status': '246'
            }
            return response
        
        if 'password' not in data.keys():
            response = {
                'message': 'The password field must be completed',
                'status': '247'
            }
            return response
        
        return None