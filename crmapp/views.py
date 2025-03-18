from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Iniciaste sesion correctamente")
            return redirect("home")
        else:
            messages.success(request, "Usuario o contraseña incorrecto")
            return redirect("login")
    else:
        return render(request, "login.html", {})


def home_view(request):
    records = Record.objects.all()

    return render(request, "home.html", {"records": records})


def logout_view(request):
    logout(request)
    messages.success(request, "Ha cerrado sesion")
    return redirect("login")


def register_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Inicia sesion luego de registrarse exitosamente
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Se ha registrado exitosamente")
            return redirect("home")
    else:
        form = SignUpForm()
        return render(request, "register.html", {"form": form})
    return render(request, "register.html", {"form": form})


def customer_record(request, pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        return render(request, "record.html", {"customer_record": customer_record})
    else:
        messages.success(request, "Debes de iniciar sesion para ver esta pagina")
        return redirect("home")


def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Se elimino correctamente")
        return redirect("home")
    else:
        messages.success(request, "Debes iniciar sesion para eliminar el registro")
        return redirect("login")


def add_record(request):
    if request.user.is_authenticated:
        form = AddRecordForm(request.POST or None)
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Se ha registrado correctamente")
                return redirect("home")
        else:
            return render(request, "add_record.html", {"form": form})
    else:
        messages.success(request, "Debes iniciar sesion")
        return redirect("login")


def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Se ha actualizado con exito")
            return redirect("home")
        return render(request, "update_record.html", {"form": form})
    else:
        messages.success(request, "Debes iniciar sesion")
        return redirect("login")
