# myapp/views.py
from django.shortcuts import render, redirect
from .forms import UserInfoForm

def user_info_form(request):
    if request.method == 'POST':
        form = UserInfoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')  # Redirect to a success page
    else:
        form = UserInfoForm()

    return render(request, 'user_info_form.html', {'form': form})

def success_page(request):
    return render(request, 'success_page.html')
