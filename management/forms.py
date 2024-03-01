from django import forms

from management.models import UploadModel


class AdminForm(forms.ModelForm):
    class Meta:
        model = UploadModel
        fields = ('departure','flight','airline','planetype')

