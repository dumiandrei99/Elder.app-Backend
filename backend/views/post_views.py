from rest_framework.parsers import JSONParser
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView
from ..services.post_service import PostService


class AddPost(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):
        post_service = PostService()
        response = post_service.save_post(request.data)
        return Response(response)


class GetPostsForUser(APIView):

    def post(self, request):
        data = JSONParser().parse(request)
        
        post_service = PostService()

        response = post_service.get_posts_for_user(data, request)
        return Response(response)

class Like(APIView):
    
    def post(self, request):
        data = JSONParser().parse(request)
        post_service = PostService()

        response = post_service.like(data)

        return Response(response)

class Comment(APIView):

    def post(self, request):
        data = JSONParser().parse(request)
        post_service = PostService()

        response = post_service.comment(data)

        return Response(response)

class GetComments(APIView):

    def post(self, request):
        data = JSONParser().parse(request)
        post_service = PostService()

        response = post_service.get_comments(data)

        return Response(response)