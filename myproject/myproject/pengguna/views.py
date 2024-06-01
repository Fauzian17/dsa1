from django.shortcuts import render,redirect

from pengguna.models import Formulir
from pengguna.forms import FormulirForm


# Create your views here.

def home(request):
    template = "index.html"
    context = {
        'title': 'Home',
    }
    return render(request, template, context)

def formulir_list(request):
    template = "admin.html"
    formulir_list = Formulir.objects.all()
    print(formulir_list)
    context = {
        'title': 'Form Pendaftaran',
        'formulir_list': formulir_list
    }
    return render(request, template, context)

def akun_pengguna(request):
    template = "akun_pengguna.html"
    context = {
        'title': 'Akun Pengguna',
    }
    return render(request, template, context)

    

def formulir_view(request, kode_formulir):
    try:
        formulir = Formulir.objects.get(kode_formulir=kode_formulir)
        nama_formulir = formulir.nama  # Asumsi bahwa model Formulir memiliki field 'nama'
    except Formulir.DoesNotExist:
        nama_formulir = None
    context = {
        'title': 'Formulir',
        'nama_formulir': nama_formulir
    }
    return render(request, 'dashboard/snippets/formulir_view.html', context)


def create_formulir(request):
    if request.method == "POST":
        form = FormulirForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('formulir_view')  # Ganti dengan URL halaman sukses Anda
    else:
        form = FormulirForm()

    context={
        'form': form, 
        'title': 'Formulir Pendaftaran'
        }

    return render(request,'dashboard/snippets/formulir.html', context)


