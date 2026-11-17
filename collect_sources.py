
import json
import requests
import hashlib
from pathlib import Path
from datetime import datetime, timezone

BASE_DIR = Path(__file__).resolve().parent
SOURCE_FILE = BASE_DIR / "data" / "sources.json"
RAW_DIR = BASE_DIR / "data" / "raw"

RAW_DIR.mkdir(parents=True, exist_ok=True)

with open(SOURCE_FILE, "r", encoding="utf-8") as file:
    sources = json.load(file)

report = []

headers = {
    "User-Agent": "TN-Govt-Schemes-Research-Assistant/1.0"
}

for source in sources:
    source_id = source["source_id"]
    department = source["department"]
    url = source["url"]

    print(f"\nDownloading: {source_id}")
    print(f"Department: {department}")

    try:
        response = requests.get(
            url,
            headers=headers,
            timeout=60
        )

        response.raise_for_status()

        content_type = response.headers.get(
            "Content-Type", ""
        ).lower()

        if "pdf" in content_type or url.lower().endswith(".pdf"):
            extension = ".pdf"
        else:
            extension = ".html"

        filename = f"{source_id}{extension}"
        department_folder = RAW_DIR / department.lower().replace(
            " ", "_"
        )

        department_folder.mkdir(
            parents=True,
            exist_ok=True
        )

        output_file = department_folder / filename
        output_file.write_bytes(response.content)

        checksum = hashlib.sha256(
            response.content
        ).hexdigest()

        report.append({
            "source_id": source_id,
            "department": department,
            "source_url": url,
            "downloaded_file": str(output_file.relative_to(BASE_DIR)),
            "status": "success",
            "http_status": response.status_code,
            "content_type": content_type,
            "sha256": checksum,
            "downloaded_at": datetime.now(
                timezone.utc
            ).isoformat()
        })

        print(f"SUCCESS: {output_file}")

    except requests.RequestException as error:

        print(f"DOWNLOAD FAILED: {error}")

        report.append({
            "source_id": source_id,
            "department": department,
            "source_url": url,
            "status": "failed",
            "error": str(error)
        })

report_file = BASE_DIR / "data" / "download_report.json"

with open(report_file, "w", encoding="utf-8") as file:
    json.dump(
        report,
        file,
        indent=4,
        ensure_ascii=False
    )

print("\n================================")
print("DATA COLLECTION COMPLETED")
print("================================")

success = sum(
    1 for item in report
    if item["status"] == "success"
)

print(f"Total sources: {len(report)}")
print(f"Successful downloads: {success}")
print(f"Failed downloads: {len(report) - success}")
print(f"Report: {report_file}")
