from django.shortcuts import render

# Create your views here.

def contact(request):
    context = {
        'nama': 'Kontak Saya',
    }
    return render(request, 'contact/contact.html', context)