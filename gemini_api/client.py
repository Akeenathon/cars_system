import google.generativeai as gemini
import os


# Configurando a API KEY
gemini.configure(api_key='AIzaSyAFpH31XoGhsZQuyEj0CgrqgVqT2yOmwX0')

def get_car_ai_bio(model, brand, year):
    # Criando a prompt (pergunta) a ser feita, (brand, model, year são as informações sobre o veiculo que sera adicionado)
    prompt = '''
    Me moestre uma descrição de venda para o carro {} {} {} em apenas 250 caracteres.
    Fale coisas especificas sobre esse modelo, descreva especificações tecnicas sobre este carro
    e detalhes especificos como consumo por litro e potencia do motor
    '''.format(brand, model, year)
    model = gemini.GenerativeModel('gemini-1.5-flash')  # Modelo gemini a ser usado, pode ser 'gemini-pro' ou 'gemini-1.5-flash
    response = model.generate_content(prompt)   # Gerando a resposta da pergunta feita (prompt)

    return response.text    # Retornando o texto gerado