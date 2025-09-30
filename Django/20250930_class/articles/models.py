from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=20)  # 제목 (20글자 이내)
    content = models.TextField()  # 내용
    created_time = models.DateTimeField(auto_now_add=True)  # 생성일자 (자동생성)
    updated_time = models.DateTimeField(auto_now=True)  # 수정일자 (자동생성)

