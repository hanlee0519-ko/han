from django.forms import ModelForm

from articleapp.models import Article


class ArticleCreationForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'image', 'content'] # writer는 유저와 마찬가지로 서버에서, view에서 하겠구먼