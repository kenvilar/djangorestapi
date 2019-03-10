from django import forms

from .models import Status


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = [
            'user',
            'content',
            'image',
        ]

    def clean_content(self, *args, **kwargs):
        content = self.cleaned_data.get('content')
        if len(content) > 240:
            raise forms.ValidationError("Content is too long")
        return content

    def clean(self, *args, **kwargs):
        _data = self.cleaned_data
        _content = _data.get('content', None)

        if _content == "":
            _content = None
        _image = _data.get("image", None)

        if _content is None and _image is None:
            raise forms.ValidationError('Content or image is required.')
        return super().clean(*args, **kwargs)
