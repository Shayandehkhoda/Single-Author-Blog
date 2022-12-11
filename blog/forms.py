from django import forms
from .models import Newsletter, Comment
from captcha.fields import CaptchaField


class NewsletterForm(forms.ModelForm):

    class Meta:
        model = Newsletter
        fields = '__all__'


class CommentForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Comment
        fields = '__all__'
