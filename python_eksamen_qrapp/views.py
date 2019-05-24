from django.shortcuts import render

from .forms import UrlForm

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = UrlForm(request.POST)

    else:
        form = UrlForm()

    return render(request, 'python_eksamen_qrapp/index.html', {'form': form})