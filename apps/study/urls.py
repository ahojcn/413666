from django.urls import path, include
from . import views

app_name = 'study'

urlpatterns = [
    path('register', views.RegisterView.as_view(), name='register'),  # 注册接口
    path('', views.RegisterView.as_view(), name='index'),  # 测试页面
]