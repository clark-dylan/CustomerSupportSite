from django import forms

from forum.models import Questions, Answers
from tinymce import HTMLField

class CreatePost(forms.ModelForm):
    title = forms.CharField()
    description = HTMLField("content")
    class Meta:
        model = Questions
        fields = ('title', 'description',)


class AnswerForm(forms.ModelForm):
    reply = HTMLField("content")

    class Meta:
        model = Answers
        fields = ('reply',)