from django.http import HttpResponse
from django.core import serializers
from home.models import TodoList

def ApiTodo(request):
    instance = TodoList.objects.all()
    qs_json = serializers.serialize('json',instance)
    return HttpResponse(qs_json,content_type='application/json')