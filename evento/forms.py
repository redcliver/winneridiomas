from django.forms import ModelForm      
from .models import eventoModel

class eventoForm(ModelForm):
  class Meta:
        model = eventoModel
        fields = "__all__" 