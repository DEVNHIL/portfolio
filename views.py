from django.shortcuts import render

projects = ["sample 1", "sample 2", "sample 3"]
# Create your views here.

def index(request):
    return render(request, "portfolio/index.html", {
        "projects": projects
    })