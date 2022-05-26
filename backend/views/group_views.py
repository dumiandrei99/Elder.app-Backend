from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from ..services.group_service import GroupService
from ..services.recommend_service import RecommendService

class RecommendGroupsView(APIView):
    def post(self, request):
        data = JSONParser().parse(request)
        group_service = GroupService()
        
        response = group_service.save_prefferences(data)
        if response != None:
            return Response(response)
        
        user = data['username']
        recommend_service = RecommendService()
        response = recommend_service.recommend_groups(user)

        return Response(response)
        
