from backend.models.standalone.group_model import Group
from ..validators.prefferences_validator import PrefferencesValidator
from ..validators.add_user_in_group_validator import AddUserInGroupValidator
from ..validators.groups_a_user_is_in_validator import GroupsAUserIsInValidator
from ..repositories.user_repository import UserRepository
from ..repositories.prefference_repository import PrefferenceRepository
from ..repositories.user_prefference_repository import UserPrefferenceRepository
from ..repositories.group_repository import GroupRepository
from ..repositories.user_in_group_repository import UserInGroupRepository
from ..serializers.group_related.user_prefference_serializer import UserPrefferenceSerializer
from ..serializers.group_related.user_in_group_serializer import UserInGroupSerializer

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
        return True


    def add_user_in_group(self, data):
        user_and_group_validator = AddUserInGroupValidator()
        is_data_valid = user_and_group_validator.validate_user_and_group(data)

        # check if username and group name are present
        if is_data_valid != None:
            return is_data_valid

        # get username and group name from the request
        username = data['username']
        group_name = data['group_name']

        # get the user uuid and the group uuid by name
        user_uuid = UserRepository.get_uuid_by_username(username)
        group_uuid = GroupRepository.get_group_uuid_by_name(group_name)

        # build the data
        data = {
            'group_name': group_name,
            'uuid_group': group_uuid,
            'uuid_user': user_uuid
        }

        # save the data in DB
        serializer = UserInGroupSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            print(username)
            print(group_name)
            print(user_uuid)
            print(group_uuid)
            return True
        else:
            return serializer.error_messages

    def groups_a_user_is_in(self, data):
        groups_a_user_is_in_validator = GroupsAUserIsInValidator()
        is_data_valid = groups_a_user_is_in_validator.validate(data)

        if is_data_valid != None:
            return is_data_valid
        
        username = data['username']
        user_uuid = UserRepository.get_uuid_by_username(username)
        groups_user_is_in = UserInGroupRepository.get_all_groups_a_user_is_in(user_uuid)

        result = []
        for group in groups_user_is_in:
            group_name = GroupRepository.get_group_name_by_uuid(group.uuid_group.uuid)
            group_description = GroupRepository.get_group_description(group_name)
            group = {
                'group_name': group_name,
                'group_description': group_description
            }
            result.append(group)

        return result

    def get_all_groups(self):

        groups = GroupRepository.get_all_groups()

        result = []
        for group in groups:
            group = {
                'group_name': group.group_name,
                'group_description': group.group_description
            }
            result.append(group)
        return result