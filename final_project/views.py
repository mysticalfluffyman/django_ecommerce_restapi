from django.shortcuts import render

def home(request):
    template_dir= "login.html"
    datas = {"name":"project"}
    return render(request,template_dir,datas)