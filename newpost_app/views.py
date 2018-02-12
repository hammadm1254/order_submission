## for redirection and rendering
from django.shortcuts import render #, get_object_or_404, redirect

## for user authentication
#from django.contrib.auth import login, logout, authenticate
#from django.contrib.auth.decorators import login_required

# for getting current time
#from django.utils import timezone

## my own functions in modules directory
from modules import mappingLib

## The forms and models
#from django.contrib.auth.forms import UserCreationForm
from .forms import OrderForm

## for url parsing
from urllib.parse import urlencode
from urllib.parse import parse_qs

## Django Decorators
#from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    if request.method == 'POST':
        submitted_order_form = OrderForm(request.POST)
        if submitted_order_form.is_valid():
            return order_confirmation(request, submitted_order_form)
        else:
            pass
    else:
        url = request.get_full_path()
        url = parse_qs(url)
        try:
            origin = url['origin'][0]
        except KeyError:
            origin = None
        try:
            destination = url['destination'][0]
        except KeyError:
            destination = None
        try:
            instructions = url['specialInstructions'][0]
        except KeyError:
            instructions = None
        if origin and destination and instructions:
            order_form = OrderForm({'origin': origin, 'destination': destination, 'special_instructions': instructions})
        else:
            order_form = OrderForm()
    return render(request, 'newpost_app/home.html', {'title': " - Home", 'form': order_form})

def order_confirmation(request, form_object):
    origin_string = form_object.cleaned_data.get('origin')
    destination_string = form_object.cleaned_data.get('destination')
    instruction_string = form_object.cleaned_data.get('special_instructions')
    try:
        route_data = mappingLib.cost_calculator(origin_string, destination_string)
    except Exception as e:
        return render(request, 'newpost_app/error_page.html', {'error_message': e, 'title': ' - error'})
    form_object.save(commit=False)
    url = urlencode({'query': 'none', 'origin': route_data['origin'], 'destination': route_data['dest'], 'specialInstructions': instruction_string}, doseq=True)
    return render(request, 'newpost_app/order_confirmation.html',
                  {'title': " - Order Confirmation", 'origin': route_data['origin'], 'destination': route_data['dest'],
                   'special_instructions': instruction_string, 'cost': route_data['cost'], 'url': url})
