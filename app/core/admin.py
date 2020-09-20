from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _

from core.models import Banco, Emitente, Assinante, Documento, Telefone, Cheque, Regularizacao, MotivoDevolucao, User, Profile



class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'nome']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('nome',)}),
        (
            _('Permissions'),
            {'fields': ('is_active', 'is_staff', 'is_superuser')}
        ),
        (_('Important dates'), {'fields': ('last_login',)})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }),
    )

admin.site.register(User, UserAdmin)
admin.site.register(Profile)
admin.site.register(Banco)
admin.site.register(Emitente)
admin.site.register(Assinante)
admin.site.register(Documento)
admin.site.register(Telefone)
admin.site.register(Cheque)
admin.site.register(Regularizacao)
admin.site.register(MotivoDevolucao)
