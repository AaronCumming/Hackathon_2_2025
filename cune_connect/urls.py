from django.urls import path

from . import views

app_name = "cune_connect"
urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("<int:pk>/", views.OrgView.as_view(), name="organization"),
    path("<int:pk>/<int:event_id>/", views.EventView.as_view(), name="event"),
    path("up_coming_events/", views.upcoming_events_view, name="upcoming_events_view"),
]