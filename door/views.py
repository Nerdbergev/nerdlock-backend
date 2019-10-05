from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import DoorStatusSerializer
from django.http import Http404
import os
from django.apps import apps


DoorStatus = apps.get_model('doorlog', 'DoorStatus')

@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def open(request, format=None):
    mycmd = os.popen("open_door")

    content = {
        'result': mycmd,
    }
    doorStatus = DoorStatus()
    doorStatus.status = DoorStatus.OPEN
    doorStatus.user = request.user
    doorStatus.save()
    return Response(content)


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def close(request, format=None):
    mycmd = os.popen("close_door")
    content = {
        'result': mycmd,
    }
    doorStatus = DoorStatus()
    doorStatus.status = DoorStatus.CLOSE
    doorStatus.user = request.user
    doorStatus.save()
    return Response(content)


class DoorStatusDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self):
        return DoorStatus.objects.latest('id')

    def get(self, request, format=None):
        status = self.get_object()
        serializer = DoorStatusSerializer(status)
        return Response(serializer.data)
