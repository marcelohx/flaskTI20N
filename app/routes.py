from app import app
from flask import render_template
from flask import request
import requests
import json
link = "https://flaskti20nmarcelo-default-rtdb.firebaseio.com/" #conectar ao banco
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', titulo="Página Principal")
@app.route('/contato')
def contato():
    return render_template('contato.html', titulo="Contato")

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html', titulo="Cadastro")

@app.route('/cadastrarUsuario',methods=['POST'])
def cadastrarUsuario():
    try:
        cpf = request.form.get("cpf")
        nome = request.form.get("nome")
        telefone = request.form.get("telefone")
        endereco = request.form.get("endereco")
        dados = {"cpf":cpf,"nome":nome,"telefone":telefone,"endereco":endereco}
        requisicao = requests.post(f'{link}/cadastrar/.json', data = json.dumps(dados))
        return 'Cadastrado com sucesso!'
    except Exception as e:
        return f'Ocorreu um erro\n\n {e}'


