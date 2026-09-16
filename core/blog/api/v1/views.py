from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from .serializers import PostSerializer
from blog.models import Post
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def post_list(request):

    if request.method == 'GET':
        posts = Post.objects.filter(status=True)
        serializer = PostSerializer(posts,many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
@api_view(['GET','PUT','DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])
def post_detail(request,id):

    post = get_object_or_404(Post,pk=id)
    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = PostSerializer(post,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        post.delete()
        return Response({'detail':'item removed successfully'},status=status.HTTP_204_NO_CONTENT)
    
class PostListApiView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        posts = Post.objects.filter(status=True)
        serializer = PostSerializer(posts,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
class PostDetailApiView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer

    def get(self,request,id):
        post = get_object_or_404(Post,pk=id,status=True)
        serializer = self.serializer_class(post)
        return Response(serializer.data)
    
    def put(self,request,id):
        post = get_object_or_404(Post,pk=id,status=True)
        serializer = self.serializer_class(post,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self,request,id):
        post = get_object_or_404(Post,pk=id,status=True)
        post.delete()
        return Response({'detail':'item removed successfully'},status=status.HTTP_204_NO_CONTENT)

class PostListGenericApiView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)

    def get(self,request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
class PostDetailGenericAPIView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer

    def get(self,request,id):
        post = get_object_or_404(Post,pk=id,status=True)
        serializer = self.serializer_class(post)
        return Response(serializer.data)
    
    def put(self,request,id):
        post = get_object_or_404(Post,pk=id,status=True)
        serializer = self.serializer_class(post,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self,request,id):
        post = get_object_or_404(Post,pk=id,status=True)
        post.delete()
        return Response({'detail':'item removed successfully'},status=status.HTTP_204_NO_CONTENT)
