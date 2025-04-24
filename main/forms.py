from django import forms
from .models import Projects, Comment


class CreateForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ['title', 'description', 'category', 'image']

class CommentSend(forms.ModelForm):
    text = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'chat-input', 'placeholder': 'Напишите сообщение...'
    }))
    class Meta:
        model = Comment
        fields = ['text']