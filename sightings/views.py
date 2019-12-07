from django.shortcuts import render
from .models import Sight
from django.shortcuts import redirect

# Create your views here.

def list_sights(request):
    sights = Sight.objects.all()
    context = {
            'sights':sights,
            }
    return HttpResponse(render(request, 'sightings/list.html', context))


