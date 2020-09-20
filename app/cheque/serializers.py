from rest_framework import serializers

from core.models import Emitente, Assinante, Cheque, Banco, Telefone, MotivoDevolucao


class BancoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Banco
        fields = ('id', 'nome')
        read_only_fields = ('id',)


class TelefoneSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Telefone
        fields = ('id', 'numero')
        read_only_fields = ('id',)
        
class MotivoDevolucaoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MotivoDevolucao
        fields = ('id', 'descricao')
        read_only_fields = ('id',)

class AssinanteSerializer(serializers.ModelSerializer):
    
    telefones = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Telefone.objects.all()
    )
    
    class Meta:
        model = Assinante
        fields = ('nome', 'numero_conta', 'telefones', 'email', 'endereco', 'bloqueio_utr')
        read_only_fields = ('id',)
        
class AssinanteDetailSerializer(AssinanteSerializer):
    telefones = TelefoneSerializer(many=True, read_only=True)
        
class EmitenteSerializer(serializers.ModelSerializer):
    
    telefones = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Telefone.objects.all()
    )
    assinantes = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Assinante.objects.all()
    )
    
    class Meta:
        model = Emitente
        fields = ('nome', 'numero_conta', 'telefones', 'email', 'endereco', 'tipo', 'assinantes', 'bloqueio_utr')
        read_only_fields = ('id',)
        
class EmitenteDetailSerializer(EmitenteSerializer):
    telefones = TelefoneSerializer(many=True, read_only=True)
        
class ChequeSerializer(serializers.ModelSerializer):
    
    motivo_devolucao = serializers.PrimaryKeyRelatedField(
        many=False,
        queryset=MotivoDevolucao.objects.all()
    )
    emitente = serializers.PrimaryKeyRelatedField(
        many=False,
        queryset=Emitente.objects.all()
    )
    
    banco = serializers.PrimaryKeyRelatedField(
        many=False,
        queryset=Banco.objects.all()
    )
    
    class Meta:
        model = Cheque
        fields = ('id', 'motivo_devolucao', 'numero_cheque', 'emitente', 'numero_conta', 'valor_cheque', 'data_devolucao', 'codigo_balcao', 'banco', 'data_criacao', 'dias')
        read_only_fields = ('id',)
        
  