# import sys
# sys.stdin = open('input.txt')

# ---->> 실행하면 input.txt 읽어와서 자동으로 입력되게


# ###### 퀵 소트 (임의의 피벗(pivot)값 설정하고 리스트 순회해서 (피벗보다 작은값) (피벗) (피벗보다 큰 값) 으로 정렬 ###### #

# array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
#
#
# def quick_sort(array, start, end):
#     if start >= end:
#         return
#     pivot = start  # 피벗 초기값은 첫번째 요소
#     left = start + 1
#     right = end
#
#     while left <= right:
#         # 피벗보다 큰 데이터를 찾을 때까지 반복
#         while left <= end and array[left] <= array[pivot]:
#             left += 1
#
#             # 피벗보다 작은 데이터를 찾을 때까지 반복
#         while right > start and array[right] >= array[pivot]:
#             right -= 1
#
#         if left > right:  # 엇갈렸다면 작은 right -=1 데이터와 피벗을 교체
#             array[right], array[pivot] = array[pivot], array[right]
#
#         else:  # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
#             array[left], array[right] = array[right], array[left]
#
#     # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
#     quick_sort(array, start, right - 1)
#     quick_sort(array, right + 1, end)
#
#
# quick_sort(array, 0, len(array) - 1)
# print(array)

# ########################################################################################################### #

# 우선순위 큐
# import heapq 조으다 .heappush, .heappop  조으다

# 유니온 파인드

# ########################################################################################################### #
# def fib(n):        # memoization ( top down )
#     if n <= 1:
#         return n
#     if memo[n]:
#         return memo[n]
#     memo[n] = fib(n-1) + fib(n-2)
#     return memo[n]
#
#
# N = 10  # change here for different value
# memo = [0] * (N + 1)
#
# print(fib(N))

# ################################################################################################
# def fib(n):        # dp ( bottom up )
#     dp = [0] * (n + 1)
#     dp[0] = 0
#     dp[1] = 1
#     for i in range(2, n + 1):
#         dp[i] = dp[i - 1] + dp[i - 2]
#     return dp[n]


# print(fib(10))

# ################################################################################################
# from heapq import heappush, heappop, heapify
#
# heap = [4, 15, 19, 11, 20, 13]
# heapify(heap)
#
# print(heap)

# heapify - sort list in heap order  -> make a list in to heap
# heappush(arr, element) - insert an element in heap order
# heappop() - pop minimum element

# ################################################################################################
# import heapq
# from collections import defaultdict
# import sys
# sys.stdin = open('input.txt')
#
#
# def dijkstra(start, table):
#     costs = [float('inf')] * (n + 1)
#     costs[start] = 0
#     q = []
#     heapq.heappush(q, (0, start))
#
#     while q:
#         current_dist, current_node = heapq.heappop(q)
#
#         if costs[current_node] < current_dist:
#             continue
#
#         for next_cost, next_node in table[current_node]:
#             new_cost = current_dist + next_cost
#             if costs[next_node] > new_cost:
#                 costs[next_node] = new_cost
#                 heapq.heappush(q, (new_cost, next_node))
#
#     return costs
#
#
# n = int(input())
# m = int(input())
# table = defaultdict(list)
#
# for _ in range(m):
#     s, e, c = map(int, input().split())
#     table[s].append((c, e))
#
# s, e = map(int, input().split())
#
# result = dijkstra(s, table)
# print(result)

# ##########################################################################################

# _hex = '000000000110100000000'
# _valid = '0001101'
#
# int(_hex[:7])
# a = bin(1110110110001011101101100010110001000110100100110111011)
# b = bin(111011)
#
#
# print(int(_hex) ^ int(_valid) == 0)
# print(~int(_valid))
# print(len('1110110110001011101101100010110001000110100100110111011'))
#
# for i in range(0, 8, 2):
#     print(i)

# ###########################################################################################
# def swap(n=0):
#     global result
#     if n == N:
#         result = max(result, int(''.join(board)))
#         return
#     memo = (n, tuple(board))
#     if memo in memoization:
#         return
#     memoization.add(memo)
#     for i in range(M - 1):
#         for j in range(i + 1, M):
#             board[i], board[j] = board[j], board[i]
#             swap(n + 1)
#             board[i], board[j] = board[j], board[i]
#
#
# T = int(input())
# for case_num in range(1, 1 + T):
#     a, b = input().split()
#     board = list(a)
#     N = int(b)
#     M = len(board)
#     result = 0
#     memoization = set()
#     swap()
#     print(f'#{case_num} {result}')

