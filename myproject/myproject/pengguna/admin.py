from django.contrib import admin
from .models import Formulir

class FormulirAdmin(admin.ModelAdmin):
    list_display = ['nama',
                    'email',
                    'tempat_lahir',
                    'tanggal_lahir',
                    'nik',
                    'jenis_kelamin',
                    'no_hp',
                    'no_hp_ortu',
                    'alamat',
                    'kelurahan',
                    'kecamatan',
                    'kabupaten',
                    'prodi1',
                    'prodi2',
                    'prodi3',
                    'foto']
    list_filter = ["nama"]

admin.site.register(Formulir, FormulirAdmin)