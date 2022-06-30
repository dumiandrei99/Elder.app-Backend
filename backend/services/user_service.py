from backend.repositories.user_repository import UserRepository
from backend.dtos.user_dto import UserDTO
from backend.serializers.standalone.user_serializer import UserSerializer
from backend.repositories.verification_code_repository import VerificationCodeRepository
from backend.serializers.standalone.verification_code_serializer import VerificationCodeSerializer
from ..validators.registration_validator import RegistrationValidator
from ..validators.verification_code_validator import VerificationCodeValidator
from ..validators.login_validator import LoginValidator
from ..validators.email_validator import EmailValidator
from ..validators.update_profile_picture_validator import UpdateProfilePictureValidator
from ..validators.change_password_validator import ChangePasswordValidator
from django.contrib.auth.hashers import make_password, check_password
from email.message import EmailMessage
import jwt, datetime, random, string, os, smtplib, time, threading

class UserService:

    def __devalidate_verification_code(self, verification_code):
        # sleep for 5 minutes before deleting the verification code from the db
        time.sleep(5 * 60)
        print("done")
        verification_code.delete()

    def __send_verification_email(self, email_receiver, verification_code):
        email_sender = "dumitrescu549@gmail.com"
        password = os.environ.get('EMAIL')
        
        email_content = "Password recovery verification code: " + verification_code
        email_content += "\nBe aware, this code is available for only 5 minutes !"
        
        email_message = EmailMessage()
        email_message['Subject'] = "Elder.app - Password Recovery Verification Code"
        email_message['From'] = email_sender
        email_message['To'] = email_receiver
        email_message.set_content(email_content)
        
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email_sender, password)
        server.send_message(email_message)
        server.quit()

    def user_register(self, data):
        registration_validator = RegistrationValidator()
        is_data_validated = registration_validator.validate_registration(data)

        # convert the username and email to lowercase, as they should not be case sensitive
        data['username'] = data['username'].casefold()
        data['email'] = data['email'].casefold()

        if is_data_validated != None:
            return is_data_validated
        
        # data in the serializer and in DB doesn't have the 're-password' field, it's just a UI check to make sure the user entered his password correctly
        # so we delete this data and it's index
        del data['re_password']

        # hash the password so nobody can see it in plain text in DB
        data['password'] = make_password(data['password'])

        user = UserRepository.search_user_by_username(data['username'])
        
        # user variable is not None when a person tries to register an account with an username that already exists
        if user is not None:
            response = {
                "message": "This username already exists!",
                "status": '248'
            }
            return response
        
        user = UserRepository.search_user_by_email(data['email'])
        
        # user variable is not None when a person tries to register an account with an email that is already associated to another account
        if user is not None:
            response = {
                "message": "This email is associated with another account!",
                "status": '249'
            }
            return response

        serializer = UserSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            response = {
                'message': 'You have registered your account with success !',
                'status': '200'
            }
            return response
        else:
            response = {
                'message': serializer.errors,
                'status': '230'
            }
            return response
    

    def user_login(self, data, request):
        login_validator = LoginValidator()
        is_data_validated = login_validator.validate_login(data)
        
        # convert the username to lowercase, as it should not be case sensitive
        data['username'] = data['username'].casefold()

        if is_data_validated != None:
            return is_data_validated
        
        user = UserRepository.search_user_by_username(data['username'])

        # user variable is None when a person tries to log-in with a username that doesn't map to any user in DB
        if user is None:
            response = {
                "message": "User does not exist!",
                "status": '248'
            }
            return response
        
        if not check_password(data['password'], user.password):
            response = {
                "message": "The password you have entered is not correct!",
                "status": '249'
            }
            return response
        
        # at this point, the user's credentials are checked and we create and send as response the JWT Token
        payload = {
            'username': user.username,
            'expiration': str(datetime.datetime.utcnow() + datetime.timedelta(minutes=60)),
            'iat': datetime.datetime.utcnow()
        }

        # transform the logged-in user to a DTO that we send to the frontend

        userDTO = UserDTO(user, request)

        token = jwt.encode(payload, 'secret', algorithm='HS256')

        # we check if this is the user's first login and if so, we set the is_first_login field in the DB to False and 
        # return the fact that this is the user's first login
        if user.is_first_login == True :      
            UserRepository.set_first_login_to_false(user)
            # set it to true in order to return to the frontend the fact that this was the user's first login
            user.is_first_login = True

        
        response = {
            'token': token,
            'user': userDTO.Dictionary_UserDTO(),
            'status': '200'
        }

        return response


    def get_authenticated_user(self, token):

        if not token:
            response = {
                'message': 'User is not authenticated !',
                'status': '403 - forbidden'
            }
        else: 
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
            user = UserRepository.search_user_by_username(payload['username'])
            if not user:
                response = {
                'message': 'User is not authenticated !',
                'status': '403 - forbidden'
            }
            else:
                serializer = UserSerializer(user)
                response = serializer.data

        return response

    def generate_verification_code(self, data): 
        email_validator = EmailValidator()
        email = data['email']

        # check if the email is valid
        is_email_valid = email_validator.validate_email(email)

        # return error message if it's not
        if is_email_valid != None:
            return is_email_valid
        
        # check if the email provided by the user is associated to any account
        user = UserRepository.search_user_by_email(email)

        # user variable is  None when a person tries to recover a password with an email that is not associated to any account
        if user is None:
            response = {
                "message": "This email is not associated with any account!",
                "status": '250'
            }
            return response

        # generate the verification code with a length of 6 characters and save it in the data array
        verification_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 6)) 
        data['verification_code'] = verification_code

        # add the user's UUID to the data array
        data['uuid_user'] = user.uuid

        # instantiate the serializer
        serializer = VerificationCodeSerializer(data = data)

        # verify if the user already generated another verification code without waiting for the other one to expire
        verification_code = VerificationCodeRepository.search_by_email(email)
        
        # if so, delete the old verification code from the DB before generating and inserting the new one
        if verification_code != None:
            verification_code.delete()

        # save the verification code in the DB
        if serializer.is_valid(): 
            serializer.save()
        else: 
            response = {
                "message": "Couldn't generate the verification code! Contact the support team!",
                "status": "500"
            }
            return response

        # retrieve the verification code back after deleting it from the DB, in order to use it for sending the email
        verification_code = VerificationCodeRepository.search_by_email(email)

        # send an email with the verification code to the user
        self.__send_verification_email(email, verification_code.verification_code)
        
        # make the verification code unavailable after 5 minutes (delete it from the DB)
        devalidate_thread = threading.Thread(target=self.__devalidate_verification_code, args=[verification_code])
        devalidate_thread.start()

        response = {
            "message": "Verification code generated! Check your email!",
            "status": '200'
        }

        return response
    
    def check_verification_code(self, data):
        verification_code_validator = VerificationCodeValidator()
        is_data_valid = verification_code_validator.validate_verification_code_data(data)

        if is_data_valid != None:
            return is_data_valid
        
        user_via_email = UserRepository.search_user_by_email(data['email'])

        if user_via_email is None:
            response = {
                "message": "You have to generate a verification code first !",
                "status": "254"
            }
            return response

        user_via_verification_code = VerificationCodeRepository.search_by_verification_code(data['verification_code'])

        if user_via_verification_code is None:
            response = {
                "message": "Invalid verification code",
                "status": "254"
            }
            return response
            
        if user_via_email.uuid != user_via_verification_code.uuid_user_id:
            response = {
                "message": "Wrong verification code!",
                "status": "253"
            }
            return response
        
        response = {
            "status": "200"
        }
        return response

    def update_profile_picture(self, data):
        # validate data
        update_profile_picture_validator = UpdateProfilePictureValidator()
        is_data_valid = update_profile_picture_validator.validate_profile_picture(data)

        if is_data_valid != None:
            return is_data_valid
        
        username = data['username']
        user = UserRepository.get_user_by_username(username)
        profile_picture = data['profile_picture']

        print(profile_picture)

        response = UserRepository.set_profile_picture(user, profile_picture)

        return response

    def change_password(self, data):
        change_password_validator = ChangePasswordValidator()
        is_data_valid = change_password_validator.validate_change_password(data)

        if is_data_valid != None:
            return is_data_valid
        
        change_password_type = data['type']

        if change_password_type == 'change_password':
            username = data['username']
            user = UserRepository.get_user_by_username(username)
            old_password = data['old_password']
            new_password = data['new_password']

            if old_password == new_password:
                response = {
                    "message": "Your new password must be different from the old one!",
                    "status": "253"
                }
                return response

            if not check_password(old_password, user.password):
                response = {
                    "message": "Your old password is not correct!",
                    "status": '249'
                }
                return response

            if len(new_password) < 6:
                response = {
                    "message": "Your new password is too short",
                    "status": "253"
                }
                return response

            new_password = make_password(new_password)
            UserRepository.save_new_password(user, new_password)
            return "Password successfully changed !"
    
        if change_password_type == 'reset_password':
            new_password = data['new_password']

            if len(new_password) < 6:
                response = {
                    "message": "Your new password is too short",
                    "status": "253"
                }
                return response

            # check if the verification code is still available
            verification_code_data = data['verification_code']
            verification_code = VerificationCodeRepository.search_by_verification_code(verification_code_data)
            
            if not verification_code:
                response = {
                    "message": "The code you have entered expired!",
                    "status": "253"
                }
                return response
            
            user_uuid = VerificationCodeRepository.get_user_uuid_by_verification_code(verification_code_data)
            username = UserRepository.get_username_by_uuid(user_uuid)
            user = UserRepository.get_user_by_username(username)

            new_password = make_password(new_password)
            UserRepository.save_new_password(user, new_password)

            return "Password successfully changed !"
