from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _ #get text ka use kar rahe hai assume karke k input multiple languages me aa sakta hai

#Custom User ka model ka banaya gaya hai yaha 

#inbuilt Abstract class ko customize kiya gaya
class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(_('user name'), max_length=150, unique=True)

#model k save hone me validation k liye
    def save(self, *args, **kwargs):
        self.full_clean() #saarey fields pe validation lagega woh field pe bhi jo model me nahi dikh rahi
        super().save(*args, **kwargs) #superclass ka jo save method hai usi ko call kiya gaya jissey save process hoga


#password kao validate kiya ja raha hai k input me koi exception ho toh kya return hona chahiye
    def validate_password(self):
        if not any(char.isdigit() for char in self.password):
            raise ValidationError(_("Password must contain at least one digit."), code='password_no_number')
        if not any(char.isupper() for char in self.password):
            raise ValidationError(_("Password must contain at least one uppercase letter."), code='password_no_upper')
        if not any(char.islower() for char in self.password):
            raise ValidationError(_("Password must contain at least one lowercase letter."), code='password_no_lower')
        if len(self.password) < 8:
            raise ValidationError(_("Password must be at least 8 characters long."), code='password_too_short')
        
#custom validation lagaye hai jo password pe uss function ko call karne k liye clean method ka use kiye hai
    def clean_password(self):
        self.validate_password()
        return self.password
