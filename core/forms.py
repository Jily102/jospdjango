from django.forms import ModelForm
from .models import Message


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'email', 'subject', 'body']

    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control', })

        self.fields['subject'].widget.attrs.update(
            {'class': 'form-control', })
        self.fields['body'].widget.attrs.update(
            {'class': 'form-control', })