from django.shortcuts import render, redirect
from .models import User, StudyRecord
from django.urls import reverse
import re
from django.conf import settings
from django.http import JsonResponse
from django.views.generic import View


# Create your views here.
def index(request):
    """测试首页"""
    return render(request, 'study/index.html', {'test': 'test'})


# /register
class RegisterView(View):
    """注册"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.resp_json = {'status': 0, 'msg': 'success'}

    def post(self, request):
        """用户注册处理"""
        # 接收数据
        username = request.POST.get('username')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        email = request.POST.get('email')
        print(username, password, cpassword, email)

        # 数据校验
        # 数据完整性校验
        if not all([username, password, email]):
            self.resp_json['status'] = -1
            self.resp_json['msg'] = '参数不足'
            ret = JsonResponse(self.resp_json)
            return ret
        # 校验邮箱
        if not re.match(r'^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}', email):
            self.resp_json['status'] = -1
            self.resp_json['msg'] = '邮箱格式有误'
            ret = JsonResponse(self.resp_json)
            return ret
        # 校验密码
        if password != cpassword:
            self.resp_json['status'] = -1
            self.resp_json['msg'] = '两次输入的密码不一致'
            ret = JsonResponse(self.resp_json)
            return ret
        # 校验用户名、邮箱是否重复
        try:
            e = User.objects.get(email=email)
        except User.DoesNotExist:
            # 邮箱不重复，可用
            e = None

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            # 用户名不存在，可用
            user = None

        if user or e:
            # 用户已存在
            self.resp_json['status'] = -1
            self.resp_json['msg'] = '用户或邮箱已被注册'
            ret = JsonResponse(self.resp_json)
            return ret

        # 校验完成，把信息存进数据库
        user = User.objects.create_user(username, email, password)
        user.save()

        # TODO 发送激活邮件

        # 返回成功信息
        self.resp_json['status'] = 0
        self.resp_json['msg'] = '注册成功'
        self.resp_json['user_info'] = {'username': username, 'email': email}
        ret = JsonResponse(self.resp_json)
        return ret
