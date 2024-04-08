from rest_framework import viewsets

from walk_a_dog_app.models import (ClientOpinion, Dog, Slot, TrainerOpinion,
                                   Walk)
from walk_a_dog_app.serializers import (ClientOpinionSerializer, DogSerializer,
                                        SlotSerializer, TrainerOpinionSerializer,
                                        WalkSerializer)


class DogViewSet(viewsets.ModelViewSet):
    serializer_class = DogSerializer

    def get_queryset(self):
        return Dog.objects.all()


class SlotViewSet(viewsets.ModelViewSet):
    serializer_class = SlotSerializer

    def get_queryset(self):
        return Slot.objects.all()


class WalkViewSet(viewsets.ModelViewSet):
    serializer_class = WalkSerializer

    def get_queryset(self):
        return Walk.objects.all()


class ClientOpinionViewSet(viewsets.ModelViewSet):
    serializer_class = ClientOpinionSerializer

    def get_queryset(self):
        return ClientOpinion.objects.all()


class TrainerOpinionViewSet(viewsets.ModelViewSet):
    serializer_class = TrainerOpinionSerializer

    def get_queryset(self):
        return TrainerOpinion.objects.all()
