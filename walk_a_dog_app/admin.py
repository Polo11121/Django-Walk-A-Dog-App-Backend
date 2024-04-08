from django.contrib import admin

from walk_a_dog_app.models import (ClientOpinion, Dog, Slot, TrainerOpinion,
                                   Walk)

admin.site.register(Dog)
admin.site.register(Slot)
admin.site.register(Walk)
admin.site.register(ClientOpinion)
admin.site.register(TrainerOpinion)
