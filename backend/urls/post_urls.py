from django.urls import path
from ..views.post_views import AddPost, GetPostsForUser, Like, Comment, GetComments

urlpatterns = [
    path('add-post', AddPost.as_view()),
    path('get-posts-for-user', GetPostsForUser.as_view()),
    path('like', Like.as_view()),
    path('comment', Comment.as_view()),
    path('get-comments', GetComments.as_view())
]