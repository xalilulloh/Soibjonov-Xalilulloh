from django.shortcuts import render,redirect
from .urls import *
from .models import *
from django.contrib import messages
from django.views.generic import DetailView
# Create your views here.
def Home(request):
    info = Info.objects.first()
    photo = Photo.objects.first()
    context = {
        'info':info,
        'photo':photo
    }
    return render(request,'index.html',context)


def Resume(request):
    info = Info.objects.first()
    
    context = {
        'info':info,
        'about':About.objects.first(),
        'service':Service.objects.all(),
        'educat':Education.objects.all(),
        'skill':Skill.objects.all(),
        'programming':Programming.objects.all(),
        'lang':Language.objects.all()
       
    }

    return render(request,'about.html',context)

def Contact(request):
    return render(request,'contact.html')

def Send(request):
    r=request.POST
    if request.method=='POST':
        fname=r['fname']
        lname = r['lname']
        email = r['email']
        text = r['text']
        Aloqa.objects.create(fname=fname,lname=lname,email=email,text=text)
        info = '<strong>{}</strong>. Xabaringiz Yuborildi! , Tez orada aloqaga chiqamiz'.format(lname)
        messages.success(request,info)
        
    return redirect('/contact/')

    
def Blog(request):


    context={
        'blog':BlogTitle.objects.all()
    }
    return render(request,'blog.html',context)

def BlogSingle(request,id):
    article = BlogTitle.objects.get(id=id)

class BlogDetail(DetailView):

    model = BlogTitle
    template_name = 'blog-single.html'
    context_object_name = 'blog'

def Commenting(request):
    r=request,'POST'
    if request.mathod == 'POST':
        fname=r['fname']
        lname = r['lname']
        email = r['email']
        text = r['text']
        Aloqa.objects.create(fname=fname,lname=lname,email=email,text=text)
        info = '<strong>{}</strong>. Xabaringiz Yuborildi! , Tez orada aloqaga chiqamiz'.format(lname)
        messages.success(request,info)

    return redirect('/views/') 