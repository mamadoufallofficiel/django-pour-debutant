from django.shortcuts import render
from .models import Employer

def liste_employers(request):
    employers = Employer.objects.all()
    return render(request, 'employer/liste.html', {'employers': employers})
