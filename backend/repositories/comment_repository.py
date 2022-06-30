from ..models.standalone.comment_model import Comment

class CommentRepository:

    def get_number_of_comments_by_post_uuid(post_uuid):
        return Comment.objects.filter(post_uuid_comment_id=post_uuid)
    
    def create_comment(post_uuid, user_uuid, comment_text):
        comment = Comment.objects.create(comment=comment_text, post_uuid_comment_id=post_uuid, user_uuid_comment_id=user_uuid)
        comment.save()
    
    def get_all_comments(post_uuid):
        return Comment.objects.filter(post_uuid_comment_id=post_uuid)