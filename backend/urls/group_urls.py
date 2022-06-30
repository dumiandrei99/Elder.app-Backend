from django.urls import path
from ..views.group_views import RecommendGroupsView, AddUserInGroup, SavePrefferencesView, GroupsAUserIsIn, AllGroups

urlpatterns = [
    path ('get-all-groups', AllGroups.as_view()),
    path ('groups-a-user-is-in', GroupsAUserIsIn.as_view()),
    path ('save-prefferences', SavePrefferencesView.as_view()),
    path ('recommend-groups', RecommendGroupsView.as_view()),
    path ('add-user-to-group', AddUserInGroup.as_view())
]