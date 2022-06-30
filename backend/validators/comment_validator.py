class CommentValidator: 

    def validate_comment(self, data):
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
        
        if 'comment' not in data.keys():
            response = {
                'message': 'The comment field must be completed',
                'status': '247'
            }
            return response
        
        if len(data['comment']) < 1: 
            response = {
                'message': 'The comment field must have at least 1 character',
                'status': '247'
            }
            return response

        return None