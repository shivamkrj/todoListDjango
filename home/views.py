from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from datetime import datetime
from rest_framework import viewsets,generics
from .serializers import TodoSerializer
from django.core import serializers
from urllib.request import urlopen
import json

from .models import TodoList
# Create your views here.

def index(request):
    list = TodoList.objects.all()[::-1]
    # # list = [x.text for x in list]
    # # output = ', '.join(list)
    # # print(list)
    # template = loader.get_template('home/index.html')
    context = {
        'list': list,
    }
    msg = request.GET.get('msg')
    print(msg,' skr')
    # return HttpResponse(template.render(context, request))
    return render(request,'home/index.html',context)

def details(request,id):
    print(id)
    s = TodoList.objects.get(pk=id)
    print(s)
    context = {
        'text' : s.text,
        'id' : s.id,
    }
    return render(request, 'home/details.html', context)

def addTodo(request):
    text = request.POST['message']

    print(text)
    if len(text)>0:
        TodoList.objects.create(text = text,pub_date = datetime.now())
    # todo = TodoList()
    # todo.text = text
    # todo.pub_date =datetime.now
    # todo.save()
    return HttpResponseRedirect(reverse(index))

def deleteTodo(request,id):
    todo = get_object_or_404(TodoList,pk = id)
    todo.delete()
    return HttpResponseRedirect(reverse(index))

class TodoViewSetAPI(generics.ListAPIView):

    queryset = TodoList.objects.all()
    serializer_class = TodoSerializer

def ApiTodo(request):
    instance = TodoList.objects.all()
    qs_json = serializers.serialize('json',instance)
    return HttpResponse(qs_json,content_type='application/json')

def testJSON(request):
    url = 'http://127.0.0.1:8000/api/api'
    response = urlopen(url)

    # Convert bytes to string type and string type to dict
    string = response.read().decode('utf-8')
    print(string)
    print()
    print('skr')
    print()
    json_obj = json.loads(string)
    print(json_obj)
    return HttpResponse(string)

