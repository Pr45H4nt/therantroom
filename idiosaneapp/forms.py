from django import forms
from .models import Article , Comment , Feedback

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['poster','Title','summary','Content','Tags']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['Body']


class Feedbackform(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'