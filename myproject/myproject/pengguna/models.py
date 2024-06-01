from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Pendaftar(models.Model):
    user= models.OneToOneField(User,on_delete=models.CASCADE)
    nama = models.CharField(max_length=100)
    alamat = models.TextField()
    umur =models.IntegerField(blank=True,null=True)

    def __str__(self):
        return self.nama
    

class Formulir(models.Model):
    PROGRAM_CHOICES = [
        ('IT', 'Information Technology'),
        ('CS', 'Computer Science'),
        ('EE', 'Electrical Engineering'),
        ('ME', 'Mechanical Engineering'),
        # Add more programs as needed
    ]

    nama = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    tempat_lahir = models.CharField(max_length=255, blank=True, null=True)
    tanggal_lahir = models.DateField(default='')
    nik = models.CharField(max_length=16, blank=True, null=True)
    no_hp = models.CharField(max_length=15, blank=True, null=True)
    no_hp_ortu = models.CharField(max_length=15, blank=True, null=True)
    alamat = models.TextField(max_length=255, blank=True, null=True)
    kelurahan = models.CharField(max_length=255, blank=True, null=True)
    kecamatan = models.CharField(max_length=255, blank=True, null=True)
    kabupaten = models.CharField(max_length=255, blank=True, null=True, default='')  # Tambahkan default
    jenis_kelamin = models.CharField(max_length=10, choices=[('Laki-Laki', 'Laki-Laki'), ('Perempuan', 'Perempuan')], blank=True, null=True)
    prodi1 = models.CharField(max_length=50, choices=[
        ('S1 - Pendidikan Dokter', 'S1 - Pendidikan Dokter'),
        ('D4 - Analis Kesehatan', 'D4 - Analis Kesehatan'),
        ('S1 - Ilmu Kesehatan Masyarakat', 'S1 - Ilmu Kesehatan Masyarakat'),
        ('S1 - Gizi', 'S1 - Gizi'),
        ('S1 - PGSD', 'S1 - PGSD'),
        ('S1 - PGPAUD', 'S1 - PGPAUD'),
        ('S1 - Pendidikan Bahasa Inggris', 'S1 - Pendidikan Bahasa Inggris'),
        ('S1 - Akuntansi', 'S1 - Akuntansi'),
        ('S1 - Manajemen', 'S1 - Manajemen'),
        ('S1 - Sistem Informasi', 'S1 - Sistem Informasi'),
        ('S1 - Keperawatan', 'S1 - Keperawatan'),
        ('D3 - Keperawatan', 'D3 - Keperawatan'),
        ('D4 - Bidan', 'D4 - Bidan'),
        ('D3 - Kebidanan', 'D3 - Kebidanan')
    ], blank=True, null=True)
    prodi2 = models.CharField(max_length=50, choices=[
        ('S1 - Pendidikan Dokter', 'S1 - Pendidikan Dokter'),
        ('D4 - Analis Kesehatan', 'D4 - Analis Kesehatan'),
        ('S1 - Ilmu Kesehatan Masyarakat', 'S1 - Ilmu Kesehatan Masyarakat'),
        ('S1 - Gizi', 'S1 - Gizi'),
        ('S1 - PGSD', 'S1 - PGSD'),
        ('S1 - PGPAUD', 'S1 - PGPAUD'),
        ('S1 - Pendidikan Bahasa Inggris', 'S1 - Pendidikan Bahasa Inggris'),
        ('S1 - Akuntansi', 'S1 - Akuntansi'),
        ('S1 - Manajemen', 'S1 - Manajemen'),
        ('S1 - Sistem Informasi', 'S1 - Sistem Informasi'),
        ('S1 - Keperawatan', 'S1 - Keperawatan'),
        ('D3 - Keperawatan', 'D3 - Keperawatan'),
        ('D4 - Bidan', 'D4 - Bidan'),
        ('D3 - Kebidanan', 'D3 - Kebidanan')
    ], blank=True, null=True, default='')  # Tambahkan default
    prodi3 = models.CharField(max_length=50, choices=[
        ('S1 - Pendidikan Dokter', 'S1 - Pendidikan Dokter'),
        ('D4 - Analis Kesehatan', 'D4 - Analis Kesehatan'),
        ('S1 - Ilmu Kesehatan Masyarakat', 'S1 - Ilmu Kesehatan Masyarakat'),
        ('S1 - Gizi', 'S1 - Gizi'),
        ('S1 - PGSD', 'S1 - PGSD'),
        ('S1 - PGPAUD', 'S1 - PGPAUD'),
        ('S1 - Pendidikan Bahasa Inggris', 'S1 - Pendidikan Bahasa Inggris'),
        ('S1 - Akuntansi', 'S1 - Akuntansi'),
        ('S1 - Manajemen', 'S1 - Manajemen'),
        ('S1 - Sistem Informasi', 'S1 - Sistem Informasi'),
        ('S1 - Keperawatan', 'S1 - Keperawatan'),
        ('D3 - Keperawatan', 'D3 - Keperawatan'),
        ('D4 - Bidan', 'D4 - Bidan'),
        ('D3 - Kebidanan', 'D3 - Kebidanan')
    ], blank=True, null=True, default='')  # Tambahkan default
    foto = models.ImageField(upload_to='uploads/')

    def __str__(self):
        return self.nama