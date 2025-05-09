from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from . import models, forms


class CarListView(ListView):
    model = models.Car
    template_name = 'car_list.html'
    context_object_name = 'cars'
    paginate_by = 12

    def get_queryset(self):
        queryset = super().get_queryset().order_by('model')
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(model__icontains=search)

        return queryset


class CarCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Car
    template_name = 'car_create.html'
    form_class = forms.CarForm
    success_url = reverse_lazy('car_list')
    permission_required = 'cars.add_car'


class CarDetailView(DetailView):
    model = models.Car
    template_name = 'car_detail.html'


class CarUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Car
    template_name = 'car_update.html'
    form_class = forms.CarForm
    success_url = reverse_lazy('car_list')
    permission_required = 'cars.change_car'


class CarDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Car
    template_name = 'car_delete.html'
    success_url = reverse_lazy('car_list')
    permission_required = 'cars.delete_car'
