
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from authentication.models import CustomUser
from .forms import CustomUserCreationForm
from django.http import HttpResponse

@login_required
def user_list(request):
    if request.user.is_staff or request.user.is_superuser:
        users = CustomUser.objects.all()
        return render(request, 'user_management_temp/users.html', {'users': users})
    else:
        return HttpResponse("<h2>The information is confidential.Only for Staff Users. <a href='/accounts/login/'>Back To Home</a></h2>")

#inbuilt decorators me se login required or staff member required decorator ka use kiya gaya hai
@login_required
@staff_member_required
def user_delete(request, user_id):
    user = CustomUser.objects.get(id=user_id) #fetch karega user ko id se
    user.delete() #user ko delete kardega
    return redirect('user_list')

@login_required
@staff_member_required
def add_user(request):
    form = CustomUserCreationForm(request.POST) #jo cutom form banaya gaya tha uska object banaye
    if request.method == 'POST': #check karega method post hai ya nahi
        if form.is_valid(): #form ko validate karega ki input barabar aay ahai ya nahi
            form.save() # form ko save kardega 
            return redirect('add_user')
    else:
        form = CustomUserCreationForm() #form ko reinitialize kiya gaya hai 
        
    return render(request, 'user_management_temp/users.html', {'form': form, 'users': CustomUser.objects.all()}) 
#template render karne k sath usme form bhej rahe hai or CustomUser table me jitne user hai unko dikha rahe hai