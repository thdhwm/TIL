from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ArticleForm


# 게시판 메인 페이지 (GET)
def index(request):
    # DB의 모든 articles 를 context 로 전달
    articles = Article.objects.all()

    context = {
        'articles': articles,
    }

    response = render(request, "articles/index.html", context)
    
    # [참고] 쿠키 설정
    response.set_cookie(
        key="username",
        value="giryun",
    )

    return response


# 생성 페이지 (GET)
# 게시물 생성 (POST)
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        # 유효성 검증
        # - 성공 시 True 반환
        # - 실패 시 form 안에 error 를 담는다.
        if form.is_valid():
            form.save()
            return redirect("articles:index")
    else:
        form = ArticleForm()

    # 들여쓰기 하면
    # 유효성 검증 실패 시에 문제가 생긴다.
    context = {
        'form': form,
    }
    
    return render(request, "articles/create.html", context)


def detail(request, id):
    article = get_object_or_404(Article, id=id)

    context = {
        'article': article,
    }

    return render(request, "articles/detail.html", context)

def update(request, id):
    article = Article.objects.get(id=id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.id)
    
    else:
        form = ArticleForm(instance=article)

    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)

def delete(request, id):
    article = get_object_or_404(Article, id=id)
    article.delete()

    return redirect('articles:index')
