from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

@api_view(['GET'])
def get_all_posts(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_post(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def like_post(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
        post.likes += 1
        post.save()
        return Response(status=status.HTTP_200_OK)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def add_comment(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
        text = request.data.get('text')
        comment = Comment(post=post, text=text)
        comment.save()
        return Response(status=status.HTTP_201_CREATED)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
