from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())
def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())
def aritmetikasosial(request):
    template = loader.get_template('aritmetikasosial.html')
    return HttpResponse(template.render())
def bangunruangsisidatar(request):
    template = loader.get_template('bangunruangsisidatar.html')
    return HttpResponse(template.render())
def bangunruangsisilengkung(request):
    template = loader.get_template('bangunruangsisilengkung.html')
    return HttpResponse(template.render())
def bentukaljabar(request):
    template = loader.get_template('bentukaljabar.html')
    return HttpResponse(template.render())
def bidangkartesius(request):
    template = loader.get_template('bidangkartesius.html')
    return HttpResponse(template.render())
def bilangan(request):
    template = loader.get_template('bilangan.html')
    return HttpResponse(template.render())
def bilanganberpangkatdanbentukakar(request):
    template = loader.get_template('bilanganberpangkatdanbentukakar.html')
    return HttpResponse(template.render())
def fungsikuadrat(request):
    template = loader.get_template('fungsikuadrat.html')
    return HttpResponse(template.render())
def garisdansudut(request):
    template = loader.get_template('garisdansudut.html')
    return HttpResponse(template.render())
def himpunan(request):
    template = loader.get_template('himpunan.html')
    return HttpResponse(template.render())
def kekongruenandankesebangunan(request):
    template = loader.get_template('kekongruenandankesebangunan.html')
    return HttpResponse(template.render())
def lingkaran(request):
    template = loader.get_template('lingkaran.html')
    return HttpResponse(template.render())
def peluang(request):
    template = loader.get_template('peluang.html')
    return HttpResponse(template.render())
def penyajiandata(request):
    template = loader.get_template('penyajiandata.html')
    return HttpResponse(template.render())
def perbandingan(request):
    template = loader.get_template('perbandingan.html')
    return HttpResponse(template.render())
def persamaandanpertidaksamaanlinearsatuvariabel(request):
    template = loader.get_template('persamaandanpertidaksamaanlinearsatuvariabel.html')
    return HttpResponse(template.render())
def persamaangarislurus(request):
    template = loader.get_template('persamaangarislurus.html')
    return HttpResponse(template.render())
def persamaankuadrat(request):
    template = loader.get_template('persamaankuadrat.html')
    return HttpResponse(template.render())
def persamaanlinearduavariabel(request):
    template = loader.get_template('persamaanlinearduavariabel.html')
    return HttpResponse(template.render())
def polabilangan(request):
    template = loader.get_template('polabilangan.html')
    return HttpResponse(template.render())
def relasidanfungsi(request):
    template = loader.get_template('relasidanfungsi.html')
    return HttpResponse(template.render())
def segiempatdansegitiga(request):
    template = loader.get_template('segiempatdansegitiga.html')
    return HttpResponse(template.render())
def statistika(request):
    template = loader.get_template('statistika.html')
    return HttpResponse(template.render())
def teoremapythagoras(request):
    template = loader.get_template('teoremapythagoras.html')
    return HttpResponse(template.render())
def transformasi(request):
    template = loader.get_template('transformasi.html')
    return HttpResponse(template.render())