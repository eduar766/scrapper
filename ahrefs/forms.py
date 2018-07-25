from django.forms import ModelForm, TextInput
from .models import GoogleSearch, ScrapperTest, SingleAhref


class GoogleForm(ModelForm):
    class Meta:
        model = GoogleSearch
        fields = ['keyword', 'cant']
        widgets = {
            'keyword': TextInput(
                attrs= {
                    'class': 'input',
                    'placeholder': 'Ingresa tu keyword'
                }
            ),
            'cant': TextInput(
                attrs= {
                    'class': 'input',
                    'placeholder': 'Cantidad de Resultados deseados'
                }
            )
        }


class ScrapperForm(ModelForm):
    class Meta:
        model = ScrapperTest
        fields = ['url']
        widgets = {
            'url': TextInput(
                attrs = {
                    'class': 'input',
                    'placeholder': 'Ingresa una url para probar el Scrapper'
                }
            )
        }


class SingleAhrefsForm(ModelForm):
    class Meta:
        model = SingleAhref
        fields = ['url']
        widgets = {
            'url': TextInput(
                attrs = {
                    'class': 'input form-control',
                    'placeholder': 'Ingresa URL para scanear',
                    'id': 'exampleInputEmail1'
                }
            )
        }
