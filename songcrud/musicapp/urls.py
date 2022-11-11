from django.urls import path
from .views import index, genericApiView
# SongView, SongUpdateView

urlpatterns = [
    path("", index, name="index"),
    path('genericApiView/', genericApiView.as_view()),
    path('genericApiView/<int:id>/', genericApiView.as_view())

]
