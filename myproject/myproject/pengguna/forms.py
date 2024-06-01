from django import forms
from .models import Formulir

class FormulirForm(forms.ModelForm):
    class Meta:
        model = Formulir
        fields = (
            'nama',
            'email',
            'tempat_lahir', 
            'tanggal_lahir', 
            'nik', 
            'no_hp', 
            'no_hp_ortu', 
            'alamat', 
            'kelurahan', 
            'kecamatan', 
            'kabupaten', 
            'jenis_kelamin', 
            'prodi1', 
            'prodi2', 
            'prodi3',
            'foto'
        )
        widgets = {
            "nama": forms.TextInput(attrs={'class':'form-control'}),
            "email": forms.EmailInput(attrs={'class':'form-control'}),
            "tempat_lahir": forms.TextInput(attrs={'class':'form-control'}),
            "tanggal_lahir": forms.DateInput(attrs={'class':'form-control', 'type': 'date'}),
            "nik": forms.TextInput(attrs={'class':'form-control'}),
            "no_hp": forms.TextInput(attrs={'class':'form-control'}),
            "no_hp_ortu": forms.TextInput(attrs={'class':'form-control'}),
            "alamat": forms.Textarea(attrs={'class':'form-control'}),
            "kelurahan": forms.TextInput(attrs={'class':'form-control'}),
            "kecamatan": forms.TextInput(attrs={'class':'form-control'}),
            "kabupaten": forms.TextInput(attrs={'class':'form-control'}),
            "jenis_kelamin": forms.Select(attrs={'class':'form-control'}),
            "prodi1": forms.Select(attrs={'class':'form-control'}),
            "prodi2": forms.Select(attrs={'class':'form-control'}),
            "prodi3": forms.Select(attrs={'class':'form-control'}),
            "foto": forms.FileInput(attrs={'class':'form-control'}),
        }

