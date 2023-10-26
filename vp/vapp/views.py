from django.shortcuts import render, HttpResponse
from vapp.models import Member
# Create your views here.


def home(request):
    return render(request, ('home.html'))


def about(request):
    return render(request, ('about.html'))


def contact(request):
    return render(request, ('contact.html'))


def service(request):
    return render(request, ('service.html'))


def send(request):
    if request.method == 'POST':
        # id = request.POST['id']
        fname = request.POST['fname']
        lname = request.POST['lname']
        country = request.POST['country']
        subject = request.POST['subject']
        Member(fname=fname, lname=lname,country=country, subject=subject).save()
        msg = "Data Stored Successfully"
        return render(request, "contact.html", {'msg': msg})
    else:
        return HttpResponse("404 Not Found")
