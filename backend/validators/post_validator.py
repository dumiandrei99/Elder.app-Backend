class PostValidator: 

    def validate_post(self, data):
        if 'post_user' not in data.keys():
            response = {
                'message': 'The username field must be completed',
                'status': '246'
            }
            return response

        if 'post_description' not in data.keys():
            response = {
                'message': 'The post description field must be completed',
                'status': '246'
            }
            return response
        
        if 'post_group' not in data.keys():
            response = {
                'message': 'The post group field must be completed',
                'status': '246'
            }
            return response
        
        if 'post_image' not in data.keys():
            response = {
                'message': 'The post image field must be completed',
                'status': '246'
            }
            return response
        

        if len(data['post_description']) < 1:
            response = {
                'message': 'You have to write a post description!',
                'status': '246'
            }
            return response

        if len(data['post_group']) < 1:
            response = {
                'message': 'Ypu have to select a group to post in!',
                'status': '246'
            }
            return response
        
        return None