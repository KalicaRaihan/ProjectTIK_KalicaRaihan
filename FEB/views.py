from django.shortcuts import render

# Create your views here.
def FEB(request):
    judul = ["Marketing", "Akuntansi", "Perpajakan", "Keuangan Perbankan"]

    konteks = {
        'judul' : judul,
    }

    return render(request, 'FEB/indexfeb.html', konteks)
