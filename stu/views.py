from django.shortcuts import render

# 打开index.html页面
def index(request):
    return render(request,"index.html")

# 打开登录页面
def open_login(request):
    return render(request, "login.html")