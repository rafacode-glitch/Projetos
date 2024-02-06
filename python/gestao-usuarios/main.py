from flask import Flask, url_for, render_template

# inicialização
app = Flask(__name__)


# rotas
@app.route('/')
def ola_mundo():
    titulo = "Gestão de Usuários"
    usuarios = [
        {"nome": "Maximus", "membro_ativo": True},
        {"nome": "Redy", "membro_ativo": False},
        {"nome": "João", "membro_ativo": False},
        {"nome": "Iron", "membro_ativo": False},
    ]
    return render_template('index.html', titulo=titulo, usuarios=usuarios)


@app.route('/sobre')
def pagina_sobre():
    return "sobre oque?"


# execução
app.run(debug=True)
