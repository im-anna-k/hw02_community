from django import forms


class PostForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    group = forms.CharField(required=False)
