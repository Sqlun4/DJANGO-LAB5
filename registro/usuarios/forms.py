from django import forms

class RegistroUsuariosForm(forms.Form):
    nombre_usuario = forms.CharField(max_length=150)
    email = forms.EmailField()
    contrasena = forms.CharField(widget = forms.PasswordInput)
    contrasena_confirmar = forms.CharField(widget = forms.PasswordInput)
    fecha_nacimiento = forms.DateField(widget = forms.TextInput(attrs = {'class': 'datepicker'}))

    #funcion para validare email
    def clean_email(self):
        email=self.cleaned_data.get('email')
        if email == "existe@gmail.com":
            raise forms.ValidationError("Este correo ya fue registrado")
        return email

    #funcion para validar contraseña
    def clean_contrasena(self):
        contrasena = self.cleaned_data.get('contrasena')
        if len(contrasena)<8:
            raise forms.ValidationError("La contraseña debe tener al menos 8 caracteres")
        return contrasena

    #validacoion confirma contraseña
    def clean_contrasena_confirmar(self):
        contrasena = self.cleaned_data.get('contrasena')
        contrasena_confirmar = self.cleaned_data.get('contrasena_confirmar')

        if contrasena!=contrasena_confirmar:
            raise forms.ValidationError('Las contraseñas no son iguales')
        return contrasena_confirmar