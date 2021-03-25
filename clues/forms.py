from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Team


class VolleyballUpdateForm(forms.Form):
    teams_field = forms.ModelChoiceField(queryset=Team.objects.all())
    score = forms.IntegerField()


class JengaUpdateForm(forms.Form):
    teams_field = forms.ModelChoiceField(queryset=Team.objects.all())
    score = forms.IntegerField()