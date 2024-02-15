"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpRequest
from .forms import YourModelForm


def try_josie(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Try Josie ML',
            'year':datetime.now().year,
        }
    )

def about_creator(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'About Creator',
            'year':datetime.now().year,
        }
    )

def about_josie(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About Josie ML',
            'year':datetime.now().year,
        }
    )

def upload_image(request):
    if request.method == 'POST':
        form = YourModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success_url')
    else:
        form = YourModelForm()
    return render(request, 'upload_image.html', {'form': form})
