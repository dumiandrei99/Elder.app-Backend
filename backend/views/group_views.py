from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from ..services.group_service import GroupService
from ..services.recommend_service import RecommendService


class AllGroups(APIView):
    def get(self, request):
        group_service = GroupService()
        response = group_service.get_all_groups()
        return Response(response)

class GroupsAUserIsIn(APIView):
    def post(self, request):
        data = JSONParser().parse(request)
        group_service = GroupService()
        response = group_service.groups_a_user_is_in(data)
        return Response(response)

class SavePrefferencesView(APIView):
    def post(self, request):
        data = JSONParser().parse(request)
        group_service = GroupService()
        response = group_service.save_prefferences(data)
        return Response(response)  

class RecommendGroupsView(APIView):
    def post(self, request):
        data = JSONParser().parse(request)
        user = data['username']
        recommend_service = RecommendService()
        response = recommend_service.recommend_groups(user)
        return Response(response)
        
class AddUserInGroup(APIView):
    def post(self, request):
        data = JSONParser().parse(request)
        group_service = GroupService()

        response = group_service.add_user_in_group(data)

        return Response(response)