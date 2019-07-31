from django.urls import path, include
from . import views

from rest_framework.documentation import include_docs_urls

app_name = 'study'

urlpatterns = [
    path('register', views.RegisterView.as_view(), name='register'),  # 注册接口

    path('api-auth/', include('rest_framework.urls')),  # api browsable rest_framework
    path('docs/', include_docs_urls(title="six413")),

    path('test', views.Test.as_view(), name='test'),  # test django rest framework
    path('drf', views.Drf.as_view(), name='drf'),

    path('', views.RegisterView.as_view(), name='index'),  # 测试页面
]