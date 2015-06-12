from django import forms

from zmoc.models import Change


class ChangeForm(forms.ModelForm):
    uid = forms.IntegerField(widget=forms.HiddenInput())
    commit_id = forms.IntegerField(max_value=128, help_text="Gitlab commit id")
    tag_id = forms.IntegerField(max_value=64, help_text="Gitlab tag")
    stamp = forms.DateTimeField(widget=forms.HiddenInput())
    content = forms.Textarea()

    class Meta:
        model = Change
        fields = ('uid', 'type', 'commit_id', 'tag_id', 'staff', 'stamp', 'content')
