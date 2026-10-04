from app.rag import ask_question


while True:

    question = input("\nAsk a question about the book: ")

    if question.lower() == "exit":
        break

    answer, results = ask_question(question)

    print("\nAnswer:")
    print(answer)

    print("\nSources:")

    for metadata in results["metadatas"][0]:
        print(f"Page {metadata['page']}")