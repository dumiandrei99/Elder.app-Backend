class ChangePasswordValidator: 

    def validate_change_password(self, data):
        if 'type' not in data.keys():
            response = {
                'message': 'The type field must be completed',
                'status': '246'
            }
        
        if data['type'] == 'change_password':
            if 'username' not in data.keys():
                response = {
                    'message': 'The username field must be completed',
                    'status': '246'
                }
                return response

            if 'old_password' not in data.keys():
                response = {
                    'message': 'The old password field must be completed',
                    'status': '246'
                }
                return response

            if 'new_password' not in data.keys():
                response = {
                    'message': 'The new password field must be completed',
                    'status': '246'
                }
                return response
            
            if len(data['old_password']) < 1:
                print(data['old_password'])
                response = {
                    'message': 'You must enter your old password',
                    'status': '246'
                }
                return response
            
            if len(data['new_password']) < 1:
                response = {
                    'message': 'You must enter your new password',
                    'status': '246'
                }
                return response

        if data['type'] == 'reset_password':
            if 'verification_code' not in data.keys():
                response = {
                    'message': 'The verification code field must be completed',
                    'status': '246'
                }
                return response

            if 'new_password' not in data.keys():
                response = {
                    'message': 'The new password field must be completed',
                    'status': '246'
                }
                return response
            
            if len(data['new_password']) < 1:
                response = {
                    'message': 'You must enter your new password',
                    'status': '246'
                }
                return response

        return None