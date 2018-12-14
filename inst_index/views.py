from django.shortcuts import render


def home(request):
    d = {'content': 'Home page is under construction...'}
    return render(request, 'inst_index/template.html', context=d)

def view_index(request):
    d = {'content': 'Instrument Index is under construction...'}
    return render(request, 'inst_index/template.html', context=d)
