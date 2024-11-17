from django.shortcuts import get_object_or_404, render, redirect
from django.views import View
from django.views.generic import ListView

from users.models import Purchase, Customer
from .models import Scooter


class ScooterListView(ListView):
    model = Scooter
    template_name = 'scooters\scooter_list.html'


class ScooterDetailView(View):
    def get(self, request, **kwargs):
        template = 'scooters\scooter_detail.html'

        scooter = get_object_or_404(Scooter, id=kwargs.get('id'))
        context = {
            'scooter': scooter,
        }
        return render(request, template, context)

    def post(self, request, **kwargs):
        time = int(request.POST.get('time'))
        scooter = get_object_or_404(Scooter, id=kwargs.get('id'))
        customer = get_object_or_404(Customer, id=request.user.id)

        purchase = Purchase.objects.create(
            user=customer,
            scooter=scooter,
            price=time * scooter.price,
            time=time
        )
        purchase.save()
        return redirect('catatog:scooters')
