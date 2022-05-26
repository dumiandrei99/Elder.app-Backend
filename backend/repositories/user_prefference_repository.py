from ..models.group_related.user_prefference_model import UserPrefference

class UserPrefferenceRepository:
    def get_prefference_by_name(prefference_name):
        return UserPrefference.objects.filter(prefference_name=prefference_name).first()
    
    def get_all_user_prefferences():
        return UserPrefference.objects.all()