from ..models.standalone.group_model import Group

class GroupRepository:

    def get_all_groups():
        return Group.objects.all()
            
    def get_group_description(group_name):
        return Group.objects.filter(group_name=group_name).first().group_description

    def get_group_uuid_by_name(group_name):
        return Group.objects.filter(group_name=group_name).first().uuid

    def get_group_name_by_uuid(uuid_group):
        return Group.objects.filter(uuid=uuid_group).first().group_name
    
    def get_group_by_name(group_name):
        return Group.objects.filter(group_name=group_name).first()