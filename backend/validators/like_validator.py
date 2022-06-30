class LikeValidator: 

    def validate_login(self, data):
        if 'username' not in data.keys():
            response = {
                'message': 'The username field must be completed',
                'status': '246'
            }
            return response
        
        if 'post_uuid' not in data.keys():
            response = {
                'message': 'The post_uuid field must be completed',
                'status': '247'
            }
            return response
        
        return None