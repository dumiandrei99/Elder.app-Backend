from django.urls import path
from ..views.group_views import RecommendGroupsView

urlpatterns = [
    path('recommend-groups', RecommendGroupsView.as_view())
]