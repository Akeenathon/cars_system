from django import forms
from models import Car


class CarForm(forms.ModelForm):

    class Meta:
        model = Car
        fields = '__all__'

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
