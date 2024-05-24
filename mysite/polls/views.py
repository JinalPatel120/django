from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('helooo i am jinal')

def detail(request,question_id):
    return HttpResponse(request, 'you are looking at question %s.'% question_id)

def result(request,question_id):
    response=('you are looking at result of the question %s')
    return HttpResponse(response % question_id)

def vote(request,question_id):
    return HttpResponse('you ar voting on question %s.' % question_id)
