from django.shortcuts import render
from .models import UserProfile #jo hamne model me db banaya hai usko import karna hai yaha use krne ke liye 
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')

def submit_form(request): #isse ham form ka data le payenge
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if UserProfile.objects.filter(username=username).exists(): #check if username already exists
            return HttpResponse("Username already exists!")
        user_profile = UserProfile(username=username, email=email, password=password)
        user_profile.save()
        return HttpResponse("Form submitted successfully!")
    return render(request, 'index.html') #agar insert nahi hua to form ko dobara render karega
def show_form(request):
    data = UserProfile.objects.all() #ye sabhi data ko le aayega jo db me hai
    return render(request, 'show_form.html', {'data': data}) #yaha se form ko show karega
def update_details(request, id):
    data = UserProfile.objects.get(id=id)
    return render(request, 'update_form.html', {'data': data}) #yaha se update form ko show karega
def update_submit(request, id):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_profile = UserProfile.objects.get(id=id) 
        user_profile.username = username
        user_profile.email = email
        user_profile.password = password
        user_profile.save()
        data = UserProfile.objects.all() #update hone ke baad sabhi data ko le aayega
        return render(request, 'show_form.html', {'data': data}) #yaha se form ko show karega
    return render(request, 'update_form.html', {'data': UserProfile.objects.get(id=id)})

def delete_form(request, id):
    data = UserProfile.objects.get(id=id)
    data.delete() #ye record ko delete karega
    data = UserProfile.objects.all() #delete hone ke baad sabhi data ko le aayega
    return render(request, 'show_form.html', {'data': data}) #yaha se form ko show karega

def home(request):
    return render(request, 'home.html')
def sample(request):
    return render(request, 'sample.html')  # Render the sample.html template