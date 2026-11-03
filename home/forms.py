from django import forms
from products.models import UserProfile

class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile

        fields = [
            "theme",
            "title",
            "first_name",
            "surname",
            "address",
            "phone",
        ]

        widgets = {
            "address": forms.Textarea(
                attrs={
                    "rows": 3,
                    "placeholder": "Enter your address..."
                }
            ),
        }
