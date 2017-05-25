from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from .models import Ticket
from .forms import TicketForm

# Create your views here.

def index(request):
    tickets = Ticket.objects.all()
    return render(request, 'ticketing/index.html', {'tickets': tickets})

def ticket_create(request):
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit = False)
            ticket.user = request.user
            ticket.save()
            return redirect(ticket_detail, pk = ticket.pk )
    else:
        form = TicketForm()
    context = {
        'form': form
        }
    return render(request, 'ticketing/ticket_create.html', context )

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
        'tickets':query
        }
    return render(request, 'ticketing/tickets.html', context)

def ticket_remove(request):
    pass

def ticket_reslove(request):
    pass
