# views.py

from django.shortcuts import render
from .forms import NameForm

from .models import SaveFile

def index(request):
    name_form = NameForm(request.POST or None, initial={'name': 'whatever'})

    if request.method == 'POST':
        if name_form.is_valid():
            # do something
            SaveFile().savenewfile(name_form.cleaned_data['name'])
            pass

    return render(request, 'polls/index.html', {'name_form': name_form})

