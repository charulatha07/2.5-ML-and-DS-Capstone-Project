from django import forms
from .models import *


class ckdForm(forms.ModelForm):
    class Meta():
        model=ckdModel
        fields=['subscription_length','vehicle_age','customer_age','region_density','turning_radius','length','width','gross_weight','engine_type']
