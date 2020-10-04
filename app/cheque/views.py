from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated

from . import serializers
from core.models import Cheque, Assinante, Banco, Emitente, Telefone

# from core.tasks import update_dias, update_status_cheque, bloqueio_conta


class ChequeViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    permission_classes = (IsAuthenticated,)
    queryset = Cheque.objects.all()
    serializer_class = serializers.ChequeSerializer
    lookup_field = ('id')
    
    
class AssinanteViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.ListModelMixin):
    permission_classes = (IsAuthenticated,)
    queryset = Assinante.objects.all()
    serializer_class = serializers.AssinanteSerializer
    lookup_field = ('id')
    
    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return serializers.AssinanteDetailSerializer
        
        return self.serializer_class
    
    
    def perform_create(self, serializer):
        serializer.save()
        
    
    
    
class BancoViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.ListModelMixin):
    permission_classes = (IsAuthenticated,)
    queryset = Banco.objects.all()
    serializer_class = serializers.BancoSerializer
    lookup_field = ('id')
    
    
class EmitenteViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.ListModelMixin):
    permission_classes = (IsAuthenticated,)
    queryset = Emitente.objects.all()
    serializer_class = serializers.EmitenteSerializer
    lookup_field = ('id')
    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return EmitenteDetailSerializer
        return self.serializer_class
    
    def perform_create(self, serializer):
        serializer.save()
    

    
class TelefoneViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.ListModelMixin):
    permission_classes = (IsAuthenticated,)
    queryset = Telefone.objects.all()
    serializer_class = serializers.TelefoneSerializer
    lookup_field = ('id')
    
# def celery(request):
#     update_dias.delay()
#     update_status_cheque.delay()
#     bloqueio_conta.delay()
#     return HttpResponse('Enviado com sucesso')

# class CeleryViewSet(viewsets.GenericViewSet):
#     update_dias.delay()
#     update_status_cheque.delay()
#     bloqueio_conta.delay()
    