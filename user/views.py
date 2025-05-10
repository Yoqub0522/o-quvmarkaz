from django.contrib.auth import logout,login
from django.shortcuts import render, redirect

from user.forms import UserForm


def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form = UserForm()  # bu GET so‘rov uchun
    return render(request, 'register.html', {'form': form})  # bu umumiy qaytish


from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('course-list')  # login bo‘lsa, yo‘naltiramiz
        else:
            error = "Login yoki parol noto‘g‘ri"
            return render(request, 'login.html', {'error': error})
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('course-list')