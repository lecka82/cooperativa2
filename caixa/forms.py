from django import forms
from .models import LancamentoCaixa

class LancamentoCaixaForm(forms.ModelForm):
    class Meta:
        model = LancamentoCaixa
        fields = ["tipo", "categoria", "material", "quantidade_kg",
                  "valor", "descricao", "coletor", "data"]
        widgets = {
            "quantidade_kg": forms.NumberInput(attrs={"step": "0.001", "min": "0"}),
            "valor": forms.NumberInput(attrs={"step": "0.01", "min": "0"}),
            "data": forms.DateInput(attrs={"type": "date"}),
        }

    def clean(self):
        cleaned = super().clean()
        # dispara o clean() do model para eventual cálculo automático do valor
        instance = self.instance
        instance.tipo = cleaned.get("tipo")
        instance.categoria = cleaned.get("categoria")
        instance.material = cleaned.get("material")
        instance.quantidade_kg = cleaned.get("quantidade_kg")
        instance.valor = cleaned.get("valor")
        instance.clean()
        cleaned["valor"] = instance.valor
        return cleaned
