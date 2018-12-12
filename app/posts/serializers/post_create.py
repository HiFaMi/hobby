from rest_framework import serializers

from ..models import Post


class PostCreateSerializer(serializers.Serializer):
    content = serializers.CharField(
        max_length=None,
    )

    class Meta:
        model = Post
        fields = (
            'author',
            'content',
        )
