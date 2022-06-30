from django.urls import path
from ..views.user_views import AddProfilePicture, ChangePassword

urlpatterns = [
    path('add-profile-picture', AddProfilePicture.as_view()),
    path('change-password', ChangePassword.as_view())
]