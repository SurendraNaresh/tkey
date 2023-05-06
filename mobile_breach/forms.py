from django import forms
from .models import Breach, Device


class BreachForm(forms.ModelForm):
    device_id = forms.CharField(max_length=50, label="Device ID")
    description = forms.CharField(max_length=255, label="Device Description")
    breach_type = forms.CharField(max_length=50, label="Breach Type")
    prevention_steps = forms.CharField(widget=forms.Textarea, label="Prevention Steps")

    class Meta:
        model = Breach
        fields = ["device_id", "description", "breach_type", "prevention_steps"]
