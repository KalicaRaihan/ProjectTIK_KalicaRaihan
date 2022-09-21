from django.shortcuts import render

# Create your views here.
def Pascasarjana(request):
    judul = ["Pendidikan Bahasa Indonesia", "Teknologi Pembelajaran", "Ilmu Hukum", "Magister Administrasi Publik", "Magister Akuntansi", "Magister Manajemen", "Pendidikan Bahasa Inggris", "Pendidikan Matematika", "Ilmu Pertanian", "Ilmu Komunikasi"]

    konteks = {
        'judul': judul,
    }

    return render(request, 'Pascasarjana/indexpascasarjana.html', konteks)
