import profile
from django.contrib.sites.models import Site
from urllib import request
from django.http import QueryDict
from backend.models.standalone.post_model import Post
from backend.validators.comment_validator import CommentValidator
from ..repositories.user_repository import UserRepository
from ..repositories.group_repository import GroupRepository
from ..repositories.post_repository import PostRepository
from ..repositories.comment_repository import CommentRepository
from ..repositories.user_in_group_repository import UserInGroupRepository
from ..repositories.like_repository import LikeRepository
from ..validators.post_validator import PostValidator
from ..validators.like_validator import LikeValidator
from ..validators.get_comments_validator import GetCommentsValidator

class PostService:
    def save_post(self, data):
        # validate data
        post_validator = PostValidator()
        is_data_valid = post_validator.validate_post(data)

        # return error message if it's the case
        if is_data_valid != None:
            return is_data_valid

        # get the username and group name that the user want's to add the post to (also, parse it)
        username = data['post_user']
        post_group_name = data['post_group']
        
        post_group_name = post_group_name.lower()
        user = UserRepository.get_user_by_username(username)
        
        group = None
        if post_group_name != "public":
            group = GroupRepository.get_group_by_name(post_group_name)

        # replace the group uuid and user uuid in the dictionary that will be passed to the serializer
        serializer_data = QueryDict.copy(data)
        
        serializer_data['post_user'] = user
        serializer_data['post_group'] = group

        post = Post.objects.create(
            post_description=serializer_data['post_description'],
            post_group=serializer_data['post_group'],
            post_user=serializer_data['post_user'],
            post_image=serializer_data['post_image'],
        )

        post.save()

        return "The post was created successfully!"


    def get_posts_for_user(self, data, request):

        username = data['username']
        user_uuid = UserRepository.get_uuid_by_username(username)
        request_type = data['posts']
        
        groups = []
        # get the groups a user is in
        if request_type == 'all_groups' or request_type == 'profile':
            groups_user_is_in  = UserInGroupRepository.get_all_groups_a_user_is_in(user_uuid)

            for group in groups_user_is_in:
                group_name = GroupRepository.get_group_by_name(group.uuid_group.group_name)
                groups.append(group_name)

        if request_type == 'one_group':
            group_name = data['group']
            group = GroupRepository.get_group_by_name(group_name)
            print(group_name)
            groups.append(group)
        

        user_posts = Post.objects.none()
        for group in groups:
            if request_type == 'profile':
                user_posts = user_posts | PostRepository.get_posts_user_posted_in_group(group, user_uuid)
            else:
                user_posts = user_posts | PostRepository.get_posts_from_group_user_is_in(group)
        
        response_array = []
        for post in user_posts:
            number_of_likes = len(LikeRepository.get_number_of_likes_by_post_uuid(post.uuid))
            number_of_comments = len(CommentRepository.get_number_of_comments_by_post_uuid(post.uuid))
            group_name = GroupRepository.get_group_name_by_uuid(post.post_group_id).upper()
            post_content = post.post_description
            post_image = post.post_image
            author_uuid = PostRepository.get_author_by_post_uuid(post.uuid)
            author = UserRepository.get_username_by_uuid(author_uuid)
            liked_post = LikeRepository.is_post_liked_by_user(user_uuid, post.uuid)
            profile_picture = UserRepository.get_profile_picture_by_username(author)

            if profile_picture != 'null':
                profile_picture = request.build_absolute_uri(profile_picture.url)
            else: 
                profile_picture = None

            if post_image == 'null':
                response = {
                    'number_of_likes': number_of_likes,
                    'number_of_comments': number_of_comments,
                    'group_name': group_name,
                    'post_content': post_content,
                    'post_image': None,
                    'post_uuid': post.uuid,
                    'author': author,
                    'liked': liked_post,
                    'profile_picture': profile_picture
                }
            else:
                url = request.build_absolute_uri(post_image.url)
                response = {
                    'number_of_likes': number_of_likes,
                    'number_of_comments': number_of_comments,
                    'group_name': group_name,
                    'post_content': post_content,
                    'post_image': url,
                    'post_uuid': post.uuid,
                    'author': author,
                    'liked': liked_post,
                    'profile_picture': profile_picture
                }
            response_array.append(response)
        return response_array
    

    def like(self, data):
        
        post_uuid = data['post_uuid']
        username = data['username']
        
        user_uuid = UserRepository.get_uuid_by_username(username)

        liked_post = LikeRepository.is_post_liked_by_user(user_uuid, post_uuid)
        
        if liked_post == False:
            LikeRepository.user_liked_post(user_uuid, post_uuid)
            return "Like"
        else:
            LikeRepository.user_disliked_post(user_uuid, post_uuid)
            return "Dislike"
    
    def comment(self, data):
        comment_validator = CommentValidator()

        is_data_valid = comment_validator.validate_comment(data)

        if is_data_valid != None:
            return is_data_valid

        post_uuid = data['post_uuid']
        comment_text = data['comment']
        username = data['username']

        user_uuid = UserRepository.get_uuid_by_username(username)
        CommentRepository.create_comment(post_uuid, user_uuid, comment_text)

        response = {
            'author': username,
            'comment': comment_text
        }
        return response


    def get_comments(self, data):
        get_comments_validator = GetCommentsValidator()

        is_data_valid = get_comments_validator.validate_get_comments(data)

        if is_data_valid != None:
            return is_data_valid
        
        post_uuid = data['post_uuid']

        all_comments = CommentRepository.get_all_comments(post_uuid)

        result = []
        for comment in all_comments:
            username = UserRepository.get_username_by_uuid(comment.user_uuid_comment_id)
            response = {
                'comment': comment.comment,
                'author': username
            }
            result.append(response)
        
        return result