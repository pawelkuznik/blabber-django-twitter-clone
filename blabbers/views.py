from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render
from .models import Blab

# Create your views here.
def home_view(request, *args, **kwargs):
    return HttpResponse("<h1>Hello World</h1>")

def blabber_detail_view(request, blab_id, *args, **kwargs):
    """
    REST API VIEW
    """
    data = {
        "id": blab_id,
    }    
    status = 200
    try:
        obj = Blab.objects.get(id=blab_id)
        data['content'] = obj.content
    except:
        data['message'] = "Not found"
        status = 404

    return JsonResponse(data, status=status)
    
