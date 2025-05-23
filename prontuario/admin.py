from django import forms
from django.contrib import admin
from django.forms import TextInput
from django.db import models
from .models import Especialidade, Medico, Paciente, Endereco


@admin.register(Especialidade)
class EspecialidadeAdmin(admin.ModelAdmin):
    list_display = ['nome']
    search_fields = ['nome']
    ordering = ['nome']


@admin.register(Medico)
class MedicoAdmin(admin.ModelAdmin):
    list_display = ['nome']
    ordering = ['nome']
    filter_horizontal = ['especialidades']


@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    class Media:
        js = ('js/cep_autocomplete.js',)

    campos_cep_readonly_inicial = ['rua', 'bairro', 'cidade', 'estado']

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        if db_field.name in self.campos_cep_readonly_inicial:
            kwargs['widget'] = forms.TextInput(attrs={
                'readonly': 'readonly'
            })
        return super().formfield_for_dbfield(db_field, request, **kwargs)

    list_display = ['rua', 'numero', 'bairro', 'cidade', 'estado', 'cep']
    ordering = ['rua']
    fieldsets = [
        ('Paciente', {'fields': ['paciente']}),
        ('Endereço', {'fields': ['cep', 'rua', 'numero', 'complemento', 'bairro', 'cidade', 'estado']}),
    ]



class EnderecoInline(admin.StackedInline):
    model = Endereco
    extra = 1
    fieldsets = [
        (None, {'fields': ['cep', 'rua', 'numero', 'complemento', 'bairro', 'cidade', 'estado']}),
    ]

    class Media:
        js = ('js/cep_autocomplete.js',)

    campos_cep_readonly_inicial = ['rua', 'bairro', 'cidade', 'estado']

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        if db_field.name in self.campos_cep_readonly_inicial:
            kwargs['widget'] = forms.TextInput(attrs={
                'readonly': 'readonly'
            })
        return super().formfield_for_dbfield(db_field, request, **kwargs)


@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ['nome', 'data_nascimento']
    ordering = ['nome']
    inlines = [EnderecoInline]


