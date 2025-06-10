from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gerar', methods=['POST'])
def gerar():
    tamanho = request.form.get('tamanho', '12')
    letras = 'letras' in request.form
    numeros = 'numeros' in request.form
    simbolos = 'simbolos' in request.form

    try:
        # Chama o código Java passando os argumentos
        resultado = subprocess.check_output([
            'java', 'GeradorSenha',
            tamanho,
            str(letras),
            str(numeros),
            str(simbolos)
        ])
        senha = resultado.decode('utf-8').strip()
    except subprocess.CalledProcessError:
        senha = 'Erro ao gerar senha.'

    return render_template('index.html', senha=senha)

if __name__ == '__main__':
    app.run(debug=True)
