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

    return render(request, "rooms/room_list.html", context)


# Reservation view (no login required)
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.shortcuts import redirect

@csrf_exempt
def reservation(request):
    from .models import Room
    rooms = Room.objects.select_related('building').all()
    success = False
    error = None
    if request.method == 'POST':
        room_id = request.POST.get('room')
        date = request.POST.get('date')
        time_ = request.POST.get('time')
        duration = request.POST.get('duration')
        name = request.POST.get('name')
        if not (room_id and date and time_ and duration):
            error = 'Please fill in all required fields.'
        else:
            # Here you would normally save the reservation to the database
            # For now, just show success (no model yet)
            success = True
    context = {
        'rooms': rooms,
        'success': success,
        'error': error,
    }
    return render(request, "rooms/reservation.html", context)
