from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import TodoSerializer
from .models import Todo
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import mixins, viewsets



@api_view(['GET','POST','PATCH'])
def get_home(request):
    if request.method=='GET':
        return Response({
            'status':200,
            'message':' called get method'
        })
        
    elif request.method=='POST':
         return Response({
            'status':200,
            'message':' called post method'
        })
         
    elif request.method =='PATCH':
         return Response({
            'status':200,
            'message':' called patch method'
        })
    else:
         return Response({
            'status':400,
            'message':' you called invaliud methos'
        })
  
         
     
    
class todoview(APIView):
    
    def get(self,request):
        todo_objs= Todo.objects.all()
        serializer=TodoSerializer(todo_objs , many= True)
    
        return Response({
        "status" : True,
        "message":"todo fetches",
        "data" : serializer.data
         })      
        
    def post(self,request):
        try:
            data= request.data
            serializer=TodoSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                  
                  'status':True,
                  'message':'data retrive success',
                  'data': serializer.data
              })
            
      
            return Response({
            'status': False,
            'message':' Invalid data',
            'data' :serializer.errors
            })
        
        except Exception as e:
            print(e)
    
            return Response({
            'status':False,
            'message':'somethiong went wrong'
        })
        
    def patch(self,request):
        return Response({
            'status':200,
            'message':' called patch method'
        })
        
        
class Todoviewset(viewsets.ModelViewSet):
    queryset=Todo.objects.all()
    serializer_class=TodoSerializer