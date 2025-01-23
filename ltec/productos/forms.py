from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'categoria', 'imagen', 'activo']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['imagen'].widget.attrs.update({
            'class': 'custom-file-input'
        })
        self.fields['imagen'].widget.clear_checkbox_label = "Vaciar"
        self.fields['imagen'].widget.input_text = "Cambiar imagen"
