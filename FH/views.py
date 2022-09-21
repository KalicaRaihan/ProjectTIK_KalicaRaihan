from django.shortcuts import render

# Create your views here.
def FH(request):
    judul = ["Ilmu Hukum"]

    konteks = {
        'judul': judul,
    }
    return render(request, 'FH/indexfh.html', konteks)
