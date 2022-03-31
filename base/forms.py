from django import forms

class EmailForm(forms.Form):
    email = forms.EmailField()
    betreff = forms.CharField(max_length=100)
    datei = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    nachricht = forms.CharField(widget = forms.Textarea)