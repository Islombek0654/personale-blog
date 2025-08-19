from rest_framework import serializers
from .models import Blog

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'


# если есть пользователи которые регаются
# class PostSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Post
#         fields = ['id', 'title', 'content', 'author']
#         read_only_fields = ['author']  # автор устанавливается автоматически