# ###########################################################################################
# from collections import defaultdict
# from heapq import heappush, heappop
# import sys
# sys.stdin = open('input.txt')
#
# N = int(input())   # 도시 개수
# M = int(input())   # 버스 개수 (간선 개수)
# graph = defaultdict(list)
#
# for _ in range(M):
#     s, e, d = map(int, input().split())
#     graph[s].append((d, e))     # 양방향이 아니야 이 라만릊댜매ㅜ햗ㄱ
#     # graph[e].append((d, s))
#
# start, end = map(int, input().split())
#
#
# def dijkstra(start, graph):
#     distance = [float('inf')] * (N + 1)   # 1~N city
#     distance[start] = 0
#     pq = [(0, start)]    # 비용, 시작
#
#     while pq:
#         current_dist, current_node = heappop(pq)
#         if distance[current_node] < current_dist:
#             continue
#
#         for next_distance, next_node in graph[current_node]:
#             new_distance = current_dist + next_distance
#             if new_distance < distance[next_node]:
#                 distance[next_node] = new_distance
#                 heappush(pq, (new_distance, next_node))
#
#     return distance
#
#
# result = dijkstra(start, graph)
# print(result)

# ##############################################################################################

#
# def find(parent, a):
#     root = a
#     while parent[root] != root:
#         root = parent[root]
#
#     while parent[a] != a:
#         next_node = parent[a]
#         parent[a] = root
#         a = next_node
#
#     return root
#
# rank = [0] * (n + 1)
# def union(parent, rank, a, b):
#     root_a = find(parent, a)
#     root_b = find(parent, b)
#     if root_a != root_b:
#         if rank[root_a] < rank[root_b]:
#             parent[root_a] = root_b
#
#         elif rank[root_a] > rank[root_b]:
#             parent[root_b] = root_a
#         else:
#             parent[root_b] = root_a
#             rank[root_a] += 1
#     return
#
#
# parent = []
#

# ########################################################################################
# sort 연습

# arr = [4, 3, 2, 8, 10]
# .sort(), sorted()   ->    sort 는 반환값 없고, sorted 는 정렬한 (*중요*) 새로운 (*중요*) list 반환
# sorted(arr) -> [2, 3, 4, 8, 10]   but arr 은 그대로!!!

# 특정 조건이 존재할 때, 정렬 조건을 (key) 에 넣어주어야 한다.
# lambda: 익명 함수 (일회용 함수)
# - 파라미터, return 값
# - 앞 x(파라미터): 원본 배열의 값 하나하나
# - 뒤 x(return 값): 정렬 기준
#
# # 예시 1. 짝수 우선 정렬
# arr = [4, 3, 7, 1, 2, 5, 8, 10]
# arr.sort(key=lambda x: x % 2)
# print(arr)      # [4, 2, 8, 10, 3, 7, 1, 5]
#
# # 예시 2. 짝수 우선 정렬 + 오름차순
# arr.sort(key=lambda x: (x % 2, x))   # 앞 기준( x % 2 ) 우선 정렬 후, 뒤에 있는 기준( x )으로 정렬
# print(arr)      # [2, 4, 8, 10, 1, 3, 5, 7]

# ######################################################################

# 월말 예상
# 완전 탐색
# 백트래킹
# 그래프 -dfs, bfs
# 트리 - 이진 트리     ->>>>>  넘 쉽당
# ---------------------------------------------------------------------------------------------------
# 다익스트라
# mst - prim, kruskal
# union find     ->>>>    kruskal  중점 공부!   (kruskal + union find)
# ---------------------------------------------------------------------------------------------------
# ㅅㅅㅎ
# dfs, bfs 차이점? ex. 어느 상황에서 쓰는가, 순회 순서 차이

# ######################################################################

# django

# 가상환경 
# python -m venv venv    ->    위치에 venv 생성
# source venv/Scripts/activate    ->    venv 활성화
# deactivate    ->    venv 비활성화
# pip freeze > requirements.txt    ->    의존성 기록해서 requirements.txt 생성
# pip install -r requirements.txt    ->    requirements.txt 읽어와서 의존성 패키지 설치
# pip install django    ->    django 설치


# 프로젝트 / 앱 시작
# django-admin startproject firstpjt .    ->    현 위치에 firstpjt 프로젝트 생성
# django-admin startproject firstpjt    ->    현 위치 아래 폴더로 firstpjt 프로젝트 생성
# python manage.py startapp appname    ->    appname 이름의 앱 생성
    # 앱 생성한 후에 등록 꼭 하기!    ->    /settings.py => INSTALLED_APPS = [] 에 'appname',
    # ',' 콤마 뒤에 추가 꼭꼭!


# 서버
# python manage.py runserver    ->    서버 시작
# ctrl + c    ->    종료


# 요청 / 응답
    # URL -> View -> Template   순으로 항상 습관 들이기
# 프로젝트에 urls.py
    # 나중에 앱이 많아지면 관리 용이하게 하기 위해 각 앱에 urls.py 만들어서 관리할거임
    # 프로젝트에 있는 urls.py는 각 앱에 있는 urls.py 로 넘겨주게

# from django.contrib import admin
# from django.urls import path, include    ---->> include 추가

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('bakeries/', include('bakeries.urls'))    ---->> bakeries 앱에 있는 urls.py 로 넘기기 
# ]

# 앱에 있는 urls.py
# from django.urls import path
# from . import views    ---->> from . => 명시적 경로 위해, 현 디렉토리에서 ~ 라는 의미
# ---->> import views => views 에 있는 함수들 가져올꺼니까 views 를 import 하기

