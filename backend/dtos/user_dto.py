
class UserDTO:
    def __init__(self, user, request) -> None:
        self.username = user.username
        self.firstname = user.first_name
        self.lastname = user.last_name
        self.is_first_login = user.is_first_login
        if user.profile_picture != 'null':
            profile_picture = request.build_absolute_uri(user.profile_picture.url)
        else: 
            profile_picture = None
        self.profile_picture = profile_picture
    
    def Dictionary_UserDTO(self):
        userDTO_dict = {
            'username': self.username,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'is_first_login': self.is_first_login,
            'profile_picture': self.profile_picture
        }

        return userDTO_dict