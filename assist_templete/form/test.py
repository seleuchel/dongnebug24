from django import forms
class Nameform(form.Form):
    your_name = forms.CharField(lable='Your name', max_length=100, widget=forms.Textarea)



    #렌더링 결과에 (pyton -> html) form이나 submit 버튼은 없는데, 이들은 개발자가 직접 템플릿에 넣어줘야 함.


    '''
폼클래스를 템플릿에서 사용

<form action ="/your-name" method="post">
    {%csrf_token %}
    {{ form }}
    <input type="submit" value="Submit" />
</form>




폼을 처리하는 뷰는 2개
- 폼을 보여주는
- 폼을 처리하는 뷰
=> 하나로 통합 가능 (권장)


보여주는 폼과 제출된 폼을 구분하여 처리할 수 있어야함.
http 메소드로 장고는 구분.
뷰가 get : 처음 뷰르 ㄹ보여줌
뷰가 post로 요청 : 데이터가 담긴 제출된 폼으로 간주


{{ form}} 부문은 label과 input 엘리먼트 쌍으로 렌더링됨.
쌍으로 변환 시 3가지 추가 옵션
1. {{form.as_table}} #tr태그 ; 테이블 셀
2. {{form.as_p}} p태그
3. {{form.as_ul}} li태그

테이블이나 ul은 개발자가 추가해야함.


#url.py
from django.urls import path
from myapp.view import MyView


urlpatterns = [
    path('about/',Myview.as_view()),
]


        as_view() #장고 기본 제공 #디스패치도
            - 클래스의 인스턴스 생성
            -객체의 dispatch 호출


뷰의 코딩은
views.py 에 코딩하면 됨

from django.http import HttpResponse
from django.views.generic import view

class MyView(View):
    def get(self, request):
        return HttpResponse('result')



#클래스 뷰의 형태

from django.http import HttpResponse
from django.views.generic import view

class MyView(View):
    def get(self,request):
        return HttpResponse('result');
    def head(self, *args, **kwargs):





some_app/urls.py

from django.urls import path
from some_app.views import About view

urlpartterns = [
    path('about/', Aboutview.as_view()),
]


some_app/view.py

from django.views.generic import Templateview


class Aboutview(TemplateView):
    template_name = "about.html"





더 간단하게

some_app/urls.py

path 에 수정
path('about/', TemplateView.as_view(template_name="about.html")),



템플릿 뷰는 url 맞춰 해당 템플릿 파일의 내용만 보내줄 때 사용하는 제네릭 뷰



 클래스에서 오버라이딩 or as_view()로 오버 라이딩 가능



  공통된 로직을 미리 개발해 놓고 제공하는 뷰 : 제네릭 뷰 -> 클래스형 뷰



  장고가 제공하는 제네릭 뷰

  - BaseView : 뷰 클래스 생성, 다른 제네릭 뷰의 무보 클래스 제공
  Generi Display View : 객체의 리스트 보여주기, 특정 객체의 상세정보 보여주기
- Generic Edit View : 폼을 통해 객체를  생성, 수정 ,삭제하는 기능 제공
- Generic Date View : 날짜 기반 객체의 연/월/일 페이지로 구분해서 ㄹ보여줌




#클래스형 뷰

from django.http import HttpResponseReDirect
from django.shortcuts import render
from django.views.generic import view

class MyFormView(View):
    fomr_class = MyFormView
    initial = {'key': 'value'}
    template_name = 'form_template.html'

    def get(self,request, *args, *kwargs):
        form = self,form_class(initial=self,initial)
        return render(request.self.template_name, {'form':form})

    def post(self ..이하 동문):
        form - self.form_class(request.POST)
        if form.is_valid():
            #cleaned_data로 관련 로직 처리
            return HttpResponseredirect('/success/')
        return render(requets, self.template_name, {'form' : form}) #유효하지 않은 데이터를 가진 post



폼 처리용 제네릭 뷰 FormView


from django.views.generic.edit import FormView
from .forms impor MyForm


class MyFormView(FormView):
    form_class = MyForm
    template_name = 'form_template.html'
    success_url = '/tha/'

    def form_valid(self, form):
        #clearned data로 로직 처리
        return super(MyFormView, self).form_valid(form)



폼 뷰 사용하면 get(), post() 메소드 정의 안해도 됨.


유의해서 코딩해라

1. form_class : forms.py 파일 내의 클래스 명
2. template_name : 폼을 포함하여 렌더링할 템플릿 파일 이름
3. success_url : 처리 정상 완료 시 리다이렉트
4. form_valid() : 유효한 폼 데이터로 처리할 로직 코딩,  super() # 지정한 url로 리다이렉션 처리됨.


    '''
