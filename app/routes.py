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

@app.route('/listar')
def listarTudo():
    try:
        requisicao = requests.get(f'{link}/cadastrar/.json') #solicitação dos dados
        dicionario = requisicao.json()
        return dicionario
    except Exception as e:
        return f'Algo deu errado \n\n{e}'

@app.route('/listarIndividual', methods=['POST'])
def listarIndividual():
    try:
        requisicao = requests.get(f'{link}/cadastrar/.json')
        dicionario = requisicao.json()
        cpf = request.form.get("cpf")
        idCadastro = "" #Armazenar o ID indiviual

        for codigo in dicionario:
            chave = dicionario[codigo]['cpf']
            if chave == cpf:
                idCadastro = codigo
                endereco = dicionario[codigo]['endereco']
                nome = dicionario[codigo]['nome']
                telefone = dicionario[codigo]['telefone']
                return f'id do Cadastro: {idCadastro}\nNome: {nome}\nEndereco: {endereco}\nTelefone: {telefone}'
    except Exception as e:
        return f'Algo deu errado \n\n{e}'

@app.route('/atualizar')
def atualizar():
    try:
        dados = {"nome":"João"}
        requisicao = requests.patch(f'{link}/cadastrar/-O89htddyr8QVQxaj2iI/.json', data=json.dumps(dados))
        return "Atualizado com sucesso!"
    except Exception as e:
        return f'Algo deu errado\n\n {e}'

@app.route('/excluir')
def excluir():
    try:
        requisicao = requests.delete(f'{link}/cadastrar/-O8JxobEHMlnpuI8vtY9/.json')
        return "Excluir com sucesso!"
    except Exception as e:
        return f"Algo deu errado\n\n {e}"