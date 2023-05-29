from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Fisioterapeuta, Agenda, Especialidade


class TestMixinIsAdmin(UserPassesTestMixin):
    def test_func(self):
        is_admin_or_is_staff = self.request.user.is_superuser or \
            self.request.user.is_staff
        return bool(is_admin_or_is_staff)

    def handle_no_permission(self):
        messages.error(
            self.request, "Você não tem permissões!"
        )
        return redirect("accounts:index")

class FisioterapeutaCreateView(LoginRequiredMixin, TestMixinIsAdmin, CreateView):

    model = Fisioterapeuta
    login_url = 'accounts:login'
    template_name = 'fisioterapeutas/cadastro.html'
    fields = ['nome', 'crefito', 'email', 'telefone', 'especialidade']
    success_url = reverse_lazy('fisioterapeutas:fisioterapeutas_lista')
    
class FisioterapeutaListView(LoginRequiredMixin, TestMixinIsAdmin, ListView):
    
    login_url = 'accounts:login'
    template_name = 'fisioterapeutas/fisioterapeutas_list.html'

    def get_queryset(self):
        return Fisioterapeuta.objects.all().order_by('-pk')
    
class EspecialidadeCreateView(LoginRequiredMixin, TestMixinIsAdmin, CreateView):

    model = Especialidade
    login_url = 'accounts:login'
    template_name = 'fisioterapeutas/cadastro.html'
    fields = ['nome',]
    success_url = reverse_lazy('fisioterapeutas:especialidade_lista')
    
class EspecialidadeListView(LoginRequiredMixin, TestMixinIsAdmin, ListView):
    
    login_url = 'accounts:login'
    template_name = 'fisioterapeutas/especialidade_list.html'

    def get_queryset(self):
        return Especialidade.objects.all().order_by('-pk')


class AgendaCreateView(LoginRequiredMixin, TestMixinIsAdmin, CreateView):

    model = Agenda
    login_url = 'accounts:login'
    template_name = 'fisioterapeutas/agenda_cadastro.html'
    fields = ['fisioterapeuta', 'dia', 'horario']
    success_url = reverse_lazy('fisioterapeutas:agenda_lista')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class AgendaUpdateView(LoginRequiredMixin, TestMixinIsAdmin, UpdateView):

    model = Agenda
    login_url = 'accounts:login'
    template_name = 'fisioterapeutas/agenda_cadastro.html'
    fields = ['fisioterapeuta', 'dia', 'horario']
    success_url = reverse_lazy('fisioterapeutas:agenda_lista')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class AgendaDeleteView(LoginRequiredMixin, TestMixinIsAdmin, DeleteView):
    model = Agenda
    success_url = reverse_lazy('fisioterapeutas:agenda_lista')
    template_name = 'form_delete.html'

    def get_success_url(self):
        messages.success(self.request, "Consulta excluída com sucesso!")
        return reverse_lazy('fisioterapeutas:agenda_lista')


class AgendaListView(LoginRequiredMixin, TestMixinIsAdmin, ListView):
    
    login_url = 'accounts:login'
    template_name = 'fisioterapeutas/agenda_list.html'

    def get_queryset(self):
        return Agenda.objects.filter().order_by('-pk')
    
fisioterapeuta_cadastro = FisioterapeutaCreateView.as_view()
fisioterapeuta_lista = FisioterapeutaListView.as_view()
especialidade_cadastro = EspecialidadeCreateView.as_view()
especialidade_lista = EspecialidadeListView.as_view()
agenda_cadastro = AgendaCreateView.as_view()
agenda_atualizar = AgendaUpdateView.as_view()
agenda_lista = AgendaListView.as_view()
agenda_deletar = AgendaDeleteView.as_view()

