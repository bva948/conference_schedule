from django.urls import path
from . import views

app_name='booking'

urlpatterns = [
    path('', views.Hi),
    path('rooms/', views.RoomListView.as_view(), name='room_list'),
    path('rooms/<int:pk>', views.RoomDetailView.as_view(), name='room_detail'),
    path('rooms/update_<int:pk>', views.RoomUpdateView.as_view(), name='room_update'),
    path('new_room/', views.NewRoomView.as_view(), name='new_room'),
]

