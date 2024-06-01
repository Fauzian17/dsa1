from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import User,Group
from django.contrib.auth.hashers import make_password

@csrf_protect
def akun_login(request):
    # Cek jika pengguna sudah terautentikasi
    if request.user.is_authenticated:
        return redirect('/')
    
    template_name = "halaman/login/login.html"
    pesan = ''
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            pesan = "Login Gagal"
    
    # Pastikan konteks terbentuk dan di-render dalam kedua kasus (GET dan POST)
    context = {
        'pesan': pesan
    }
    return render(request, template_name, context)


def akun_registrasi(request):
    if request.user.is_authenticated:
        return redirect('/')
    
    pesan = ''
    template_name = "halaman/login/register.html"
    
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if password == password:
            if User.objects.filter(username=username).count() == 0:
                User.objects.create(
                    username=username,
                    email=email,
                    password=make_password(password), # type: ignore
                    is_active=True
                )
                return redirect('/')      
            else:
                pesan = 'Username sudah ada'
        else:
            pesan = 'Password tidak sama'
    
    context = {
        'pesan': pesan
    }
    return render(request, template_name, context)

def akun_logout(request):
    logout(request)
    return redirect('/')
