import streamlit as st
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

# Configuração da página do Streamlit
st.set_page_config(page_title="Agente Escola de Desenho", page_icon="🎨", layout="centered")

st.title("🎨 Assistente Virtual - Escola de Desenho")
st.write("Consulte as políticas, regimentos e documentos internos da instituição de forma direta.")

# Carrega o banco vetorial
@st.cache_resource
def carregar_banco():
    modelo_embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    return Chroma(persist_directory="./banco_vetorial", embedding_function=modelo_embeddings)

with st.spinner("Carregando a base de conhecimento..."):
    banco = carregar_banco()
    # Reduzimos para k=2 para trazer menos blocos e focar no mais importante
    retriever = banco.as_retriever(search_kwargs={"k": 2})

# Gerenciamento do histórico de conversas
if "mensagens" not in st.session_state:
    st.session_state.mensagens = []

for mensagem in st.session_state.mensagens:
    with st.chat_message(mensagem["role"]):
        st.markdown(mensagem["content"])

# Caixa de input do chat
if pergunta := st.chat_input("Digite sua dúvida..."):
    st.session_state.mensagens.append({"role": "user", "content": pergunta})
    with st.chat_message("user"):
        st.markdown(pergunta)

    with st.chat_message("assistant"):
        with st.spinner("Buscando resposta precisa..."):
            docs = retriever.invoke(pergunta)
            
            if not docs:
                resposta = "Não encontrei essa informação nos documentos disponíveis."
            else:
                # Pegamos apenas o trecho mais relevante para evitar excesso de texto
                melhor_doc = docs[0]
                fonte = melhor_doc.metadata.get('source', 'Documento Interno')
                conteudo = melhor_doc.page_content.strip()
                
                # Resposta estruturada, limpa e direta
                resposta = f"{conteudo}\n\n*📄 Fonte: {fonte}*"
            
            st.markdown(resposta)
            st.session_state.mensagens.append({"role": "assistant", "content": resposta})