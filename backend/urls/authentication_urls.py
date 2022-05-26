from django.urls import path
from ..views.authentication_views import LogInView, RegisterView, GetAuthenticatedUserView, LogOutView, GenerateVerificationCodeView, CheckVerificationCode

urlpatterns = [
    path('register', RegisterView.as_view()),
    path('log-in', LogInView.as_view()),
    path('user', GetAuthenticatedUserView.as_view()),
    path('log-out', LogOutView.as_view()),
    path('generate-verification-code', GenerateVerificationCodeView.as_view()),
    path('check-verification-code', CheckVerificationCode.as_view())
]