from django import forms
from .models import Ticket

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = {
            "title",
            "description",
            "category",
            "priority",
            
        }
class ChangeTicketStatus(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = {
            "status",
        }