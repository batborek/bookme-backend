from rest_framework import serializers
from bookme_api import models

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Room
        fields = ('id','type','price','is_booked','is_clean')
