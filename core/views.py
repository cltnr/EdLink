import random
import string

from django.shortcuts import render

from EdLink.local_settings import APP_NAME
from .forms import LinkAdd
from .models import Link


# Create your views here.


def home(request):
    home_nav = "active"
    # context = {"home_nav": "active"}
    app_url = APP_NAME
    form = LinkAdd(request.POST or None)
    if form.is_valid():

        def randomLink(lenght):
            exists = True
            while exists == True:
                link = ''.join(random.choice(string.ascii_letters) for i in range(lenght))
                if not Link.objects.filter(link=link).exists(): exists = False
            return link

        exists = False
        link = form.cleaned_data["link"]
        target = form.cleaned_data["target"]

        if link == "":
            if Link.objects.filter(link=link).exists():



        # if Link.objects.filter(name=name).exists():
        #     exists = True
        # else:
        #     link = Link(name=name, url=url).save()

    return render(request, "core/pages/home.html", locals())
