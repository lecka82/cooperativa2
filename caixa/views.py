# views.py
from django.db.models import Q, Sum
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import LancamentoCaixa
from .forms import LancamentoCaixaForm

class CaixaListView(LoginRequiredMixin, ListView):
    model = LancamentoCaixa
    template_name = "caixa/caixa_list.html"
    context_object_name = "lancamentos"
    paginate_by = 20
    ordering = ["-data", "-criado_em"]

    def get_queryset(self):
        qs = super().get_queryset()

        # filtros GET
        q = self.request.GET.get("q")
        tipo = self.request.GET.get("tipo")          # E / S
        cat = self.request.GET.get("categoria")      # arrecadacao / repasse / despesa / ajuste
        dt_ini = self.request.GET.get("de")
        dt_fim = self.request.GET.get("ate")
        coletor_id = self.request.GET.get("coletor")
        material_id = self.request.GET.get("material")

        if q:
            qs = qs.filter(Q(descricao__icontains=q))
        if tipo in {"E", "S"}:
            qs = qs.filter(tipo=tipo)
        if cat:
            qs = qs.filter(categoria=cat)
        if dt_ini:
            qs = qs.filter(data__gte=dt_ini)
        if dt_fim:
            qs = qs.filter(data__lte=dt_fim)
        if coletor_id:
            qs = qs.filter(coletor_id=coletor_id)
        if material_id:
            qs = qs.filter(material_id=material_id)

        qs = qs.select_related("coletor", "material")

        # ✅ guarde o queryset *antes* da paginação
        self.qs_full = qs
        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        # ✅ use o queryset completo (não paginado) para agregados
        base = getattr(self, "qs_full", LancamentoCaixa.objects.none())
        aggs = base.aggregate(
            total_entradas=Sum("valor", filter=Q(tipo="E")),
            total_saidas=Sum("valor", filter=Q(tipo="S")),
        )
        total_entradas = aggs["total_entradas"] or 0
        total_saidas = aggs["total_saidas"] or 0
        saldo = total_entradas - total_saidas

        ctx.update({
            "total_entradas": total_entradas,
            "total_saidas": total_saidas,
            "saldo": saldo,
            "TIPOS": LancamentoCaixa.TIPO,
            "CATEGORIAS": dict(LancamentoCaixa._meta.get_field("categoria").choices),
        })
        return ctx

class CaixaCreateView(LoginRequiredMixin, CreateView):
    model = LancamentoCaixa
    form_class = LancamentoCaixaForm
    template_name = "caixa/caixa_form.html"
    success_url = reverse_lazy("caixa:list")

class CaixaUpdateView(LoginRequiredMixin, UpdateView):
    model = LancamentoCaixa
    form_class = LancamentoCaixaForm
    template_name = "caixa/caixa_form.html"
    success_url = reverse_lazy("caixa:list")

class CaixaDeleteView(LoginRequiredMixin, DeleteView):
    model = LancamentoCaixa
    template_name = "caixa/caixa_confirm_delete.html"
    success_url = reverse_lazy("caixa:list")

class CaixaDetailView(LoginRequiredMixin, DetailView):
    model = LancamentoCaixa
    template_name = "caixa/caixa_detail.html"
    context_object_name = "obj"
