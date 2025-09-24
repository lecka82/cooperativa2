from django.db.models import Q
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Coletor
from .forms import ColetorForm

class ColetorListView(LoginRequiredMixin, ListView):
    model = Coletor
    template_name = "coletores/coletores_list.html"
    context_object_name = "coletores"
    paginate_by = 20
    ordering = ["nome"]

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get("q")
        coop = self.request.GET.get("coop")  # "1" / "0"
        if q:
            qs = qs.filter(
                Q(nome__icontains=q) |
                Q(documento__icontains=q) |
                Q(email__icontains=q) |
                Q(telefone__icontains=q)
            )
        if coop in {"0", "1"}:
            qs = qs.filter(faz_parte_cooperativa=(coop == "1"))
        return qs

class ColetorCreateView(LoginRequiredMixin, CreateView):
    model = Coletor
    form_class = ColetorForm
    template_name = "coletores/coletores_form.html"
    success_url = reverse_lazy("coletores:list")

class ColetorUpdateView(LoginRequiredMixin, UpdateView):
    model = Coletor
    form_class = ColetorForm
    template_name = "coletores/coletores_form.html"
    success_url = reverse_lazy("coletores:list")

class ColetorDeleteView(LoginRequiredMixin, DeleteView):
    model = Coletor
    template_name = "coletores/coletores_confirm_delete.html"
    success_url = reverse_lazy("coletores:list")

class ColetorDetailView(LoginRequiredMixin, DetailView):
    model = Coletor
    template_name = "coletores/coletores_detail.html"
    context_object_name = "obj"
