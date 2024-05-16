# posts > views.py
from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets

from .models import Post
from .serializers import *

class PostAPIView(APIView):
    def post(self, request):
        serializer = PostBaseSerializer(data = request.data)
        if serializer.is_valid():
            if serializer.validated_data['bad_post'] == True:
                return Response({"message": "bad post" }, status=status.HTTP_400_BAD_REQUEST)
            else:
                serializer.save()
                return Response({"message": "post success"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PostAPIView2(APIView):
    def post(self, request):
        serializer = PostSerializer(data = request.data)
        print(serializer.initial_data)
        if serializer.is_valid():
            print(serializer.validated_data)
            print(serializer.data)
            if serializer.initial_data['bad_post'] == True:
                return Response({"message": "bad post" }, status=status.HTTP_400_BAD_REQUEST)
            else:
                serializer.save()
                return Response({"message": "post success"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#과제 2번 : 전체 게시글 목록 가져오기
class PostList(APIView):
    def get(self, request):
        posts = Post.objects.all() # Post에 있는 모든 오브젝트 가져오기
        serializers = PostSerializer(posts, many=True)
        return Response(serializers.data)

#과제 3번 : 특정 게시글에 댓글 달기
@api_view(['POST'])
def CommentCreate(request):
    serializer = CommentSerializer(data = request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)

    
class PostModelViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
