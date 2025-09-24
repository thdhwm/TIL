from django.shortcuts import render, redirect, get_object_or_404
from .models import Bakery


def index(request):
    # DB의 Bakery 테이블에서 데이터를 모두 가져온다
    bakeries = Bakery.objects.all().order_by("-rating")
    print(bakeries)
    for bakery in bakeries:
        print(bakery)
        # print(bakery.name)
        # print(bakery.address)
        # print(bakery.rating)

    context = {
        "bakeries": bakeries,
    }
    
    return render(request, "bakeries/index.html", context)


from django.http import HttpResponseNotFound

def detail(request, id):
    # 데이터 하나를 조회
    # - get() 의 단점: 없는 데이터는 버그가 나버린다
    # bakery = Bakery.objects.get(pk=id)

    # - 개발 시에는 없으면, 에러 페이지로 이동해야 한다
    # bakery = Bakery.objects.filter(pk=id).first()
    # if bakery is None:
    #     return HttpResponseNotFound("<h1>잘못된 id 를 넣었다.</h1>")

    # - 실제 개발 시 많이 활용한다.
    bakery = get_object_or_404(Bakery, id=id)

    context = {
        'bakery': bakery,
    }

    return render(request, "bakeries/detail.html", context)


# 1. 생성하기 페이지 보여주기 (GET)
# 2. DB에 새로운 정보 저장 (POST)
def create(request):
    if request.method == "POST":
        # request 에서 데이터 받아와서 DB에 저장
        print(request.POST)
        name = request.POST.get("name")
        address = request.POST.get("address")
        rating = request.POST.get("rating")
        opening_time = request.POST.get("opening_time")
        closing_time = request.POST.get("closing_time")

        # Bakery 저장
        # save vs create
        Bakery.objects.create(
            name=name,
            address=address,
            rating=rating,
            opening_time=opening_time,
            closing_time=closing_time,
        )
        
        # 메인페이지로 다시 요청을 보내줘야 함
        return redirect("bakeries:index")
    else:
        return render(request, "bakeries/create.html")
