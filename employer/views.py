from django.shortcuts import render
from .models import Employer
from .forms import EmployerForm
from django.shortcuts import render, redirect


def liste_employers(request):
    employers = Employer.objects.all()
    return render(request, 'employer/liste.html', {'employers': employers})

def ajouter_employer(request):
    form = EmployerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('liste_employers')
    return render(request, 'employer/formulaire.html', {'form': form})