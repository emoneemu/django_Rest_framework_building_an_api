from .serializers import StatusSerializer
from .models import Status

#importing some of drf functions to make easy my api built context_process
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

#creating a class based view Like before:
class StatusAPIView(APIView):

    def get(self , request , format=None):
        status_list = Status.objects.all()

        #converting into json data
        status_serializer = StatusSerializer(status_list,many = True)

        return Response(status_serializer.data)
        #now we have to call this view
