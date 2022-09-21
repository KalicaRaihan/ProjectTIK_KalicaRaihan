from django.shortcuts import render

# Create your views here.
def FISIP(request):
    judul = ["Administrasi Publik", "Ilmu Komunikasi", "Ilmu Pemerintahan"]
    
    konteks = {
        'judul':judul,
    }
    return render(request, 'FISIP/indexfisip.html', konteks)
