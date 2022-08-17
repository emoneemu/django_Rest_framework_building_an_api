from .serializers import StatusSerializer
from .models import Status

#importing some of drf functions to make easy my api built context_process
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import generics
# Create your views here.

#creating a class based view Like before:
class StatusAPIView(APIView):

    def get(self , request , format=None):
        status_list = Status.objects.all()

        #converting into json data
        status_serializer = StatusSerializer(status_list,many = True)

        return Response(status_serializer.data)
        #now we have to call this view

class StatusListAPIView(generics.ListAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

class StatusCreateAPIView(generics.CreateAPIView):
    queryset =Status.objects.all()
    serializer_class = StatusSerializer

class StatusDetailAPIView(generics.RetrieveAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

    #it's a way to retrieve unique fields
    lookup_field = "id"

    #another way to retrive unique fields: using(or should i say rewrite ;) ) a function get_object()

    #def get_object(self,*args,**kwargs):
    #    kwargs = self.kwargs
    #    #print(kwargs)
    #    kw_id = kwargs.get("id")
    #    return Status.objects.get(id=kw_id)


class StatusUpdateAPIView(generics.UpdateAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    lookup_field = "id"


class StatusDeleteAPIView(generics.DestroyAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    lookup_field = "id"
