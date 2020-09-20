from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('cheques-devolvidos', views.ChequeViewSet)
router.register('assinantes', views.AssinanteViewSet)
router.register('bancos', views.BancoViewSet)
router.register('emitentes', views.EmitenteViewSet)
router.register('telefones', views.TelefoneViewSet)

app_name = 'cheque'

urlpatterns = [
    path('', include(router.urls)),
    

]