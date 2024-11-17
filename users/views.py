from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView

from core.views import is_ajax
from users.forms import CustomerCreateForm, CustomerImageForm, CustomerBalanceAddForm
from users.models import Customer, Purchase


class SignupView(FormView):
    form_class = CustomerCreateForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        template = 'users/profile.html'

        customer = get_object_or_404(Customer, user=request.user.id)
        image_form = CustomerImageForm()
        purchases = Purchase.objects.filter(user=customer)

        context = {
            'form_image': image_form,
            'customer': customer,
            'purchases': purchases
        }

        return render(request, template, context)

    def post(self, request):
        if not is_ajax(request):
            customer = get_object_or_404(Customer, user=request.user)
            form_image = CustomerImageForm(request.POST, request.FILES, instance=customer)

            if form_image.is_valid():
                form_image.save()

            return redirect("users:profile")
        else:
            purchase = get_object_or_404(Purchase, id=request.POST.get('id'))
            if purchase.user.id == request.user.id:
                purchase.delete()
            return JsonResponse({})


class BalanceAddView(LoginRequiredMixin, FormView):
    form_class = CustomerBalanceAddForm
    success_url = reverse_lazy('users:profile')
    template_name = 'users/balance_add.html'

    def form_valid(self, form):
        form.save(self.request.user)
        return super().form_valid(form)
