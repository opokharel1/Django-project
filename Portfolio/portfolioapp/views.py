
from django.shortcuts import render
from portfolioapp.models import Education, Experience

# Create your views here.

def homepage_view(request):
    educations =Education.objects.all()
    experiences= Experience.objects.all()  #--> yo ORM le garda code yesto sajilo bhako, natra, SQL lekhna parthyo
    context= {
        "educations": educations, 
        "experiences": experiences}
    return render(request, "homepage.html", context=context)

def about_view(request):
    return render(request, "about.html")

def contact_view(request):
    return render(request, "contact.html")



