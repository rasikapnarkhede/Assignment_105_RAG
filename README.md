# Assignment_105_RAG
This project is a Retrieval-Augmented Generation (RAG) chatbot that:

Loads .txt documents from a folder

Encodes them using SentenceTransformers

Retrieves the most relevant documents for a user query using FAISS

Generates answers using Google Generative AI (PaLM) via google-generative-ai

Provides a Streamlit-based UI for user interaction

SentenceTransformers is a Python library for encoding sentences or paragraphs into dense vector embeddings that capture semantic meaning. It is built on top of HuggingFace Transformers and [PyTorch/TF].

Developed by UKPLab, it's widely used in:

Semantic search

Information retrieval (e.g., RAG)

Clustering

Text classification

Duplicate question detection

RAG combines two powerful ideas:

Retrieval – Find relevant information from a knowledge base (e.g., your .txt files).

Generation – Use a language model to answer questions using that information.

🧱 Components of a Simple RAG Pipeline
1. Document Store (Your .txt files)
You give it a folder of documents.
🔹 These contain the knowledge your bot will use.

2. Embedding Model (e.g., SentenceTransformer)
This converts each document into a vector (a list of numbers that represent meaning).
🔹 It allows the computer to compare meaning, not just words.

3. FAISS Index
This is a fast tool to search for similar documents based on a question’s embedding.

4. Retriever Function
Given a user query, it:

Embeds the query.

Finds top k similar documents from FAISS.

5. Generative Model (e.g., PaLM via google.generativeai)
It takes:

The retrieved context, and

The user question,
And generates an answer using both.

🧠 How It Works (Step-by-step)
📂 Load .txt files → break into readable text chunks.

🔢 Embed all chunks using SentenceTransformer.

📚 Store embeddings in FAISS index.

🤔 User asks a question → embed the question.

🔍 Retrieve top k matching documents.

🧠 Feed these docs + question into a language model (PaLM) → get answer.

💬 Show the answer to the user.


