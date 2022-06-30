from django.shortcuts import render
from subject.models import *
from django.views import View
from django.views.generic import *
from django.http import HttpResponseRedirect
# Create your views here.
class deletesub(View):
    def get(self,req):
        context={}
        context['subs']=subject.objects.all()
        return render(req,'subject/subshow.html',context)

    def post(self,req):
        subject.objects.get(id=req.POST['determine']).delete()
        context = {}
        context['subs'] = subject.objects.all()
        return render(req, 'subject/subshow.html',context)

class subupdate(UpdateView):
    model = subject
    fields ='__all__'

def subupdateview(req,id):
    if req.method == 'GET':
        u = subject.objects.get(id=id)
        context={}
        context['sub']=u
        return render(req,'subject/upsub.html',context)
    else:
        subject.objects.filter(id=id).update(name=req.POST['name'],hours=req.POST['hours'])
        return HttpResponseRedirect('/')

def subdeleteview(req,id):
    subject.objects.filter(id=id).delete()
    return HttpResponseRedirect('/')