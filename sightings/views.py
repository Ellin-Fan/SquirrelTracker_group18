from django.shortcuts import render
from .models import Sight
from django.shortcuts import redirect
from .forms import SightForm

# Create your views here.

def list_sights(request):
    sights = Sight.objects.all()
    fields = ['Unique_Squirrel_Id','Longtitude','Latitude','Date','Shift']
    context = {
            'sights':sights,
            'fields':fields,
            }
    return render(request, 'sightings/list.html', context)

def update_sights(request,Unique_Squirrel_Id):
    sight = Sight.objects.get(Unique_Squirrel_Id=Unique_Squirrel_Id)
    if request.method == 'POST':
        form = SightForm(request.POST, instance = sight)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings/{Unique_Squirrel_Id}')
    else:
        form = SightForm(instance = sight)

    context = {
            'form':form,
            }
    return render(request, 'sightings/update.html', context)

def add_sights(request):
    if request.method == 'POST':
        form = SightForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings/')
    else:
        form = SightForm()

    context = {
            'form':form,
            }

    return render(request, 'sightings/update.html', context)

