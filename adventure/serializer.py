from rest_framework import serializers
from .models import Room, Character

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'n_to', 's_to', 'e_to', 'w_to', 'x', 'y', 'title', 'description']

class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ['id','data']