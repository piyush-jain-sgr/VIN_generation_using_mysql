from django.forms import ModelForm
from .models import vinnumbers_new

class vinNumber(ModelForm):
    class Meta:
        model = vinnumbers_new
        fields = '__all__'