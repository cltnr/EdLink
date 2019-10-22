from django.shortcuts import render

# Create your views here.


def home(request):
    home_nav = "active"
    # context = {"home_nav": "active"}
    return render(request, "core/pages/home.html", locals())
