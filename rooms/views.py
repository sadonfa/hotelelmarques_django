from turtle import title
from django.shortcuts import render
from rooms.models import Room

# Create your views here.

def rooms(request):

    room = Room.objects.order_by('title')

    return render(request, "rooms/index.html",{
        'title_pag': 'Nuestras Habitaciones',
        'rooms': room
    })