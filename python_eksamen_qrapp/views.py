from django.shortcuts import render

# Create your views here.
def index(request):

    context = {
        
    }

    return render(request, 'python_eksamen_qrapp/index.html', context)