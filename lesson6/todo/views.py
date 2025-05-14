from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the todo index.")



def header_view(request):
    headers = request.headers
    
    print(headers.get('User-Agent'))
    return HttpResponse("Headers: " + headers.get('User-Agent'))



def query_params_view(request):
    query_param = request.GET.get('param1', 'default')
    return HttpResponse("Query param: " + query_param)


def path_argument_view(request, *args,**kwargs):
    return HttpResponse("Path arguments: " + str(args) + " args" + str(kwargs) + " kwargs")

@csrf_exempt
def body_view(request):
    body = request.body
    print(body)
    
    return HttpResponse("Body: " + body.decode('utf-8'))


@csrf_exempt
def http_type_view(request):
    method = request.method
    if method == "GET":
        return HttpResponse("Method: GET")
    elif method == "POST":
        return HttpResponse("Method: POST")
    elif method == "PUT":
        return HttpResponse("Method: PUT")
    elif method == "DELETE":
        return HttpResponse("Method: DELETE")
    else:
        return HttpResponse("Method: " + method)