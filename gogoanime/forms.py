from django.forms import ModelForm
from django import forms
from .models import Anime_All


STATUS_CHOICES = (
    ("", "Select"),
    ("Complete", "Complete"),
    ("Ongoing", "Ongoing"),
    ("Upcoming", "Upcoming"),
)


class AddAnime(ModelForm):

    anime_name = forms.CharField(
        widget=forms.TextInput(),
        required=False,
    )
    gogoanime_url = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Gogoanime Url"}),
        max_length=255,
        label="",
    )
    gogoanime_id = forms.IntegerField(
        widget=forms.NumberInput(),
        required=False,
    )
    no_of_episodes = forms.IntegerField(
        widget=forms.NumberInput(attrs={"placeholder": "No of Episodes"}),
        label="",
    )
    summary = forms.CharField(
        widget=forms.TextInput(),
        required=False,
    )
    # Latest_Episode = models.IntegerField(null=False)
    status = forms.CharField(
        widget=forms.Select(
            choices=STATUS_CHOICES,
        ),
        label="",
    )
    other_name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Other Name"}),
        max_length=255,
        label="",
    )

    class Meta:
        model = Anime_All
        fields = [
            "anime_name",
            "gogoanime_url",
            "gogoanime_id",
            "no_of_episodes",
            "status",
            "other_name",
            "gogoanime_id",
            "summary",
        ] 
        # widgets = {"gogoanime_id": forms.HiddenInput(), "summary": forms.HiddenInput()}
