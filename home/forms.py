from django import forms
from .models import Post, Comment


class PostCreateUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('body',)


class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        widgets = {'body': forms.Textarea(attrs={'class': "form-control", 'rows': 3, 'cols': 30})}


class CommentReplyForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        widgets = {'body': forms.Textarea(attrs={'class': "form-control", 'rows': 3, 'cols': 30})}


class PostSearchForm(forms.Form):
    search = forms.CharField(max_length=100)
