class AddUserInGroupValidator: 

    def validate_user_and_group(self, data):
        if 'username' not in data.keys():
            response = {
                'message': 'The username field must be completed',
                'status': '270'
            }
            return response
        
        if 'group_name' not in data.keys():
            response = {
                'message': 'The password field must be completed',
                'status': '271'
            }
            return response
        
        return None