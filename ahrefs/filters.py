from django.forms import ModelForm, TextInput

from .models import Backlinks, CSV_import
import django_filters

class BacklinksFilter(django_filters.FilterSet):
    class Meta:
        model = Backlinks
        fields = ['language', 'site_link', 'url_from', 'title', 'url_to', 'anchor', 'nofollow']



class CSVFilter(django_filters.FilterSet):
    class Meta:
        model = CSV_import
        fields = ['language', 'site_link', 'foro']
