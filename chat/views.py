from django.shortcuts import render
from .models import Room, Message 
# Create your views here.


def index_view(request):
    rooms = Room.objects.all()
    return render(request, 'index.html', {'rooms' : rooms })


def room_view(request, room_name):
    room = Room.objects.get_or_create(name=room_name)
    return render(request, 'room.html', {'room': room})
