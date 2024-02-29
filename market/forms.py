from django import forms
from django.core.exceptions import ValidationError
from django.forms import Form

from market.models import Product, Author


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class AuthorLoginForm(Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"id": "username"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"id": "password"}))


class AuthorRegistrationForm(forms.ModelForm):
    password1 = forms.CharField(max_length=28, widget=forms.TextInput(
        attrs={"type": "password", "id": "password1"}))
    password2 = forms.CharField(max_length=28, widget=forms.TextInput(
        attrs={"type": "password", "id": "password2"}))
    avatar = forms.FileField()

    def save(self, commit=True):
        user = super().save(commit)
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 == password2:
            user.set_password(password1)
            user.save()
        else:
            raise ValidationError("Passwords must be match")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control"})

    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'username', 'avatar']
