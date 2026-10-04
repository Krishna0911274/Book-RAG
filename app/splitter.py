def split_pages(pages, chunk_size=500, chunk_overlap=50):
    chunks = []

    chunk_id = 1

    for page in pages:
        text = page["text"]
        page_number = page["page"]

        start = 0

        while start < len(text):
            end = start + chunk_size

            chunk_text = text[start:end]

            if chunk_text.strip():
                chunks.append({
                    "id": f"chunk_{chunk_id}",
                    "text": chunk_text,
                    "page": page_number
                })

                chunk_id += 1

            start = end - chunk_overlap

    return chunks