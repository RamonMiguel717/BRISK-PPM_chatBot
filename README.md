# BRISK-PPM ChatBot (MVP) - Guia de Implantação e Descrição do Projeto

O **BRISK-PPM ChatBot** é um sistema desenvolvido para oferecer suporte automatizado e interação inteligente com usuários. Este guia descreve o processo de configuração e execução do projeto em um ambiente local. O sistema foi criado como um MVP (Produto Mínimo Viável), com foco em usabilidade e funcionalidades básicas, utilizando **Flask** para o backend e tecnologias simples para o frontend.

---

## Objetivo do Projeto

O objetivo do **BRISK-PPM ChatBot** é facilitar a comunicação entre os usuários e o sistema, oferecendo respostas rápidas e precisas a perguntas frequentes. Este MVP utiliza uma abordagem baseada em arquivos JSON para armazenar e processar perguntas e respostas, garantindo flexibilidade e fácil manutenção.

---

## Tecnologias Utilizadas

### Backend:
- **Python 3.8+**
- **Flask** - Framework web leve e versátil.
- **Sentence Transformers** - Para processamento de linguagem natural.

### Frontend:
- **HTML5**
- **CSS3**
- **JavaScript**

---

## Equipe de Desenvolvimento

- **Backend**:  
  - Ramon Miguel  
  - Tiago  

- **Frontend**:  
  - Murilo Farias  
  - Arthur Gabriel  
  - Leticia Parreiras  
  - Maria Eduarda Marques  

---

## Funcionalidades

1. **Reconhecimento de Frases**: Respostas automatizadas baseadas em correspondência com perguntas predefinidas.
2. **Interface Simples**: Design básico para facilitar a interação com o chatbot.
3. **Facilidade de Personalização**: Arquitetura baseada em JSON, permitindo ajustes rápidos nas perguntas e respostas.

---

## Estrutura do Repositório

```bash
BRISK-PPM_chatBot/
├── Site_integrado/            # Código do sistema integrado
│   ├── templates/             # Templates HTML
│   │   └── main.py            # Script principal do Flask
│   └── static/                # Arquivos estáticos (CSS, JS, imagens)
├── Perguntas.json             # Base de perguntas
├── Respostas.json             # Base de respostas
└── README.md                  # Guia de implantação e documentação
```

---

## Configuração e Execução

### Pré-requisitos

Antes de começar, verifique os seguintes requisitos:

- **Sistema Operacional**: Windows, macOS ou Linux.
- **Python**: Versão 3.8 ou superior.
- **Gerenciador de Pacotes**: `pip`.

### Passo 1: Instalar Dependências

No terminal, execute os comandos para instalar as bibliotecas necessárias:

```bash
pip install Flask
pip install sentence_transformers
```

### Passo 2: Clonar o Repositório

Clone o repositório oficial para o ambiente local:

```bash
git clone https://github.com/RamonMiguel717/BRISK-PPM_chatBot.git
```

### Passo 3: Executar o ChatBot

Para executar o chatbot, navegue até o diretório Site_integrado/templates e execute o arquivo main.py com o seguinte comando:

   ```bash
   python Site_Flask/templates/main.py
   ```

   > Certifique-se de que está no diretório correto antes de executar o comando.

---

## Personalização do ChatBot

1. **Editar Arquivos JSON**:  
   - **Perguntas.json**: Adicione ou edite as perguntas que o chatbot pode reconhecer.  
   - **Respostas.json**: Defina as respostas associadas às perguntas.  

2. **Testar**: Insira frases de exemplo na interface e avalie as respostas geradas.  

3. **Ajustar**: Refine os arquivos JSON para melhorar a precisão do chatbot.

---

## Melhorias Futuras

1. Substituir a lógica baseada em JSON por um banco de dados para maior escalabilidade.
2. Implementar uma interface gráfica mais moderna e responsiva.
3. Incorporar algoritmos avançados de processamento de linguagem natural para respostas mais dinâmicas.
4. Adicionar suporte para múltiplos idiomas.

---
