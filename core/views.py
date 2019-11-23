from django.shortcuts import render
from .models import Link
from .forms import LinkAdd
from django.contrib.sites.shortcuts import get_current_site


# Create your views here.


def home(request):
    home_nav = "active"

    # context = {"home_nav": "active"}
    app_url = get_current_site(request).domain
    print(app_url)
    form = LinkAdd(request.POST or None)
    if form.is_valid():
        error = False
        user_data = form.cleaned_data["nom"]
        if Link.objects.filter(name=user_data).exists():
            error = True
        else:
            marque = Link(name=user_data).save()

    return render(request, "core/pages/home.html", locals())
