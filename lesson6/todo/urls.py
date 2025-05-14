from django.urls import path
from .views import index, header_view, query_params_view, path_argument_view, body_view, http_type_view

# app_name = 'todo'

urlpatterns = [
    path('index/', index, name='index'),
    path('header/', header_view, name='header'),
    path('query-params/', query_params_view, name='query-params'),
    path('path/<int:id>/<str:name>/', path_argument_view, name='path-argument'),
    path('body/', body_view, name='body'),
    path('http-type/', http_type_view, name='http-type'),
    
]