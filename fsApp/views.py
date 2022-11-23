from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def home(request):
#     print(request)
#     print(request.method)
#     print(request.COOKIES)
#     print(request.path)
#     print(request.user)
#     print(request.META)
#     html='<html><h1>Hello. World!</h1></html>'
#     return HttpResponse(html)

def home(request):
    context = {
        'caption': 'clarusway',
        'dict1': {'django': 'best framework'},
        'my_list': [2, 3, 4]
    }
    return render(request, 'fsApp/index.html', context)
