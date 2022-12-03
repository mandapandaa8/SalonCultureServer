from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from salonapi.models import Comment

class CommentView(ViewSet):
    def retrieve(self, request, pk):
        comment = Comment.objects.get(pk=pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    def list(self, request):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def update(self, request, pk):
        comment = Comment.objects.get(pk=pk)
        comment.comment_text = request.data["commentText"]
        comment.photo_id = request.data["photoId"]
        comment.user_id = request.data["userId"]
        comment.save()

        return Response(status=status.HTTP_204_NO_CONTENT)

    def create(self, request):
        new_comment = Comment()
        new_comment.comment_text = request.data["commentText"]
        new_comment.photo_id = request.data["photoId"]
        new_comment.user_id = request.data["userId"]
        new_comment.save()

        serializer = CommentSerializer(new_comment)

        return Response(serializer.data)

    def destroy(self, request, pk):
        comment = Comment.objects.get(pk=pk)
        comment.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

class CommentSerializer(serializers.ModelSerializer):
    """JSON serializer for comments
    Arguments:
        serializers
    """
    class Meta:
        model = Comment
        fields = ('id', 'comment_text', 'photo_id', 'user_id')