from django.contrib.messages.storage import session
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *

# Create your views here.

def index(request):
    movies = Movie.objects.all()
    request.session['ip'] = request.META.get("REMOTE_ADDR")

    visitor_count = Visitors.objects.filter(ip = request.session['ip']).count()
    count = visitor_count
    if visitor_count >= 1:
        count = ""

    return render(request,"index.html",{"movies" : movies,"count" : count})

def viewresult(request):
    review = Review.objects.all()
    return render(request,"result.html",{"review":review})

def rating(request):
    choice = request.GET['movie']
    review = Review.objects.get(id=int(choice))
    review.vote += 1
    review.save()

    visitor = Visitors(ip = request.session['ip'])
    visitor.save()
    return redirect("/result")