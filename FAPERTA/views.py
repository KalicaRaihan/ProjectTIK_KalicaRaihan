from django.shortcuts import render

# Create your views here.
def FAPERTA(request):
    judul = ["Agribisnis", "Agroteknologi", "Ilmu Perikanan", "Teknologi Pangan"]

    konteks = {
        'judul': judul,
    }

    return render(request, 'FAPERTA/indexfaperta.html', konteks)

