from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from . import models


# Create your views here.
def user_list(request) -> HttpResponse:
    """All users list"""
    users_ = models.User.objects.all()
    context = {"users": users_}
    return render(
        request=request,
        template_name="users.html",
        context=context,
    )


def user_profile(request, pk) -> HttpResponse | HttpResponseRedirect:
    """user profile page"""
    if models.User.objects.get(id=pk):
        user_: models.User = models.User.objects.get(id=pk)
        context: dict[str, user_] = {"user": user_}
        return render(request=request, template_name="user.html", context=context)
    return redirect("users")
