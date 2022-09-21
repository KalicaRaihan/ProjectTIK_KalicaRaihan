from django.shortcuts import render

# Create your views here.
def FT(request):    
    judul = ["Teknik Elektro", "Teknik Industri", "Teknik Kimia", "Teknik Mesin", "Teknik Metalurgi", "Teknik Sipil"]

    konteks = {
        'judul': judul,
    }

    return render(request, 'FT/indexft.html', konteks)

