from ..models.group_related.user_in_group_model import UserInGroup

class UserInGroupRepository:
    def get_all_users_in_groups():
        return UserInGroup.objects.all()

    def get_all_groups_a_user_is_in(uuid_user):
        return UserInGroup.objects.filter(uuid_user=uuid_user)