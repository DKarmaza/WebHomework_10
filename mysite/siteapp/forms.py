from django import forms
from .models import Author, Quote
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Форма для реєстрації користувача
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# Форма для додавання автора
class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'biography']

# Форма для додавання цитати
class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ['text', 'author']
