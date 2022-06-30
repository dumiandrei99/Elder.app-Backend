from ..models.standalone.like_model import Like
from django.db.models import Q

class LikeRepository:

    def get_number_of_likes_by_post_uuid(post_uuid):
        return Like.objects.filter(post_uuid_id=post_uuid) 

    def is_post_liked_by_user(user_uuid, post_uuid):
        query = Q(post_uuid_id=post_uuid)
        query.add(Q(liked_by_id=user_uuid), Q.AND)
        
        if Like.objects.filter(query).first() == None:
            return False
        
        return True
    
    def user_liked_post(user_uuid, post_uuid):
        like = Like.objects.create(liked_by_id=user_uuid, post_uuid_id=post_uuid)
        like.save()
    
    def user_disliked_post(user_uuid, post_uuid):
        query = Q(post_uuid_id=post_uuid)
        query.add(Q(liked_by_id=user_uuid), Q.AND)

        dislike = Like.objects.get(query)
        dislike.delete()