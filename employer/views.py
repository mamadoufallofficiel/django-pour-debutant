from django.shortcuts import render
from .models import Employer
from .forms import EmployerForm
from django.shortcuts import render, redirect, get_object_or_404


def liste_employers(request):
    employers = Employer.objects.all()
    return render(request, 'employer/liste.html', {'employers': employers})

def ajouter_employer(request):
    form = EmployerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('liste_employers')
    return render(request, 'employer/formulaire.html', {'form': form})

def modifier_employer(request, id):
    employer = get_object_or_404(Employer, id=id)
    form = EmployerForm(request.POST or None, instance=employer)
    if form.is_valid():
        form.save()
        return redirect('liste_employers')
    return render(request, 'employer/formulaire.html', {'form': form})

def supprimer_employer(request, id):
    employer = get_object_or_404(Employer, id=id)
    if request.method == 'POST':
        employer.delete()
        return redirect('liste_employers')
    return render(request, 'employer/confirmer_suppression.html', {'employer': employer})