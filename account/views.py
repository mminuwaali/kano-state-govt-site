from django.contrib import auth, messages
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

        if user:
            auth.login(request, user)
            return redirect("landing:index-view")

        messages.error(request, "Invalid credentials")
        return redirect("account:signin-view")
    return render(request, "account/signin.html")


def signup_view(request):
    if request.method == "POST":
        pass
    return render(request, "account/signup.html")
