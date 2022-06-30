from ..models.standalone.post_model import Post
from django.db.models import Q

class PostRepository:

    def get_number_of_likes_by_user_uuid(user_uuid):
        return Post.objects.filter(post_user_id=user_uuid)
    
    def get_posts_from_group_user_is_in(group_uuid):
        query = Q(post_group_id=group_uuid)
        return Post.objects.filter(query)

    def get_author_by_post_uuid(uuid):
        return Post.objects.filter(uuid=uuid).first().post_user_id

    def get_posts_user_posted_in_group(group_uuid, user_uuid):
        query = Q(post_group_id=group_uuid)
        query.add(Q(post_user_id=user_uuid), Q.AND)
        return Post.objects.filter(query)
