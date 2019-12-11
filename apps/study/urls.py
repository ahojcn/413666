from django.urls import path
from . import views

app_name = 'study'

urlpatterns = [
    path('getCSRFToken/', views.get_csrftoken, name='get-csrftoken'),
    path('register/', views.RegisterView.as_view(), name='register'),  # 注册接口
    path('login/', views.LoginView.as_view(), name='login'),  # 登录接口
    path('', views.index, name='index'),  # 测试页面
]