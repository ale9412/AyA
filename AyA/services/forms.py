from django import forms

from servicios.models import RangeTime

class DateRangeForm(forms.ModelForm):
    class Meta:
        model = RangeTime 

        fields = (
            'start_time',
            'end_time',
        )

        labels = {
            'start_time':'Tiempo de Inicio',
            'end_time':'Tiempo Final',
        }

        widgets = {
            'start_time':forms.DateTimeInput(attrs={'class':'form-control','placeholder':'dd/mm/yyyy HH:MM'},format='%m/%d/%Y %H:%M'),
            'end_time':forms.DateTimeInput(attrs={'class':'form-control','placeholder':'dd/mm/yyyy HH:MM'},format='%m/%d/%Y %H:%M'),
         }
