# usermanagement/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from authentication.models import CustomUser



#Custom form banaya gaya hai jisko Custom User model se jodd diya gaya hai jo authentication app ka model hai usko joda gaya hai taakey yaha se detail wahi pe save ho or user wahi add ho
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")

        user = CustomUser(password=password1)
        user.clean_password()

        return password2
