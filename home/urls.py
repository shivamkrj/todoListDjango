from django.urls import path,include,re_path
from rest_framework import routers

from . import views
from .views import TodoViewSetAPI
# router = routers.DefaultRouter
# router.register(r'list',views.todoViewSetAPI)


urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<id>/',views.details, name = 'detail'),
    path('add',views.addTodo, name = 'add'),
    path('delete/<id>/',views.deleteTodo, name = 'delete'),
    # re_path('api',TodoViewSetAPI.as_view(),name='api'),
    path('api',views.ApiTodo, name='api'),
    path('test',views.testJSON, name='test'),
]