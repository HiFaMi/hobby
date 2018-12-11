from django import forms

from .models import Post


class PostForm(forms.Form):
    content = forms.CharField(
        label='내용',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )

    def save(self, author):
        return Post.objects.create(
            author=author,
            content=self.cleaned_data['content'],
        )
