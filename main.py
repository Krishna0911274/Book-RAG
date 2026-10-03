from app.loader import load_pdf
from app.splitter import split_text

pages = load_pdf("data/book.pdf")

all_text = ""

for page in pages:
    all_text += page["text"] + "\n"
    
chunks = split_text(all_text)

print("Total pages:", len(pages))
print("Total chunks:", len(chunks))

for i, chunk in enumerate(chunks[:5],start=1):
    print(f"\n--- Chunk {i} ---")
    print(chunk)