class UpdateProfilePictureValidator: 

    def validate_profile_picture(self, data):
        if 'username' not in data.keys():
            response = {
                'message': 'The username field must be completed',
                'status': '246'
            }
            return response
        
        if 'profile_picture' not in data.keys():
            response = {
                'message': 'The password field must be completed',
                'status': '247'
            }
            return response
        
        return None