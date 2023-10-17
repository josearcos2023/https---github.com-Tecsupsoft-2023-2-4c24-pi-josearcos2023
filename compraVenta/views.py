from django.shortcuts import render,redirect
from .forms import NewUserForm
from django.contrib.auth import login,authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def index(request):
    return render(request=request,template_name='index.html')

def registro(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registro exitoso")
            return redirect("login")
        else:
            print(form.errors)
            messages.error(request, "Registro inválido")
    else:
        form = NewUserForm()

    return render(request=request, template_name="registro.html", context={"formulario": form})


def registroLogin(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                messages.info(request, f"Has ingresado con la cuenta de {username}.")
                return redirect("index")
            else:
                messages.error(request, "Usuario o contraseña inválida.")
        else:
            messages.error(request, "Usuario o contraseña inválida.")
    else:
        form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login": form})