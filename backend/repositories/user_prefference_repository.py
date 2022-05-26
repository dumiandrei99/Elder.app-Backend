from ..models.group_related.user_prefference_model import UserPrefference

class UserPrefferenceRepository:
    def get_prefference_by_name_and_uuid_user(prefference_name, uuid_user):
        return UserPrefference.objects.filter(prefference_name=prefference_name, uuid_user=uuid_user).first()
    
    def get_all_user_prefferences():
        return UserPrefference.objects.all()