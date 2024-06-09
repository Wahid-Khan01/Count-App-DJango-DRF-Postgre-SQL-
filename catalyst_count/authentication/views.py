from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

def signup(request):
    if request.method == 'POST': #check karega method post hai ya nahi
        form = UserCreationForm(request.POST) #inbuilt form ka use kar rahe hai
        if form.is_valid(): #will validate the input
            form.save() #will save the user details to the db
            return redirect('account_login')  # Redirect to login page after successful signup
    else:
        form = UserCreationForm() #re initialize kar rahe hai form ko
    return render(request, {'form': form}) #form ko bhej rahe template me 

def login(request):
    if request.method == 'POST': #check karega method post hai ya nahi
        form = AuthenticationForm(data=request.POST) #inbuilt form ka use kar rahe hai
        if form.is_valid(): #will validate the input
            user = form.get_user() #ek baar validate hojayega toh uss detail k user ko get kar rahe hai
            login(request, user) #user ko inbuilt login ki madad se login kara rahe hai
            return redirect('/')  # Redirect to home page after successful login
    else:
        form = AuthenticationForm() #form ko reinitialize kara rahe hai yaha 
    return render(request, {'form': form}) # form ko bhej rahe hai template me


