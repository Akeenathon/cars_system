from django import forms
from .models import Car


class CarForm(forms.ModelForm):

    class Meta:
        model = Car
        exclude = ['favorited_by',]
        widgets = {
            'brand': forms.Select(attrs={'class': 'form-control'}),
            'model': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Modelo do veiculo'}),
            'color': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cor do veiculo'}),
            'factory_year': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ano de Fabricação'}),
            'model_year': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ano do Modelo'}),
            'plate': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Placa do veiculo'}),
            'value': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Valor do veiculo'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control', 'placeholder': 'Imagem do veiculo'}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Deixar em branco para gerar descrição automatica', 'rows': 3}),
        }
        labels = {
            'brand': 'Marca',
            'model': 'Modelo',
            'color': 'Cor',
            'factory_year': 'Ano de Fabricação',
            'model_year': 'Ano do Modelo',
            'plate': 'Placa',
            'value': 'Valor',
            'photo': 'Imagem',
            'bio': 'Descrição',
        }

    def clean_value(self):   # Validação de valor dos veiculos cadastrados
        value = self.cleaned_data.get('value')
        if value < 5000:
            self.add_error('value', 'Valor de veiculo deve ser superior à R$5.000,00')

        return value
    
    def clean_factory_year(self):   # Validação de ano de fabricação dos veiculos cadastrados
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year < 1975:
            self.add_error('factory_year', 'Ano de fabricação deve ser superior à 1975')

        return factory_year
