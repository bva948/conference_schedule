from django.http.response import HttpResponse
from django.shortcuts import render
from django.views import generic, View
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import ConferenceRoom, Conference, RoomForm

def Hi(request):
    return HttpResponse("Hello")

class RoomListView(LoginRequiredMixin, generic.ListView):
    login_url='accounts/login'
    template_name='conference_booking/room_list.html'
    context_object_name='room_list'

    def get_queryset(self):
        return ConferenceRoom.objects.all()

class RoomDetailView(LoginRequiredMixin, generic.DetailView):
    model=ConferenceRoom
    template_name='conference_booking/room_detail.html'
    context_object_name='room'

class RoomUpdateView(LoginRequiredMixin, View):
    
    def get(self, request, pk):
        form=RoomForm()
        return render(request, 'conference_booking/room_update.html', {'form': form, 'id': pk})

    def post(self, request, pk):
        room=ConferenceRoom.objects.get(id=pk)
        room.name=request.POST['name']
        room.position=request.POST['position']
        room.save()
        return HttpResponse("Updated")

class NewRoomView(LoginRequiredMixin, View):
    
    def get(self, request):
        form=RoomForm()
        return render(request, 'conference_booking/new_room.html', {'form': form})

    def post(self, request):
        new_room=RoomForm(request.POST)
        if new_room.is_valid():
            new_room.save()
            return HttpResponse("New room has been saved")