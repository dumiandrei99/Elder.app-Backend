class GroupsAUserIsInValidator: 

    def validate(self, data):
        if 'username' not in data.keys():
            response = {
                'message': 'The username field must be completed',
                'status': '280'
            }
            return response
        return None