from ..models.standalone.verification_code_model import VerificationCode

class VerificationCodeRepository:
    def search_by_email(email):
        return VerificationCode.objects.filter(email=email).first()
    
    def search_by_verification_code(verification_code):
        return VerificationCode.objects.filter(verification_code = verification_code).first()
