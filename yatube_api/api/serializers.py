from django.shortcuts import get_object_or_404
from rest_framework import serializers


from posts.models import Comment, Post, Follow, Group, User


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        model = Comment
        fields = '__all__'


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )
    following = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all()
    )

    def validate(self, data):
        user = get_object_or_404(User, username=data['following'].username)
        follow = Follow.objects.filter(
            user=self.context['request'].user, following=user).exists()
        if user == self.context['request'].user:
            raise serializers.ValidationError(
                "Вы не можете подписаться сам на себя")
        if follow is True:
            raise serializers.ValidationError(
                "Вы уже подписаны на пользователя")
        return data

    class Meta:
        model = Follow
        fields = '__all__'
        read_only_fields = ('id', 'user')


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Group
