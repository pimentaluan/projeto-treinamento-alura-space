from django import forms

class LoginForms(forms.Form):
    matricula = forms.CharField(
        label="Matrícula",
        required=True,
        max_length=100,
    )
    senha = forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput()
    )