"""
어노테이션을 찾아서 메소드를 호출
사용자 요청===> DispatcherServlet ===>Model(@Controller) => ViewResolver

사용자 요청 ===>urls ====>함수 ===>HTML
                |       ------
                            |views <==> models(DAO)
             요청 사이트 = > 어떤 함수 호출 = > 지정
 manage.py => 서버 동작(실행) python manage.py runserver
 urls.py => 함수 호출 =>@RequestMapping
 -------------------------------------------
 views.py =>@Controller
 models.py = > @Repository
 -------------------------------------------

 =>서버 =>JSON =>React/Vue
                        => {{}} = > [[]]
 =>파일 제어
 =>한 가지만 명확 하게 사용이 가능 =>ORM

 1.파이썬 =>자료 구조 : 코딩 테스트
    =>list ==[]
    =>tuple ==() = > 데이터 베이스
    =>dict =={키:값}=>JSON = > 웹


import django
=>import java.util.*
from django.urls import path
=>import java.util.scanner
"""
from django.urls import path
from web import views,food_views,recipe_views
#localhost:8000
urlpatterns=[
path('',views.main_page),
path('food/list/',food_views.food_list),
path('food/find/',food_views.food_find),
path('recipe/list/',recipe_views.recipe_list_view),
path('recipe/list_vue/',recipe_views.recipe_llist)
]