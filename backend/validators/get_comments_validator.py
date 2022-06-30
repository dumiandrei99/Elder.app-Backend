class GetCommentsValidator: 

    def validate_get_comments(self, data):
        if 'post_uuid' not in data.keys():
            response = {
                'message': 'The post_uuid field must be completed',
                'status': '247'
            }
            return response
        return None