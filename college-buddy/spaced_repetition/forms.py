from django import forms


class Todo_completed_form(forms.Form):
    completed = forms.BooleanField(label="is_completed", initial=False)