import random
import string

from django.shortcuts import render


def home(request):
    return render(request, "password/home.html", {"lengths": range(6, 15)})


def password(request):
    symbols = list(string.ascii_lowercase)

    if request.GET.get("uppercase"):
        symbols.extend(string.ascii_uppercase)
    if request.GET.get("numbers"):
        symbols.extend(string.digits)
    if request.GET.get("special"):
        symbols.extend("!@#$%&*?")

    try:
        length = int(request.GET.get("length", 12))
    except ValueError:
        length = 12

    if length < 6:
        length = 6
    if length > 14:
        length = 14

    generated_password = "".join(random.choice(symbols) for i in range(length))
    return render(request, "password/password.html", {"password": generated_password})
