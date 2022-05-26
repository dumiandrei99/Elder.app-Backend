from ..models.group_related.user_in_group_model import UserInGroup

class UserInGroupRepository:
    def get_all_users_in_groups():
        return UserInGroup.objects.all()

