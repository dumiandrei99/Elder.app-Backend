from ..models.standalone.user_model import User

class UserRepository:
    def search_user_by_username(username):
        return User.objects.filter(username=username).first()
    
    def search_user_by_email(email):
        return User.objects.filter(email=email).first()
    
    def get_user_by_username(username):
        return User.objects.filter(username=username).first()
        
    def get_uuid_by_username(username):
        return User.objects.filter(username=username).first().uuid

    def set_first_login_to_false(user):
        user.is_first_login = False
        return user.save()

    def get_username_by_uuid(uuid):
        return User.objects.filter(uuid=uuid).first().username

    def set_profile_picture(user, profile_picture):
        user.profile_picture = profile_picture
        return user.save()
    
    def get_profile_picture_by_username(username):
        return User.objects.filter(username=username).first().profile_picture

    def save_new_password(user, password):
        user.password = password
        return user.save()