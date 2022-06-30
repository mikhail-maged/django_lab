from django import forms
from subject.models import *

class insertnewtrainee(forms.Form):
    name= forms.CharField(max_length=20,widget=forms.TextInput(attrs={'class': 'form-control form-control-user'}))
    nationnum= forms.IntegerField()
    sub= forms.ChoiceField(choices=[(c.id,c.name) for c in subject.objects.all()])


class insertnewtraineemod(forms.ModelForm):
    #course = forms.ChoiceField(choices=[(c.id, c.name) for c in Course.objects.all()])
    class Meta:
        model=newtrainee
        fields='__all__'
