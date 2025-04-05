#Habilidar no arquivo app.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from inflows.models import Inflow

@receiver(post_save, sender=Inflow)
def update_product_quantity(sender, instance, created, **kwargs):
    if created: #Criação de registro
        if instance.quantity > 0:
            product = instance.product #recebendo a instacia produto
            product.quantity += instance.quantity #armazenando quantidade e adicionando ao valor existente
            product.save()#Novo dado salvo

