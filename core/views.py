import random
import string

from django.shortcuts import render, redirect

from EdLink.local_settings import APP_NAME
from .forms import LinkAdd
from .models import Link


# Create your views here.xx


def home(request):
    def link_exists(link):
        return Link.objects.filter(link=link).exists()

    def random_link(length):
        random_exists = True
        random_link = ""
        while random_exists:
            random_link = "".join(
                random.choice(string.ascii_letters + string.digits)
                for i in range(length)
            )
            if not link_exists(random_link):
                random_exists = False
        return random_link

    home_nav = "active"
    app_url = APP_NAME
    form = LinkAdd(request.POST or None)
    # form.fields['link'].initial = random_link(9)

    if form.is_valid():
        exists = False
        input_link = form.cleaned_data["link"]
        input_target = form.cleaned_data["target"]

        if not input_target.startswith("http://") and not input_target.startswith(
            "https://"
        ):
            final_target = "http://" + input_target
        else:
            final_target = input_target

        # Si l'user ne donne pas de lien
        if input_link == "":
            link = Link(link=random_link(8), target=final_target).save()

        # Si l'user donne un lien et que
        else:
            # Le lien n'existe pas déjà
            if not link_exists(input_link):
                link = Link(link=input_link, target=final_target).save()
            # Le lien existe déjà : on en propose un random
            else:
                form = LinkAdd(None)
                form.fields["target"].initial = input_target
                form.fields["link"].initial = random_link(9)
                custom_link_exists = True
                return render(request, "core/pages/home.html", locals())

        return redirect("link_infos", input_link)
    return render(request, "core/pages/home.html", locals())


def link_infos(request, link_user):
    link = Link.objects.get(link=link_user)
    return render(request, "core/pages/link_stats.html", locals())


def link_redirect(request, link_user):
    link = Link.objects.get(link=link_user)
    link.views += 1
    link.save()
    return redirect(link.target)
