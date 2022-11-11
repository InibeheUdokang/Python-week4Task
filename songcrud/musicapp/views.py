from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from rest_framework import mixins
from .models import Song
from .Serializers import SongSerializer
from rest_framework.response import Response


# Create your views here.

# Http Response for musicapp
def index(request):
    return HttpResponse("My first zuri Musicapp")

# class method for creating, updating, deleting, listing of my song model


class genericApiView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):

    serializer_class = SongSerializer
    queryset = Song.objects.all()
    lookup_field = 'id'

    def get(self, request):

        return self.list(request)

    def post(self, request, id=None):  # check back if id is neccessary here
        return self.create(request, id)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id=None):
        return self.destroy(request, id)

