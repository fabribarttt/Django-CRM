from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record


# Formulario para registrar usuarios
class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        label="",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Correo"}
        ),
    )
    first_name = forms.CharField(
        label="",
        max_length=50,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Nombre"}
        ),
    )
    last_name = forms.CharField(
        label="",
        max_length=50,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Apellido"}
        ),
    )

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields["username"].widget.attrs["class"] = "form-control"
        self.fields["username"].widget.attrs["placeholder"] = "Usuario"
        self.fields["username"].label = ""
        self.fields[
            "username"
        ].help_text = ""  #'<span class="form-text text-muted"><small>Obligatorio. 150 caracteres o menos. Solo letras, dígitos y los símbolos @/./+/-/_.</small></span>'

        self.fields["password1"].widget.attrs["class"] = "form-control"
        self.fields["password1"].widget.attrs["placeholder"] = "Contraseña"
        self.fields["password1"].label = ""
        self.fields[
            "password1"
        ].help_text = ""  #'<ul class="form-text text-muted small"><li>Tu contraseña no puede ser demasiado similar a tu información personal.</li><li>Tu contraseña debe contener al menos 8 caracteres.</li><li>Tu contraseña no puede ser una contraseña de uso común.</li><li>Tu contraseña no puede ser completamente numérica.</li></ul>'

        self.fields["password2"].widget.attrs["class"] = "form-control"
        self.fields["password2"].widget.attrs["placeholder"] = "Confirmar contraseña"
        self.fields["password2"].label = ""
        self.fields[
            "password2"
        ].help_text = ""  #'<span class="form-text text-muted"><small>Ingresa la misma contraseña para verificar.</small></span>'


# Formularios para agregar clientes nuevos al crm


class AddRecordForm(forms.ModelForm):
    first_name = forms.CharField(
        label="",
        required=True,
        widget=forms.widgets.TextInput(
            attrs={"placeholder": "Nombre", "class": "form-control"}
        ),
    )
    last_name = forms.CharField(
        label="",
        required=True,
        widget=forms.widgets.TextInput(
            attrs={"placeholder": "Apellido", "class": "form-control"}
        ),
    )
    email = forms.CharField(
        label="",
        required=True,
        widget=forms.widgets.TextInput(
            attrs={"placeholder": "Correo", "class": "form-control"}
        ),
    )
    phone = forms.CharField(
        label="",
        required=True,
        widget=forms.widgets.TextInput(
            attrs={"placeholder": "Telefono", "class": "form-control"}
        ),
    )
    address = forms.CharField(
        label="",
        required=True,
        widget=forms.widgets.TextInput(
            attrs={"placeholder": "Direccion", "class": "form-control"}
        ),
    )
    city = forms.CharField(
        label="",
        required=True,
        widget=forms.widgets.TextInput(
            attrs={"placeholder": "Ciudad", "class": "form-control"}
        ),
    )
    state = forms.CharField(
        label="",
        required=True,
        widget=forms.widgets.TextInput(
            attrs={"placeholder": "Departamento", "class": "form-control"}
        ),
    )
    zipcode = forms.CharField(
        label="",
        required=True,
        widget=forms.widgets.TextInput(
            attrs={"placeholder": "Codigo postal", "class": "form-control"}
        ),
    )

    class Meta:
        model = Record
        exclude = ("user",)
