from django.shortcuts import render
from .models import Sight
from django.shortcuts import redirect
from .forms import SightForm

# Create your views here.
def map_view(request):
    sights = Sight.objects.all()[:100]
    context = {
            'sights':sights,
            }
    return render(request, 'sightings/map.html', context)

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

def stats_view(request):
    sights = Sight.objects.all()
    context = {
            'Shift': {'AM':sights.filter(Shift='AM').count(),'PM':sights.filter(Shift='PM').count()},
            'Age': {'Juvenile':sights.filter(Age='Juvenile').count(),'Adult':sights.filter(Age='Adult').count()},
            'Primary_Fur_Color': {'Black':sights.filter(Primary_Fur_Color='Black').count(),'Gray':sights.filter(Primary_Fur_Color='Gray').count(),'Cinnamon':sights.filter(Primary_Fur_Color='Cinnamon').count()},
            'Location': {'Above_Ground':sights.filter(Location='Above Ground').count(),'Ground_Plane':sights.filter(Location='Ground Plane').count()},
            'Runs_From': {'True':sights.filter(Runs_From='TRUE').count(),'False':sights.filter(Runs_From='FALSE').count()},
            }
    return render(request, 'sightings/stats.html', {'context':context})

