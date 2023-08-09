from django.shortcuts import render
from . forms import contactForm
def home(request):
    return render(request,"./myapp/index.html")
def about(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        return render(request,'./myapp/about.html',{'name':name,'email':email})
    else:
        return render(request,'./myapp/about.html',{'name':'N/A', 'email':'N/A'})
    
def submit_form(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    return render(request,"./myapp/form.html")

def DjangoForm(request):
    if request.method == 'POST':
        form = contactForm(request.POST,request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']
            with open('./myapp/upload/' + file.name, 'wb+') as destination:
                for chunk in file.chunks():
                    # high reso to low reso
                    destination.write(chunk)
            print(form.cleaned_data)
            return render(request,'./myapp/django_form.html',{'form':form})
    else:
        form = contactForm()
    return render(request,'./myapp/django_form.html',{'form':form})
