from flask import Flask, render_template, request
from Site_Flask import consultarBot

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/index.html')
def home2():
    return render_template('index.html')

mensagens = []
@app.route('/pag_sup.html', methods=['GET', 'POST'])
def pagSuporte():
    mensagem_usuario = ''
    if request.method == 'POST':
        mensagem_usuario = request.form['mensagemUsuario']
        if mensagem_usuario:
            mensagens.append(mensagem_usuario)
            mensagens.append(consultarBot.chamarNLP(mensagem_usuario))

    return render_template('pag_sup.html', mensagens = mensagens)

if __name__ == '__main__':
    app.run(debug=True)
