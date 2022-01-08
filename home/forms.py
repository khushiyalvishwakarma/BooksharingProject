from django import forms
from .models import Upload_book

class photo(forms.ModelForm):
    class Meta:
        model=Upload_book
        fields='__all__'