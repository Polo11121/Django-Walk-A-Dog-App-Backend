from email.policy import default

from django.db import models
from django.db.models.deletion import CASCADE

from core.user.models import User


class Dog(models.Model):
    name = models.CharField(max_length=64)
    owner = models.ForeignKey(User, on_delete=CASCADE)
    age = models.IntegerField()
    breed = models.CharField(max_length=128)
    weight = models.IntegerField()
    recommendation = models.TextField(blank=True)
    contraindications = models.TextField(blank=True)
    avatar = models.ImageField(
        blank=True, null=True, upload_to="dogs/", default="dogs/logo.png")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return '{0} ({1})'.format(self.name, self.owner)


class Slot(models.Model):
    trainer = models.ForeignKey(User, on_delete=CASCADE)
    date = models.DateField()
    time_from = models.TimeField()
    time_to = models.TimeField()
    dog1 = models.ForeignKey(Dog, on_delete=CASCADE,
                             related_name='dog1', null=True, blank=True)
    dog2 = models.ForeignKey(Dog, on_delete=CASCADE,
                             related_name='dog2', null=True, blank=True)
    dog3 = models.ForeignKey(Dog, on_delete=CASCADE,
                             related_name='dog3', null=True, blank=True)
    choices = (('nie rozpoczęty', 'nie rozpoczęty'),
               ('w trakcie', 'w trakcie'),
               ('zakończony', 'zakończony'),)
    status = models.CharField(
        max_length=64, choices=choices, default='nie rozpoczęty')

    def __str__(self):
        return '{0} {1} {2}-{3}'.format(
            self.trainer,
            self.date,
            self.time_from,
            self.time_to
        )


class Walk(models.Model):
    slot = models.ForeignKey(Slot, on_delete=CASCADE)
    lat = models.FloatField(default=0)
    lng = models.FloatField(default=0)

    def __str__(self):
        return f"{self.slot}"


class ClientOpinion(models.Model):
    client = models.ForeignKey(User, related_name='client', on_delete=CASCADE)
    dog = models.ForeignKey(Dog, on_delete=CASCADE, null=True, blank=True)
    trainer = models.ForeignKey(
        User, related_name='trainer', on_delete=CASCADE)
    review = models.TextField(max_length=250)
    points = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return 'Klient: {0} -> Trener: {1}'.format(self.client, self.trainer)


class TrainerOpinion(models.Model):
    trainer = models.ForeignKey(
        User, related_name='trainer2', on_delete=CASCADE, null=True, blank=True)
    dog = models.ForeignKey(Dog, on_delete=CASCADE, null=True, blank=True)
    client = models.ForeignKey(User, related_name='client2', on_delete=CASCADE, null=True, blank=True)
    raport = models.TextField(max_length=250)
    type = models.TextField(max_length=250,default="")

    def __str__(self):
        return 'Trener: {0} -> Pies: {1}'.format(self.trainer, self.dog)
