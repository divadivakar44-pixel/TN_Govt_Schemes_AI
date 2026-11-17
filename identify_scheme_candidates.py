
import json
import re

INPUT_FILE = "data/processed/extracted_documents.json"

keywords = [
    "scheme",
    "incentive",
    "subsidy",
    "eligibility",
    "eligible",
    "benefit",
    "assistance",
    "application",
    "entrepreneur",
    "agriculture",
    "farmer",
    "capital",
    "grant",
    "திட்டம்",
    "மானியம்",
    "விவசாயி"
]

with open(INPUT_FILE, "r", encoding="utf-8") as file:
    documents = json.load(file)

print("SCANNING EXTRACTED GOVERNMENT DOCUMENTS")
print("=" * 65)

matches = 0

for doc in documents:
    content = doc.get("content", "")
    source = doc.get("source_id", "UNKNOWN")
    page = doc.get("page_number", "N/A")

    found = [
        word for word in keywords
        if re.search(re.escape(word), content, re.IGNORECASE)
    ]

    if found:
        matches += 1

        print(f"\nSOURCE: {source}")
        print(f"PAGE: {page}")
        print(f"KEYWORDS: {', '.join(found)}")

        # Print a useful excerpt around the first keyword
        positions = [
            content.lower().find(word.lower())
            for word in found
            if content.lower().find(word.lower()) >= 0
        ]

        if positions:
            start = max(0, positions[0] - 250)
            end = min(len(content), positions[0] + 900)
            print("EXTRACT:")
            print(content[start:end])
            print("-" * 65)

print("\nSCAN COMPLETED")
print("TOTAL DOCUMENTS:", len(documents))
print("DOCUMENTS WITH MATCHING KEYWORDS:", matches)
