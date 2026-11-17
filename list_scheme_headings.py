
import json
import re

INPUT_FILE = "data/processed/extracted_documents.json"

patterns = [
    r"CHAPTER\s+\d+",
    r"SCHEME",
    r"SUBSIDY",
    r"INCENTIVE",
    r"ASSISTANCE",
    r"PEACE",
    r"Q-CERT",
    r"TWEES",
    r"ENTREPRENEUR",
]

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    documents = json.load(f)

print("=" * 75)
print("GOVERNMENT SCHEME HEADING INDEX")
print("=" * 75)

for doc in documents:
    source = doc.get("source_id", "UNKNOWN")
    page = doc.get("page_number", "N/A")
    content = doc.get("content", "")

    lines = content.splitlines()
    matches = []

    for line in lines:
        cleaned = " ".join(line.split())

        if len(cleaned) < 5 or len(cleaned) > 180:
            continue

        if any(
            re.search(pattern, cleaned, re.IGNORECASE)
            for pattern in patterns
        ):
            matches.append(cleaned)

    if matches:
        print(f"\nSOURCE: {source} | PAGE: {page}")

        for heading in matches:
            print(" -", heading)

print("\nHEADING INDEX COMPLETED")
