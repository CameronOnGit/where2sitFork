from django.shortcuts import render
from .models import Room, Building

# Create your views here.

def home(request):
    featured_rooms = Room.objects.select_related('building').all()[:6]
    buildings = Building.objects.all()

    context = {
        'featured_rooms': featured_rooms,
        'buildings': buildings,
    }
    return render(request, "rooms/home.html", context)

def room_list(request):
    rooms = Room.objects.all()

    building = request.GET.get("building")
    min_capacity = request.GET.get("min_capacity")

    if building:
        try:
            rooms = rooms.filter(building__name=building)
        except ValueError:
            pass

    if min_capacity:
        try:
            rooms = rooms.filter(capacity__gte=int(min_capacity))
        except ValueError:
            pass

    return render(request, "rooms/room_list.html", {"rooms": rooms})
