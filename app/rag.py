from app.embeddings import create_embedding
from app.vectorstore import search_chunks
from app.llm import generate_answer


def ask_question(question):

    # 1. Convert question into embedding
    question_embedding = create_embedding(question)

    # 2. Retrieve relevant chunks
    results = search_chunks(
        query_embedding=question_embedding,
        top_k=3
    )

    # 3. Build context with page numbers
    context_parts = []

    for document, metadata in zip(
        results["documents"][0],
        results["metadatas"][0]
    ):
        page = metadata["page"]

        context_parts.append(
            f"[Page {page}]\n{document}"
        )

    context = "\n\n".join(context_parts)

    # 4. Generate answer
    answer = generate_answer(
        question=question,
        context=context
    )

    return answer, results