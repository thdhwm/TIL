from django.shortcuts import render

# Create your views here.
def index(request):
    
    menus = ['koopa', 'kimchi', '10F']

    context = {
        'menus': menus,
    }
    return render(request, 'books/index.html', context)

def detail(request, menu):      # 요청과 함께 변수도 같이 전달
    # [주의사향] 변수 이름 urls.py 와 동일하게 설정
    context = {
        'menu': menu,
    }
    
    return render(request, 'books/detail.html', context)
