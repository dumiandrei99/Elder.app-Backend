from this import d
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from ..services.user_service import UserService
# Create your views here.

class RegisterView(APIView):
    def post(self, request): 
        data = JSONParser().parse(request)
        user_service = UserService()
        response = user_service.user_register(data)
        return Response(response)

class LogInView(APIView):
    def post(self, request):
        data = JSONParser().parse(request)
        user_service = UserService()
        response = user_service.user_login(data, request)

        if type(response) is dict:
            return Response(response)
        else: 
            token = response
            response = Response()
            response.set_cookie(key='jwt', value = token, httponly=True)
            response.data = {
                'jwt': token,
                'status': '200'
            }
            return response

class LogOutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'User logged out',
            'status': '200'
        }
        return response

class GetAuthenticatedUserView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')
        user_service = UserService()
        response = user_service.get_authenticated_user(token)
        return Response(response)


class GenerateVerificationCodeView(APIView):
    def post(self, request):
        data = JSONParser().parse(request)
        user_service = UserService()
        response = user_service.generate_verification_code(data)
        return Response(response)

class CheckVerificationCode(APIView):
    def post(self, request):
        data = JSONParser().parse(request)
        user_service = UserService()
        response = user_service.check_verification_code(data)
        return Response(response)