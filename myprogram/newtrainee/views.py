from django.shortcuts import render
from newtrainee.forms import *
from django.views.generic.edit import UpdateView
from subject.models import subject
# Create your views here.
def modform(req):
    context={}
    form = insertnewtraineemod()
    if req.method == 'GET':
        context['form'] = form
        return render(req,'newtrainee/mod.html',context)
    else:
        form = insertnewtraineemod(req.POST)
        if form.is_valid():
            form.save()
        return render(req,'myuser/home.html')


def formview(req):
    context={}
    form = insertnewtrainee()
    if req.method == 'GET':
        context['form'] = form
        return render(req,'newtrainee/mod.html',context)
    else:
        form = insertnewtrainee(req.POST)
        if form.is_valid():
            print(' ***********')
            newtrainee.objects.create(name=form['name'].value(),nationalnum=form['nationnum'].value(),sub=subject.objects.get(id=form['sub'].value()))

        return render(req,'myuser/home.html')