# app_name='bakeries'     ---->> url 앱 이름 
# urlpatterns = [
#     path('', views.index, name='index'),    ---->> views의 index 함수로 넘김
#     path('<int:id>/', views.detail, name='detail'),    ---->> views의 detail 함수로 넘김
            # <int:id>  ---->>   이름 id 인 int형 변수를 같이 넘겨줄거임 
# ]


#앱에 있는 views.py
# from django.shortcuts import render, get_object_or_404   ---->> 에러 상황 위해 get_object_or_404 추가
# from .models import Bakery    ---->> db 에 있는 data 사용 위해 .models 에 있는 Bakery, class 가져옴 

# def index(request):      ---->> views.index 로 들어오면 이거 실행  request는 그냥 기본이라 생각해라
#     bakeries = Bakery.objects.all()    ---->> Bakery 전체 데이터 조회     
#     context = {                        ---->> 넘겨주는 context
#         'bakeries': bakeries 
#     }
#     return render(request, 'bakeries/index.html', context)    ---->> request, context 넘기면서 html 띄우기

# def detail(request, id):    ---->> detail은 <int:id> 인자도 받으니까 request, id
#     bakery = get_object_or_404(Bakery, id=id)    # Bakery 에서 id 조회  없으면 404   
#     context = {
#         'bakery': bakery,                     
#     }
#     return render(request, 'bakeries/detail.html', context)



# templates    ---->>  여기에 html들 만들어 놓기
# 앱이 많아지면 구분 잘 하려고 template 밑에 앱 이름으로 폴더 하나 걍 만들고 거기에 html
# templates/bakeries/index.html  이런 경로




# 상속 - hmtl 페이지 만들 때 기본틀, 전체 페이지들이 공유하는 공통 요소 만들고 상속시키기위해
# 프로젝트랑 같은 위치에 layout 폴더 생성
    # 생성 후 꼭! settings.py 에 TEMPLATES 에 'DIRS'에 추가
    # template 검색할 때 BASE_DIR 밑에 있는 'layout' 폴더도 봐라... 라는 뜻
# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [BASE_DIR / 'layout'],   
# ...

# layout 에 기본 틀로 쓸 base.html 생성
# <!DOCTYPE html>
# <html lang="en">
# <head>
#   <meta charset="UTF-8">
#   <meta name="viewport" content="width=device-width, initial-scale=1.0">
#   <title>Document</title>
# </head>
# <body>
#   <nav>
#     <a href="{% url 'bakeries:index' %}">Home</a>
#     <a href="">Create</a>
#   </nav>
#   <h1>빵집 추천</h1>
#
#   {% block content %}    # 페이지마다 달라지는 영역은 block 으로
#   {% endblock content %}
#
# </body>
# </html>

# index.html 예시
# {% extends "base.html" %}    ---->> base.html 에서 상속 받는다는 느낌
#
# {% block content %}    ---->> base.html 중 block 안쪽 부분 다음으로 채우겠다...    
#     <h2>메인 페이지</h2>
#
#     {% for bakery in bakeries %}    ---->> for 문 사용 위한 django html language
#   
#     <hr>
#     <p>이름 : <a href="{% url 'bakeries:detail' bakery.id %}">{{ bakery.name }}</a></p>
#     <p>평점 : {{ bakery.rating }}</p>
#     <hr>
#                         # context 로 받아온거 변수로 쓸 수 있음
#     {% endfor %}
# {% endblock content %}


# <p>이름 : <a href="{% url 'bakeries:detail' bakery.id %}">{{ bakery.name }}</a></p>
# {% url 'bakeries:detail' bakery.id %}    ---->> {% url  %} 로 url 가져오는디
    # 'bakeries:detail'    app_name='bakeries' 인 urls.py의 name='detail'인 url path
    # bakery.id 는 detail이 <int:id> 변수를 받으므로 넣어준거
    # space 로 변수 구분, 만약 많은 변수를 받는다면
    # {% url /ulr/ulr <int> <str> <float> %}   이런 형식으로



# models.py    ---->>  각 앱에서 DB 할라고 하는거
# class Bakery(models.Model):     # django에서 미리 만들어져있는 Model 에서 상속받아서 class 만들기 
#     # 빵집 이름 (20자 이내)
#     name = models.CharField(max_length=20)   # column 만들기 
                        # 각 column 에 어떤 데이터 넣을지는 model field 로 찾기 
#     # 주소
#     address = models.TextField()
#
#     # 평점 (예: 0.0 ~ 5.0 범위 예상, 소수점 1자리까지)
#     rating = models.FloatField()
#
#     # 시작/종료 시간
#     opening_time = models.DateTimeField()
#     closing_time = models.DateTimeField()
#
#     def __str__(self):
#         return f'{self.name} {self.rating}/10'

# 선언할거 다 해 놓고, 저장하고
# python manage.py makemigrations
# python manage.py migrate



# admin
# 관리자 페이지 볼 수 있게 관리자 계정 만드는거
# python manage.py createsuperuser
# 비번 쳐도 따로 표시는 안댐 당황하지 말기


# DTL


# CRUD
# db 데이터 관리 하는거
# Create, Read, Update, Delete
# 노션 보덩가

# ######################################################################

