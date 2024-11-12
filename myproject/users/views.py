from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def register(request):
    # Check if the form is submitted
    if request.method == "POST":
        form = UserCreationForm(request.POST) # Submitted with data
        if form.is_valid():
            form.save()
            return redirect("posts:list")
    else:
        form = UserCreationForm
    context = {
        'active_link': 'register',
        'form': form
    }
    return render(request, 'users/register.html', context)