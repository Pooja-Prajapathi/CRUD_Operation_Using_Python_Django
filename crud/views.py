from django.shortcuts import render, redirect
from .models import Member

# Create your views here.

def index(request):
    members = Member.objects.all()
    context = {'members': members}
    return render(request, 'crud/index.html', context)

def create(request):
    member = Member(username=request.POST['username'], password=request.POST['password'],userid=request.POST['userid'],
                    email=request.POST['email'])
    member.save()
    return redirect('/')

def edit(request, id):
    members = Member.objects.get(id=id)
    context = {'members': members}
    return render(request, 'crud/edit.html', context)

def update(request, id):
    member = Member.objects.get(id=id)
    member.username= request.POST['username']
    member.password = request.POST['password']
    member.userid = request.POST['userid']
    member.email = request.POST['email']
    member.save()
    return redirect('/crud/')

def delete(request, id):
    member = Member.objects.get(id=id)
    member.delete()
    return redirect('/crud/')