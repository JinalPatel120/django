from django.shortcuts import render,get_object_or_404,redirect
from .models import Post1
from .forms import PostForm
from django.utils import timezone
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


# Create your views here.
def post_line(request):
    posts=Post1.objects.order_by('published_date')
    return render(request,'blog/post_line.html',{'posts':posts})

def post_detail(request,pk):
    post=get_object_or_404(Post1,pk=pk)
    return render(request,'blog/post_detail.html',{'post':post})


def post_new(request):
    if request.method=='POST':
        form=PostForm(request.POST)
    if form.is_valid():
        post=form.save(commit=False)
        post.author=request.user
        post.published_date=timezone()
        post.save()
        return redirect('post_detail',pk=post.pk)
    
    else:
        form=PostForm()
    return render(request,'blog/post_edit.html',{'form':form})
    



class Home(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)