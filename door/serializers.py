from rest_framework import serializers
from django.apps import apps


DoorStatus = apps.get_model('doorlog', 'DoorStatus')


class DoorStatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DoorStatus
        fields = ['status']


