# 🎥 Talk to YouTube: Local RAG Assistant

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-LCEL-green?style=for-the-badge)
![Llama 3](https://img.shields.io/badge/Model-Llama%203-orange?style=for-the-badge)
![Ollama](https://img.shields.io/badge/Runtime-Ollama-white?style=for-the-badge&logo=ollama&logoColor=black)

> **A privacy-first, zero-cost AI assistant that allows users to chat with YouTube videos locally using Llama 3.**

## 💡 The Problem

Students and professionals spend hours watching long technical videos to find specific information. Cloud-based AI tools raise privacy concerns and incur high API costs for processing large transcripts.

## 🛠️ The Solution

I built a **Local RAG (Retrieval-Augmented Generation)** pipeline that runs entirely on your machine.

1.  **Extracts** transcripts from YouTube URLs.
2.  **Embeds** text into a local Vector Database (ChromaDB).
3.  **Retrieves** relevant context based on user queries.
4.  **Generates** answers using Llama 3 (via Ollama).

**Result:** Fast, free, and private video analysis.

---

## 📸 Demo

## 🎥 Demo

https://github.com/user-attachments/assets/e610fe8a-49ed-46ca-bd75-0120dee9f251

---

## 🏗️ System Architecture

This project implements a standard RAG pipeline using **LangChain Expression Language (LCEL)** for orchestration.

1.  **Ingestion:** `YoutubeLoader` fetches raw text.
2.  **Chunking:** `RecursiveCharacterTextSplitter` breaks text into 1000-char chunks to fit context windows.
3.  **Embedding:** `HuggingFaceEmbeddings` converts text to vector representations (`all-MiniLM-L6-v2`).
4.  **Storage:** `ChromaDB` stores vectors locally for similarity search.
5.  **Inference:** `ChatOllama` connects to the local Llama 3 instance to synthesize the answer.

---

## 🚀 How to Run Locally

### Prerequisites

- **Python 3.8+**
- **Ollama:** [Download here](https://ollama.com)
- **Memory:** At least 8GB RAM recommended (to run Llama 3 smoothy).

### Step 1: Clone the Repository

````bash
git clone [https://github.com/YOUR_USERNAME/local-rag-video-analyst.git](https://github.com/YOUR_USERNAME/local-rag-video-analyst.git)
cd local-rag-video-analyst

### Step 2: Install Dependencies
```bash
pip install langchain langchain-community langchain-chroma langchain-huggingface sentence-transformers youtube-transcript-api streamlit

### Step 3: Initialize the model
Open your terminal and pull Llama 3 model
```bash
ollama pull llama3

### Step 4; Run the App
```bash
streamlit run app.py
````
