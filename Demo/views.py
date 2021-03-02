from django.shortcuts import render
from .models import Contact
from django.contrib.auth.models import User
from django.http import Http404

# Create your views here.
def home(request):
    return render(request, 'index.html')

def contact(request):
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('contact_no') and request.POST.get('subject') and request.POST.get('message') :
            post = Contact()
            post.name = request.POST.get('name')
            post.contact_no = request.POST.get('contact_no')
            post.subject = request.POST.get('subject')
            post.message = request.POST.get('message')
            print(post.name)
            #post = post.objects.create_user(name =request.POST['name'], contact_no =request.POST['contact_no'], subject =request.POST['subject'], message = request.POST['message'])
            post.save()

            return render(request, 'index.html')
        else:
            return render(request, 'index.html')

# def Contact(request):
#     if request.method == "POST":
#         user= User.objects.create_user(name =request.POST['name'], contact_no =request.POST['contact_no'], subject =request.POST['subject'], message = request.POST['message'])
#         user.save()
#         return render(request,"index.html",{})
#     else:
#         return render(request, "index.html")