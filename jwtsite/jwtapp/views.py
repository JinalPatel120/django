from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializer import *
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.authentication import SessionAuthentication, BaseAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics
# Create your views here.

class RegisterAPI(APIView):
    def post(self,request):
        serializer=UserSerializer(data=request.data)
        if not serializer.is_valid():
              return Response({
        'status' : 200,
        'payload' : serializer.errors,
        'message':'invalid data'
        })
       
        serializer.save()
        user=User.objects.get(username= serializer.data['username'])
        token_obj,_ =Token.objects.get_or_create(user=user)
    

            
        return Response({
                'status' : 401,
                'payload' : serializer.data,
                'message' : 'valid data',
                'token':str(token_obj)
            })
            
   

class StudentAPI(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self,request):
        student_obj=Student.objects.all()
        serializer=StudentSerializer(student_obj , many=True)
        return Response({
        'status' : 200,
        'payload' : serializer.data
    })
    
    
    def post(self,request):
        serializer= StudentSerializer(data=request.data)
    
        if serializer.is_valid():
            serializer.save()
            return Response({
            'status' : 200,
            'payload' : serializer.data,
            'message' : 'you sent data succesfully'
        })
        
        else:
            

            return Response({
                'status' : 401,
                'payload' : serializer.data,
                'message' : 'bad request'
            })
            
    
    def patch(self,request):
        try:
            stud_obj=Student.objects.get(id=request.data['id'])
            serializer=StudentSerializer(stud_obj,data=request.data , partial=True)
            
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "status":200,
                    "payload":serializer.data,
                    "message":"your data was updated"
                    
                })
                
                
            else:
                return Response({
                    "status":400,
                    "message":"bad request"
                })
                
        
        except Exception as e:
             return Response({
            "status":404,
            "message":"you entered invalid id"
        })
        
    
    def put(self,request):
        try:
            stud_obj=Student.objects.get(id=request.data['id'])
            serializer=StudentSerializer(stud_obj,data=request.data , partial=True)
            
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "status":200,
                    "payload":serializer.data,
                    "message":"your data was updated"
                    
                })
            
                
            else:
                return Response({
                    "status":400,
                    "message":"bad request"
                })
                
        
        except Exception as e:
             return Response({
            "status":404,
            "message":"you entered invalid id"
        })
        
        
    
    def delete(self,request):
        try:
            id=request.GET.get('id')
            stud_obj=Student.objects.get(id=id)
            stud_obj.delete()
            return Response({
                "status":200,
                "message":"deleted"
            })
        
        except Exception as e:
            return Response({
                
                "status":400,
                "message":"invalid id"
            })
        
  
 
        
@api_view(['GET'])
def get_book(request):
  
        book_obj= Book.objects.all()
        serializer= BookSerializer( book_obj , many=True)
        return Response({
            "status":200,
            "payload":serializer.data
        })
        
        
class student_generic(generics.ListAPIView,generics.CreateAPIView):
    serializer_class=StudentSerializer
    queryset= Student.objects.all()
    
    
class student_generic1(generics.UpdateAPIView , generics.DestroyAPIView):
    serializer_class=StudentSerializer
    queryset= Student.objects.all()
    lookup_field= 'id'