import random
import string
from IPython.display import display, HTML
import ipywidgets as widgets

# Função geradora de senhas
def gerar_senha(comprimento, usar_maiusculas, usar_minusculas, usar_numeros, usar_simbolos):
    caracteres = ""
    if usar_maiusculas:
        caracteres += string.ascii_uppercase
    if usar_minusculas:
        caracteres += string.ascii_lowercase
    if usar_numeros:
        caracteres += string.digits
    if usar_simbolos:
        caracteres += string.punctuation

    if not caracteres:
        return "Selecione ao menos um tipo de caractere!"

    return ''.join(random.choice(caracteres) for _ in range(comprimento))

# Widgets de entrada
comprimento_slider = widgets.IntSlider(value=12, min=4, max=32, description='Comprimento:')
maiusculas_check = widgets.Checkbox(value=True, description='Maiúsculas')
minusculas_check = widgets.Checkbox(value=True, description='Minúsculas')
numeros_check = widgets.Checkbox(value=True, description='Números')
simbolos_check = widgets.Checkbox(value=False, description='Símbolos')

botao_gerar = widgets.Button(description='Gerar Senha')
saida = widgets.Output()

# Função acionada ao clicar no botão
def ao_clicar_botao(b):
    senha = gerar_senha(
        comprimento_slider.value,
        maiusculas_check.value,
        minusculas_check.value,
        numeros_check.value,
        simbolos_check.value
    )
    with saida:
        saida.clear_output()
        display(HTML(f"<p style='font-size:20px; color:green;'><b>Senha Gerada:</b> {senha}</p>"))

botao_gerar.on_click(ao_clicar_botao)

# Exibir interface
display(widgets.VBox([
    comprimento_slider,
    widgets.HBox([maiusculas_check, minusculas_check, numeros_check, simbolos_check]),
    botao_gerar,
    saida
]))
