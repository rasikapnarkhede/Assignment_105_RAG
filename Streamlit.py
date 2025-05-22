import streamlit as st

# === Streamlit Frontend ===
st.title("📚 Retrieval-Augmented QA Chatbot")

# Input: Path to your documents folder (already extracted)
doc_folder = st.text_input("Enter path to your documents folder:", "/content/RAG_extracted")

# Input: User question
user_question = st.text_input("Ask a question based on the documents:")

# Action: Submit question
submit = st.button("Get Answer")

# You can connect the following variables to your backend:
# - doc_folder → the folder path you pass to os.walk()
# - user_question → the query you pass to retrieve() and generate_answer()

# Below is placeholder output (you replace this with actual backend output)
if submit:
    with st.spinner("Processing..."):
        # Call your backend functions here
        # retrieved_docs = retrieve(user_question)
        # answer = generate_answer(user_question, retrieved_docs)
        answer = "Paris is the capital of France."  # placeholder
        retrieved_docs = [("RAG/Inida.txt")]

    # Output: Answer
    st.markdown("### ✅ Answer:")
    st.write(answer)

    # Output: Sources
    st.markdown("### 📄 Source Documents")
    for doc_name, doc_text in retrieved_docs:
        with st.expander(f"Source: {doc_name}"):
            st.write(doc_text[:500] + "...")  # show first 500 characters
