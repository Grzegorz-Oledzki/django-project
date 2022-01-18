from django.forms import ModelForm
from .models import Player


class PlayerForm(ModelForm):
    class Meta:
        model = Player
        fields = [
            "title",
            "description",
            "demo_link",
            "source_link",
            "tags",
            "featured_image",
        ]
