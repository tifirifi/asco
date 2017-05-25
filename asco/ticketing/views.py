from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import Ticket

# Create your views here.

def index(request):
    tickets = Ticket.objects.all()
    return render(request, 'ticketing/index.html', {'tickets': tickets})

def ticket_create(request):
    pass

def ticket_update(request):
    pass

def ticket_detail(request, pk=None):
    instance = get_object_or_404(Ticket, pk=pk)
    context = {
        "detail": instance
    }
    return render(request, 'ticketing/ticket_detail.html', context)

def ticket_list(request):
    query = Ticket.objects.all()
    context = {
        'ticketss':query
        }
    return render(request, 'ticketing/tickets.html', context)

def ticket_remove(request):
    pass
