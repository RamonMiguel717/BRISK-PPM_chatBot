from flask import Flask, render_template, request
from Site_Flask import consultarBot

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/index.html')
def home2():
    return render_template('index.html')

@app.route('/pag_sup.html', methods=['GET', 'POST'])
def pagSuporte():
    mensagem = ''
    pergunta = ''
    if request.method == 'POST':
        pergunta = request.form['mensagemUsuario']
        if pergunta:
            mensagem = consultarBot.chamarNLP(pergunta)

    return render_template('pag_sup.html', mensagem = mensagem, pergunta = pergunta)

if __name__ == '__main__':
    app.run(debug=True)
