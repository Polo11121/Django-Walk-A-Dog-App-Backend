from rest_framework import serializers

from walk_a_dog_app.models import (ClientOpinion, Dog, Slot, TrainerOpinion,
                                   Walk)


class DogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dog
        fields = ['id', 'name', 'owner', 'age', 'breed', 'weight',
                  'recommendation', 'contraindications', 'avatar', 'is_active']


class SlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slot
        fields = ['id', 'trainer', 'date', 'time_from',
                  'time_to', 'dog1', 'dog2', 'dog3', 'status']


class WalkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Walk
        fields = ['id', 'slot', 'lat', 'lng']


class ClientOpinionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientOpinion
        fields = ['id', 'client', 'dog', 'trainer', 'review', 'points']


class TrainerOpinionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainerOpinion
        fields = ['id', 'trainer', 'dog', 'client', 'raport',"type"]
