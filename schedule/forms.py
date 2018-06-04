from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import Candidate, CHOICES, STATUS
from django import forms

Users = [(x.id, x.username) for x in User.objects.all()]


class UserForm(AuthenticationForm):
    username = forms.CharField(required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(required=True,
                               widget=forms.TextInput(
                                   attrs={'type': 'password', 'class': 'form-control', 'placeholder': 'Password'}))


class CandidateForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    experience = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    interview_date = forms.DateTimeField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'datepicker'}))
    interviewed_by = forms.ModelChoiceField(queryset=User.objects.all(),
                                            widget=forms.Select(attrs={'class': 'form-control'}))
    status = forms.ChoiceField(choices=STATUS, widget=forms.Select(attrs={'class': 'form-control'}))
    applying_for = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Candidate
        exclude = ['added_by', 'date_time', 'created_date']
