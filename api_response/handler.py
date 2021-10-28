from django.views.decorators.csrf import csrf_exempt
from django.http.response import HttpResponse
import requests
@csrf_exempt
def response_api(request):
    print("container1 is called")
    r=requests.get('http://app2:8080/')
    return HttpResponse(r)
