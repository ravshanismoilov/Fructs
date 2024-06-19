from django.forms import ModelForm
from .models import Fructs


class CreateFructForm(ModelForm):
    class Meta:
        model = Fructs
        fields = '__all__'