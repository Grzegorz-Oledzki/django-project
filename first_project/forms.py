from django.forms import ModelForm
from first_project.models import Player, Review
from django import forms


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
        widgets = {
            "tags": forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super(PlayerForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({"class": "input", "placeholder": "Add " + name})
        # self.fields['title'].widget.attrs.update({'class': 'input', 'placeholder': 'Add name'})
        # self.fields['description'].widget.attrs.update({'class': 'input', 'placeholder': 'Add description'})
        # self.fields['demo_link'].widget.attrs.update({'class': 'input', 'placeholder': 'Add demo link'})
        # self.fields['source_link'].widget.attrs.update({'class': 'input', 'placeholder': 'Add source link'})

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['value', 'body']
        labels = {
            'value': 'Place your vote',
            'body': 'Add a comment with your vote'
        }

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({"class": "input"})
