from django.shortcuts import render,redirect
from django.http import HttpResponse
visits = 0
Language="English"
Template="home"
Visitors = 0

def index(request):
    global Language , Template , Visitors , visits
    Visitors+=1
    visits = str('0'*(6- len(str(Visitors)))+str(Visitors))
    Template="home"
    return render(request,f'{Language}/index.html',{'Visitors':visits})

def switch(request):
    print("Switch function called success")
    global Language , visits
    if request.method == "POST":
        Language = request.POST.get('button')
    else:
        return HttpResponse("Something Went Wrong !",{'Visitors':visits})

    return redirect(f'{Template}')

def trustees(request):
    global Template , visits
    Template="trustees"
    print("Showed the trustees.\nThe language is :",Language)
    return render(request,f'{Language}/boardmembers.html',{'Visitors':visits})

def darshan(request):
    global Template , visits
    Template = 'darshan'
    return render(request,f'{Language}/livedarshan.html',{'Visitors':visits})

def history(request):
    global Template , visits
    Template = 'history'
    return render(request,f'{Language}/templehistory.html',{'Visitors':visits})

def dailyseva(request):
    global Template , visits
    Template = 'dailyseva'
    return render(request,f'{Language}/dailyseva.html',{'Visitors':visits})

def mahaabhishekh(request):
    global Template , visits
    Template = 'mahaabhishekh'
    return render(request,f'{Language}/mahaabhishek.html',{'Visitors':visits})

def imagegallery(request):
    global Template , visits
    Template = 'imagegallery'
    return render(request,f'{Language}/imagegallery.html',{'Visitors':visits})

def videogallery(request):
    global Template , visits
    Template = 'videogallery'
    return render(request,f'{Language}/videogallery.html',{'Visitors':visits})

def othergallery(request):
    global Template , visits
    Template = 'othergallery'
    return render(request,f'{Language}/othergallery.html',{'Visitors':visits})

def poojadetails(request):
    global Template , visits
    Template = 'poojadetails'
    return render(request,f'{Language}/pooja.html',{'Visitors':visits})

def donation(request):
    global Template , visits
    Template = 'donation'
    return render(request,f'{Language}/donation.html',{'Visitors':visits})

def contact(request):
    global Template , visits
    Template = 'contact'
    return render(request,f'{Language}/contact.html',{'Visitors':visits})

def Festivals(request):
    global Template , visits
    Template = 'Festivals'
    return render(request,f'{Language}/Festivals.html',{'Visitors':visits})

def about(request):
    global Template , visits
    Template = 'about'
    return render(request,f'{Language}/about.html',{'Visitors':visits})

def architecture(request):
    global Template , visits
    Template = 'architecture'
    return render(request,f'{Language}/architecture.html',{'Visitors':visits})
