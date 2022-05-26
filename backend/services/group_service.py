from ..validators.prefferences_validator import PrefferencesValidator
from ..repositories.user_repository import UserRepository
from ..repositories.prefference_repository import PrefferenceRepository
from ..repositories.user_prefference_repository import UserPrefferenceRepository
from ..serializers.group_related.user_prefference_serializer import UserPrefferenceSerializer

class GroupService:
    def save_prefferences(self, data):
        
        prefferences_validator = PrefferencesValidator()
        is_data_valid = prefferences_validator.validate_prefferences(data)
        
        if is_data_valid != None: 
            return is_data_valid
        
        # get the logged in user's uuid to save the prefference for that specific user
        username = data['username']
        logged_in_user_uuid = UserRepository.get_uuid_by_username(username)

        prefferences = data['prefferences']
        for prefference_name, prefference_value in prefferences.items():
            # get the prefference uuid from the prefference table
            prefference_uuid = PrefferenceRepository.get_prefference_uuid(prefference_name)
            
            # check if the prefference is already inserted in DB 
            user_prefference = UserPrefferenceRepository.get_prefference_by_name_and_uuid_user(prefference_name, logged_in_user_uuid)

            if user_prefference == None: 
                # build the data if the prefference has not been yet saved
                data = {
                    'uuid_user': logged_in_user_uuid,
                    'uuid_prefference': prefference_uuid,
                    'prefference_name': prefference_name,
                    'liked': prefference_value
                }

                #serialize the data then save it in the DB
                serializer = UserPrefferenceSerializer(data=data)

                if serializer.is_valid():
                    serializer.save()
                else : 
                    print(serializer.error_messages)
                
            else:
                # actual User object, as Serializer can't update with just the UUID
                logged_in_user = UserRepository.search_user_by_username(username)
                # actual Prefference object, as Serializer can't update with just the UUID
                prefference = PrefferenceRepository.get_prefference_by_name(prefference_name)

                user_prefference.uuid_user = logged_in_user
                user_prefference.uuid_prefference = prefference
                user_prefference.prefference_name = prefference_name
                user_prefference.liked = prefference_value

                user_prefference.save()

        return None
