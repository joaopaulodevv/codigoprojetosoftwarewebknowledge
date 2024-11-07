from django.shortcuts import render


def index(request):
    context = {
        "title": "Django example",
    }
    return render(request, "index.html", context)
def cadastro(request):
    return render(request,"cadastro.html")


def sobrenos(request):
    return render(request,"sobrenos.html")