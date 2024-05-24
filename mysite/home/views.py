from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.


# GET
# POST
# UPDATE
#DELETE
# PATCH

@api_view(['GET'])
def home(request):
    response= {'status' : 1 , 'message' : 'hi this is jinal'}
    return Response(response)