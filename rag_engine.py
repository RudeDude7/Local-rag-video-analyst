import os
from langchain_community.document_loaders import YoutubeLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

# This function does all the work
def process_video_and_ask(video_url, question):
    
    # 1. LOAD
    print("Loading video transcript...")
    loader = YoutubeLoader.from_youtube_url(video_url, add_video_info=False)
    docs = loader.load()

    # 2. SPLIT
    print("Splitting text...")
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    splits = text_splitter.split_documents(docs)

    # 3. EMBED
    print("Initializing embedding model...")
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    # 4. STORE
    print("Creating vector database...")
    vectorstore = Chroma.from_documents(documents=splits, embedding=embeddings)
    retriever = vectorstore.as_retriever()

    # 5. SETUP LLM
    print("Setting up Llama 3...")
    llm = ChatOllama(model="llama3")

    # 6. DEFINE PROMPT
    template = """Answer the question based only on the following context:
    {context}

    Question: {question}
    """
    prompt = ChatPromptTemplate.from_template(template)

    # 7. BUILD CHAIN (The LCEL Way - No "chains" import needed!)
    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    rag_chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    # 8. RUN
    print("Thinking...")
    response = rag_chain.invoke(question)
    
    return response