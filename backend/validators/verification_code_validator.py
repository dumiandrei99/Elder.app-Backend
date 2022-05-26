class VerificationCodeValidator:
    def validate_verification_code_data(self, data):
      
        if 'email' not in data.keys():
            response = {
                'message': 'An email must be provided!',
                'status': '251'
            }
            return response
        
        if 'verification_code' not in data.keys():
            response = {
                'message': 'A verification code must be provided!',
                'status': '252'
            }
            return response
        
        if len(data['email']) < 1:
            response = {
                'message': 'Email filed is required!',
                'status': '251'
            }
            return response
                
        if len(data['verification_code']) < 1:
            response = {
                'message': 'Verification code filed is required!',
                'status': '251'
            }
            return response
        
        return None