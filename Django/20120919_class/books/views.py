from django.shortcuts import render

# request: 사용자 요청 정보
def index(request):
    # django 는 기본적으로 html 파일들을
    # app/templates 폴더에서 검색한다.

    menus = ['순대국밥', '김치볶음밥', '10층']
    
    context = {
        'menus': menus,
    }

    return render(request, "books/index.html", context)


# 요청과 동시에 변수도 함께 전달
# [주의사항] 변수 이름 urls.py 와 동일하게 작성
def detail(request, menu):
    context = {
        'menu': menu,
    }

    return render(request, "books/detail.html", context)

