# Assistente Virtual - Escola de Desenho (RAG)

## Descrição Geral do Projeto
Este projeto consiste em um Agente de Inteligência Artificial (Assistente Virtual) desenvolvido para a Escola de Desenho. O objetivo é responder de forma rápida e precisa a dúvidas de alunos e colaboradores sobre políticas, regimentos internos e normas da instituição. 

O sistema utiliza a arquitetura RAG (Retrieval-Augmented Generation) para buscar informações diretamente nos documentos oficiais (PDFs) da escola, garantindo que as respostas sejam baseadas em fatos reais e evitando alucinações da IA.

## Arquitetura da Solução
A solução foi construída em duas etapas principais:
1. **Processamento de Dados (Backend):** Os documentos em PDF foram lidos, divididos em blocos de texto (chunks) e transformados em vetores matemáticos (embeddings) que foram armazenados em um banco de dados vetorial local (ChromaDB).
2. **Interface e Recuperação (Frontend/RAG):** Uma interface web foi construída com Streamlit. Quando o usuário faz uma pergunta, o sistema converte a pergunta em vetor, busca os trechos mais similares no ChromaDB, e exibe a resposta exata junto com a citação da fonte do documento original.

## Tecnologias e Ferramentas Utilizadas
- **Linguagem:** Python
- **Framework de IA:** LangChain
- **Embeddings:** HuggingFace (`all-MiniLM-L6-v2`)
- **Banco Vetorial:** ChromaDB
- **Interface Web:** Streamlit
- **Deploy em Nuvem:** Streamlit Community Cloud

## Instruções para Executar o Projeto (Localmente)
Para rodar este projeto na sua máquina, siga os passos abaixo:

1. Clone o repositório:
```bash
git clone [https://github.com/Clara-Gii/agente-ia-escola-desenho.git](https://github.com/Clara-Gii/agente-ia-escola-desenho.git)
cd agente-ia-escola-desenho

# 2. Instale as dependências:
pip install -r requirements.txt

# 3. Execute a aplicação web:
streamlit run app.py
