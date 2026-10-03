from app.loader import load_pdf

pages = load_pdf("data/book.pdf")

print("Total pages:", len(pages))

for page in pages[:3]:
    print("\n--- Page", page["page"], "---")
    print(page["text"][:1000])