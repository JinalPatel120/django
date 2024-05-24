from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view



@api_view(['GET','POST','PATCH'])
def get_home(request):
    if request.method=='GET':
        return Response({
            'status':200,
            'message':' django rest framework is working'
        })
    elif request.method=='POST':
         return Response({
            'status':200,
            'message':' call post method'
        })
         
    elif request.method=='PATCH':
         return Response({
            'status':200,
            'message':' call patch method'
        })
    
    else:
         return Response({
            'status':200,
            'message':' invalid mathod called'
        })
        