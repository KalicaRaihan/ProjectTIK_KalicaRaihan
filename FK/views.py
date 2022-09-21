from django.shortcuts import render

# Create your views here.
def FK(request):
    judul = ["Kedokteran", "Keperawatan", "Ilmu Gizi", "Ilmu Keolahragaan"]

    konteks = {
        'judul': judul,
    }

    return render(request, 'FK/indexfk.html', konteks)
