from ..models.standalone.prefference_model import Prefference

class PrefferenceRepository:
    def get_prefference_uuid(prefference_name):
        return Prefference.objects.filter(prefference_name=prefference_name).first().uuid
    
    def get_prefference_by_name(prefference_name):
        return Prefference.objects.filter(prefference_name=prefference_name).first()