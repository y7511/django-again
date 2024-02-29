from django.shortcuts import render , redirect
from .models import*
from .models import contact_admin
from .forms import ContactForm








# Create your views here.
def index(request):

    info = CompanyInformation.objects.all().first()
    product = Product.objects.all()
    
    

    data ={
    'info':info,
    'product':product
 } 
    return render(request, 'index.html',data)



def about(request):
    info = abouttable.objects.first()
    

    data ={
    'info':info,
    } 

    
    return render(request, 'about.html',data)

from .models import contact_admin

def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('mainpag')  # Redirect to mainpag after form submission
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def mainpag(request):
    # Fetch data for the main page, for example, contact_admin objects
    contacts = contact_admin.objects.all()

    # Pass the fetched data to the template
    data = {
        'contacts': contacts,
    }

    return render(request, 'mainpag.html', data)



# creating new product


