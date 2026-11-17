
import json
from pathlib import Path
from bs4 import BeautifulSoup
from pypdf import PdfReader

BASE_DIR = Path(__file__).resolve().parent
REPORT_FILE = BASE_DIR / "data" / "download_report.json"
OUTPUT_FILE = BASE_DIR / "data" / "processed" / "extracted_documents.json"

with open(REPORT_FILE, "r", encoding="utf-8") as file:
    report = json.load(file)

documents = []

for item in report:

    if item["status"] != "success":
        continue

    file_path = BASE_DIR / item["downloaded_file"]

    print(f"\nExtracting: {file_path.name}")

    try:

        if file_path.suffix.lower() == ".pdf":

            reader = PdfReader(str(file_path))

            for page_number, page in enumerate(reader.pages, start=1):

                text = page.extract_text() or ""

                documents.append({
                    "source_id": item["source_id"],
                    "department": item["department"],
                    "file_name": file_path.name,
                    "page_number": page_number,
                    "content": text.strip()
                })

        elif file_path.suffix.lower() == ".html":

            html = file_path.read_bytes()

            soup = BeautifulSoup(html, "html.parser")

            for element in soup([
                "script", "style", "noscript", "nav", "footer"
            ]):
                element.decompose()

            text = soup.get_text(
                separator="\n",
                strip=True
            )

            documents.append({
                "source_id": item["source_id"],
                "department": item["department"],
                "file_name": file_path.name,
                "page_number": None,
                "content": text
            })

        print("Extraction successful")

    except Exception as error:
        print(f"Extraction failed: {error}")

OUTPUT_FILE.parent.mkdir(
    parents=True,
    exist_ok=True
)

with open(OUTPUT_FILE, "w", encoding="utf-8") as file:

    json.dump(
        documents,
        file,
        ensure_ascii=False,
        indent=4
    )

print("\n================================")
print("TEXT EXTRACTION COMPLETED")
print("================================")

print(f"Extracted records: {len(documents)}")
print(f"Output: {OUTPUT_FILE}")
