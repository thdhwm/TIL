from django import forms
from .models import Article


# Form vs ModelForm
# Form: 입력받을 데이터를 지정할 것이다
# ModelForm: DB 에 저장할 테이블만 입력 받을 것인가 ?

# class ArticleForm(forms.Form):
#     pass


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        labels = {
            'title': "제목",
            'content': "내용",
        }
        fields = "__all__"  # 전체 데이터를 입력받겠다
        # fields = ('title', )  # 특정 컬럼만 입력받겠다 (튜플, 리스트로 작성)