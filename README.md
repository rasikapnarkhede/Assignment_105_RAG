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


