from django.contrib import admin
from .models import Player, Review, Tag

admin.site.register(Player)
admin.site.register(Tag)
admin.site.register(Review)

