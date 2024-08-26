from django import forms
from .models import Review, Order
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.help_text = None


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        widgets = {
            'comment': forms.Textarea(attrs={'placeholder': 'Write your review here...'}),
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5, 'placeholder': 'Rate (1-5)'}),
        }

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['quantity']
        widgets = {
            'quantity': forms.NumberInput(attrs={'min': 1, 'placeholder': 'Quantity'}),
        }
