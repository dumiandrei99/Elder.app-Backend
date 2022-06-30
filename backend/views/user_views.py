from rest_framework.parsers import JSONParser
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView
from ..services.post_service import PostService
from ..services.user_service import UserService


class AddProfilePicture(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):
        data = request.data
        user_service = UserService()

        response = user_service.update_profile_picture(data)

        print(response)
        
        return Response("A")

class ChangePassword(APIView):
    def post(self, request):
        data = JSONParser().parse(request)
        
        user_service = UserService()

        response = user_service.change_password(data)
        return Response(response)