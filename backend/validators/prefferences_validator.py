from rest_framework.parsers import JSONParser

class PrefferencesValidator: 

    def validate_prefferences(self, data):
        if 'username' not in data.keys():
            response = {
                'message': 'The username field must be completed',
                'status': '266'
            }
            return response
        
        if 'prefferences' not in data.keys():
            response = {
                'message': 'The password field must be completed',
                'status': '267'
            }
            return response
        
        # we are counting if at least one prefference has been selected
        count_for_false = 0        
        prefferences = data['prefferences']
        for prefference, prefference_value in prefferences.items():
            if prefference_value == False:
                count_for_false = count_for_false + 1
        
        # if all the prefferences are set to false, we return an error message
        if count_for_false == 10:
            response = {
                'message': 'At least one prefference must be selected !',
                'status': '268'
            }
            return response
            
        return None