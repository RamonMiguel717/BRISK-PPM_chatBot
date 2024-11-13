from sentence_transformers import SentenceTransformer, util
import json

Problemas_arquivo = "Problemas.json"
Respostas_arquivo = "Respostas.json"

# Carrega o modelo pré-treinado
modelo = SentenceTransformer('sentence-transformers/distiluse-base-multilingual-cased-v1')

def chamarNLP(fraseDoUsuario:str):
    with open(Problemas_arquivo) as arquivo:
        arquivo = json.load(arquivo);
        frases = []
        respostas = []

        for chave in arquivo.keys():
            for valores in arquivo[chave]:
                frases.append(valores)
                respostas.append(chave)

    embeddings = modelo.encode(frases)

    # Função para prever a intenção
    embedding_frase_usuario = modelo.encode(fraseDoUsuario)
    similaridades = util.cos_sim(embedding_frase_usuario, embeddings)[0]

    # Encontra a frase mais similar
    indice_mais_similar = similaridades.argmax().item() # Pega o indice da frase que teve a maior pontuação

    confianca = similaridades[indice_mais_similar].item() # Pega a pontuação da frase que foi escolhida

    # Pega as respostas do arquivo
    Respostas = json.load(open(Respostas_arquivo))

    limite_confianca = 0.5
    if confianca < limite_confianca:
        return "Não consegui reconhecer seu problema, vamos te redirecionar para um de nossos atendentes"
    return Respostas[respostas[indice_mais_similar]]


print(chamarNLP(input("Digite sua pergunta: ")))
