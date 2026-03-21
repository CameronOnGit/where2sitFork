from django.shortcuts import render
from .models import Room


# Create your views here.


#def room_list(request):
#   rooms = Room.objects.all()
 #  return render(request, "rooms/room_list.html", {"rooms": rooms})




def room_list(request):
   rooms = Room.objects.all()
   min_capacity = request.GET.get("min_capacity")


   if min_capacity:
       try:
           minimum = int(min_capacity)
           rooms = rooms.filter(capacity__gte = minimum)
       except ValueError:
           pass
           
    return render(request, "rooms/room_list.html", {"rooms": rooms})
