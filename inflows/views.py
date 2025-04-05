from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, CreateView, DetailView
from django.urls import reverse_lazy

from rest_framework import generics

from inflows.serializers import InflowSerializer
from inflows.models import Inflow
from inflows.forms import InflowForm

class InflowListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Inflow
    template_name = 'inflow_list.html'
    context_object_name = 'inflows'
    paginate_by = 10 #Para realizar paginação da ListView
    permission_required = 'inflows.view_inflow'

    def get_queryset(self): #Função para criar uma campo de pesquisa
        queryset = super().get_queryset()
        product = self.request.GET.get('product')

        if product:
            queryset = queryset.filter(product__title__icontains=product)

        return queryset

class InflowCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Inflow
    template_name = 'inflow_create.html'
    form_class = InflowForm
    success_url = reverse_lazy('inflow_list')
    permission_required = 'inflows.add_inflow'

class InflowDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Inflow
    template_name = 'inflow_detail.html'
    permission_required = 'inflows.view_inflow'

class InflowCreateListAPIView(generics.ListCreateAPIView):
    queryset = Inflow.objects.all()
    serializer_class = InflowSerializer

class InflowRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Inflow.objects.all()
    serializer_class = InflowSerializer
