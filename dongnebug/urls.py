"""dongnebug24 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from django.contrib.auth.views import LoginView
from .views import *
from allauth.account.views import LogoutView
app_name = 'dongnebug'

urlpatterns = [
    path('', LoginView.as_view(template_name='loegin.html'), name='login'),
    path('search/', SearchView.as_view(), name='search'),
    path('index/', IndexView.as_view(), name='index'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('complain/', ComplainListView.as_view(), name='complain_list'),
    path('complain/<int:pk>/', ComplainDetailView.as_view(), name='complain_detail'),
    path('complain/<int:pk>/sympathy/', complain_sympathy, name='complain_sympathy'),
    path('complain/new/', ComplainCreateView.as_view(), name='complain_new'),
    path('knockedbuk/', KnockedBukView.as_view(), name='knockedbuk'),
    path('uploadedcomplain/', UploadedComplainListView.as_view(), name='uploadedbuk'),
    path('complain/<int:pk>/comment/new/', CommentCreateView.as_view(), name='create_comment'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='update_profile'),
    path('certification/redirect/', CertificationRedirectView.as_view(), name='certification' ),
    path('certification/create/', CertificationCreateView.as_view(), name='certification' ),
    path('certification/update/<int:pk>/', CertificationUpdateView.as_view(), name='certification' ),
]
