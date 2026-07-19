from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('events/<int:event_id>/confirm/', views.confirm_presence, name="confirm_presence_view"),
    path('events/<int:event_id>/guest/', views.confirm_guest_presence, name="confirm_guest_presence_view")
]