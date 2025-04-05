from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, CreateView, DetailView
from django.urls import reverse_lazy
from app import metrics

from rest_framework import generics

from outflows.serializers import OutflowSerializer
from outflows.models import Outflow
from outflows.forms import OutflowForm

class OutflowListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Outflow
    template_name = 'outflow_list.html'
    context_object_name = 'outflows'
    paginate_by = 10 #Para realizar paginação da ListView
    permission_required = 'outflows.view_outflow'

    def get_queryset(self): #Função para criar uma campo de pesquisa
        queryset = super().get_queryset()
        product = self.request.GET.get('product')

        if product:
            queryset = queryset.filter(product__title__icontains=product)

        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sales_metrics'] = metrics.get_sales_metrics()

        return context

class OutflowCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Outflow
    template_name = 'outflow_create.html'
    form_class = OutflowForm
    success_url = reverse_lazy('outflow_list')
    permission_required = 'outflows.add_outflow'

class OutflowDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Outflow
    template_name = 'outflow_detail.html'
    permission_required = 'outflows.view_outflow'

class OutflowCreateListAPIView(generics.ListCreateAPIView):
    queryset = Outflow.objects.all()
    serializer_class = OutflowSerializer

class OutflowRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Outflow.objects.all()
    serializer_class = OutflowSerializer
