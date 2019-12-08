from django.urls import path

from . import views
app_name='sightings'

urlpatterns = [
        path('',views.list_sights),
        path('add/',views.add_sights),
        path('<Unique_Squirrel_Id>/',views.update_sights),
        ]
