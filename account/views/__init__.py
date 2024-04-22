from . import dashboard
from account import forms
from django.contrib import auth, messages
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect


def signout_view(request):
    auth.logout(request)
    return redirect("landing:index-view")


def signin_view(request):
    if request.method == "POST":
        user = auth.authenticate(
            request,
            username=request.POST.get("username"),
            password=request.POST.get("password"),
        )

        if user and user.groups.count():
            auth.login(request, user)
            return redirect("landing:index-view")

        messages.error(request, "Invalid credentials or inactive user")
        return redirect("account:signin-view")

    return render(request, "account/signin.html")


def signup_view(request):
    if request.method == "POST":
        role = request.POST.get("role")
        form = forms.RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            user.groups.add(Group.objects.get_or_create(name=role)[0])

            return redirect("account:signin-view")

        [messages.error(request, val) for val in form.errors.values()]
        return redirect("account:signup-view")

    return render(request, "account/signup.html")
