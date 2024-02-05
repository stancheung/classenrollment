from django import forms
from .models import Enrollments, Classes

class EnrollmentForm(forms.ModelForm):
    #classes = forms.ModelChoiceField(queryset=Classes.objects.all())
    class Meta:
        model = Enrollments
        fields = ['class_enrolled']
        widgets = {
            'class_enrolled': forms.Select,
        }