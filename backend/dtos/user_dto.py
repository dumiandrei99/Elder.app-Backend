
class UserDTO:
    def __init__(self, user) -> None:
        self.username = user.username
        self.firstname = user.first_name
        self.lastname = user.last_name
        self.is_first_login = user.is_first_login
    
    def Dictionary_UserDTO(self):
        userDTO_dict = {
            'username': self.username,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'is_first_login': self.is_first_login
        }

        return userDTO_dict