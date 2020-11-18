from django.shortcuts import render,HttpResponse
import json

# 打开index.html页面
def index(request):
    return render(request,"index.html")

# 打开登录页面
def open_login(request):
    return render(request, "login.html")

# 打开注册页面
def open_reg(request):
    return render(request,"reg.html")

# 登录（用户名和密码的判断）
def login(request):
    result = {"code":-1,"msg":"用户名不存在"}
    # 获取用户名和密码
    username = request.POST.get("username")
    password = request.POST.get("password")
    # 开始判断(用户名：abcd，密码：123)
    if username == "abcd":
        if password == "123":
            result["code"] = 0
            result["msg"] = "密码正确"
        else:
            result["code"] = -2
            result["msg"] = "密码错误"
    return HttpResponse(json.dumps(result))