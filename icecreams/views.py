from django.shortcuts import render
from . forms import IceCreamsForm, NoOfIceCreamsForm


def home(request):
    return render(request, 'icecreams/home.html')


def order(request):
    multiple_form = NoOfIceCreamsForm()
    if request.method == 'POST':
        filled_form = IceCreamsForm(request.POST)  # request.FILES
        if filled_form.is_valid():
            note = "Thanks for ordering ice cream, your %s and %s ice cream is on it's way" %\
                   (filled_form.cleaned_data['flavours'],
                    filled_form.cleaned_data['size'], )
            new_form = IceCreamsForm()
            return render(request, 'icecreams/order.html', {'icecreams_form': new_form, 'note': note, 'multiple_form': multiple_form})

    else:
        form = IceCreamsForm()
        return render(request, 'icecreams/order.html', {'icecreams_form': form, 'multiple_form': multiple_form})



