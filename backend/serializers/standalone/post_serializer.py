from rest_framework import serializers;
from ...models.standalone.post_model import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        