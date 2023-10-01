from django.shortcuts import render, redirect
from .models import Adotar, TerAnimais

# Create your views here.
def home(request):
  adocao = Adotar.objects.all()
  animal = TerAnimais.objects.all()
  return render(request, "home.html", context={
    "adocao": adocao,
  "animal":animal
  })

def create_adocao(request):
  if request.method == "POST":
    # criar novo filme usando os valores do meu formulário
    Adotar.objects.create(
      titulo = request.POST["titulo"],
      motivo = request.POST["motivo"],
      nivelAgitado = request.POST["nivelAgitado"],
      expecVida = request.POST["expecVida"]
    )
    return redirect("home")
  return render(request, "forms.html", context={
  "action": "Adicionar",
  "nivelAgitado":Adotar.nivelAgitado.field.choices})


def update_adocao(request,id):
  adocao = Adotar.objects.get(id = id)
  if request.method == "POST":
    adocao.titulo = request.POST["titulo"]
    adocao.motivo = request.POST["motivo"]
    adocao.nivelAgitado = request.POST["nivelAgitado"]
    adocao.expecVida = request.POST["expecVida"]
    adocao.save()
    
    return redirect("home")
  return render(request, "forms.html", context={
    "action": "Atualizar",
    "adocao": adocao,
  "nivelAgitado":Adotar.nivelAgitado.field.choices})

def delete_adocao(request,id):
  adocao = Adotar.objects.get(id = id)
  if request.method == "POST":
    if "confirm" in request.POST:
      adocao.delete()

    return redirect("home")
  return render(request, "are_you_sure.html", context={"adocao": adocao})

def create_animal(request):
  if request.method == "POST":
    # criar novo filme usando os valores do meu formulário
    TerAnimais.objects.create(
      titulo = request.POST["titulo"],
      resumo = request.POST["resumo"],
      genero = request.POST["genero"],
      dataLancamento = request.POST["dataLancamento"]
    )
    return redirect("home")
  return render(request, "forms2.html", context={"action": "Adicionar" })


def update_animal(request,id):
  animal = TerAnimais.objects.get(id = id)
  if request.method == "POST":
    animal.titulo = request.POST["titulo"]
    animal.resumo = request.POST["resumo"]
    animal.genero = request.POST["genero"]
    animal.dataLancamento = request.POST["dataLancamento"]
    animal.save()

    return redirect("home")
  return render(request, "forms2.html", context={"action": "Atualizar","animal": animal })


def delete_animal(request,id):
  animal = TerAnimais.objects.get(id = id)
  if request.method == "POST":
    if "confirm" in request.POST:
      animal.delete()

    return redirect("home")
  return render(request, "are_you_sure2.html", context={"animal": animal})