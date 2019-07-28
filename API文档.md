**用户注册：**

方法：`POST`

地址：`/register`

参数：

```json
username：字符串，用户名
password：字符串，密码
cpassword：字符串，重复输入密码
email：字符串，邮箱
```

返回：status = 0 代表成功，status = -1 代表失败，失败的原因在 msg 中。

```json
# 成功
{
    "status": 0,
    "msg": "注册成功",
    "user_info": {
        "username": "ahojcn1",
        "email": "ahojcn@qq.com"
    }
}

# 失败有一下几种情况
# 1.
{
    "status": -1,
    "msg": "用户或邮箱已被注册"
}
# 2.
{
    "status": -1,
    "msg": "两次输入的密码不一致"
}
# 3.
{
    "status": -1,
    "msg": "参数不足"
}
# 4.
{
    "status": -1,
    "msg": "邮箱格式有误"
}
```

