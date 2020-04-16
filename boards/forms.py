from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .models import Status, Priority, Type

class DeleteForm(forms.Form):
    delete_field = forms.CharField(label="Type DELETE to delete this project",
                                   help_text="WARNING: You will not be able to recover this project once it is deleted!",
                                   required=False)

    def clean_delete_field(self):
        data = self.cleaned_data['delete_field']
        if data != "DELETE":
            raise ValidationError(_('Enter DELETE to delete the project.'))
        return data

class NewProjectForm(forms.Form):
    title_field = forms.CharField(label="Project Title")
    description_field = forms.CharField(label="Project Description")

class NewFeatureForm(forms.Form):
    title_field = forms.CharField(label="Feature Title")
    description_field = forms.CharField(label="Feature Description")
    status_field = forms.ChoiceField(choices=Status.choices, initial=Status.NEW)

class NewItemForm(forms.Form):
    title_field = forms.CharField(label="Item Title")
    description_field = forms.CharField(label="Item Description")
    priority_field = forms.ChoiceField(label="Item Priority", choices=Priority.choices)
    points_field = forms.IntegerField(label="Item Points", min_value=0)
    type_field = forms.ChoiceField(label="Item Type", choices=Type.choices)
    status_field = forms.ChoiceField(label="Item Status", choices=Status.choices, initial=Status.NEW)
