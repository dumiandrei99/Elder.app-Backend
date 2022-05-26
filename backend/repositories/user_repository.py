from ..models.standalone.user_model import User

class UserRepository:
    def search_user_by_username(username):
        return User.objects.filter(username=username).first()
    
    def search_user_by_email(email):
        return User.objects.filter(email=email).first()
    
    def get_uuid_by_username(username):
        return User.objects.filter(username=username).first().uuid

    def set_first_login_to_false(user):
        user.is_first_login = False
        return user.save()