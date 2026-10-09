from django.shortcuts import render, redirect

from .forms import PetForm
from .models import Pet


def pet_list(request):
    pets = Pet.objects.all().order_by('-date_registered', '-id')
    return render(request, 'InVApp/pet_list.html', {'pets': pets})


def add_pet(request):
    form = PetForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('pet_list')
    return render(request, 'InVApp/pet_form.html', {'form': form})