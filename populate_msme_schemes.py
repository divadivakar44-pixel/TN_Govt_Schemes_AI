import json
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent
SCHEMES_FILE = PROJECT_DIR / "data" / "processed" / "schemes.json"

OFFICIAL_URL = "https://msmeonline.tn.gov.in/incentives/pdf/GO37.pdf"

msme_schemes = [
    {
        "scheme_id": "TN_MSME_001",
        "scheme_name_en": "Special Capital Subsidy for Thrust Sector Enterprises",
        "scheme_name_ta": "",
        "department": "Micro, Small and Medium Enterprises Department",
        "description_en": (
            "Special capital subsidy for new Micro, Small and Medium "
            "Manufacturing Enterprises in specified thrust sectors in Tamil Nadu."
        ),
        "description_ta": "",
        "eligibility_en": [
            "New Micro, Small and Medium Manufacturing Enterprises located in Tamil Nadu.",
            "The enterprise must have Udyam Registration.",
            "The enterprise must operate in one of the thrust sectors listed in the guidelines."
        ],
        "eligibility_ta": [],
        "benefits_en": [
            "Special capital subsidy is provided to eligible thrust-sector enterprises. "
            "The exact subsidy percentage and amount require further extraction."
        ],
        "benefits_ta": [],
        "subsidy_details": "Exact subsidy amount pending verification.",
        "required_documents_en": [],
        "required_documents_ta": [],
        "application_process_en": "",
        "application_process_ta": "",
        "official_url": OFFICIAL_URL,
        "source_document": "MSME_002",
        "source_page": 29,
        "last_verified": "",
        "verification_status": "pending"
    },
    {
        "scheme_id": "TN_MSME_002",
        "scheme_name_en": "Low Tension Power Tariff Subsidy",
        "scheme_name_ta": "",
        "department": "Micro, Small and Medium Enterprises Department",
        "description_en": (
            "Power tariff assistance for eligible Micro Manufacturing Enterprises "
            "using Low Tension power supply."
        ),
        "description_ta": "",
        "eligibility_en": [
            "Micro Manufacturing Enterprises using Low Tension Power supply (Tariff III).",
            "The extracted guidelines also refer to existing Micro Manufacturing "
            "Enterprises undertaking substantial expansion or diversification."
        ],
        "eligibility_ta": [],
        "benefits_en": [
            "20% of the power charges paid to TANGEDCO for the first 36 months, "
            "from commencement of production or the date of power connection, "
            "whichever is later."
        ],
        "benefits_ta": [],
        "subsidy_details": (
            "20% of eligible power charges for the first 36 months, subject to "
            "the conditions in the official guidelines."
        ),
        "required_documents_en": [],
        "required_documents_ta": [],
        "application_process_en": (
            "The extracted document refers to an Eligibility Certificate and "
            "submission of subsidy claims. Full application instructions need review."
        ),
        "application_process_ta": "",
        "official_url": OFFICIAL_URL,
        "source_document": "MSME_002",
        "source_page": 36,
        "last_verified": "",
        "verification_status": "pending"
    },
    {
        "scheme_id": "TN_MSME_003",
        "scheme_name_en": "Back-Ended Interest Subsidy",
        "scheme_name_ta": "",
        "department": "Micro, Small and Medium Enterprises Department",
        "description_en": (
            "Interest subsidy support for eligible Micro and Small Enterprises "
            "that have availed specified term loans."
        ),
        "description_ta": "",
        "eligibility_en": [
            "Existing Micro and Small Enterprises that have availed term loans "
            "for technology upgradation or modernisation.",
            "Micro and Small Enterprises that have availed term loans under CGTMSE.",
            "Existing Micro and Small Enterprises undertaking substantial "
            "expansion or diversification using CGTMSE loans.",
            "Existing Micro and Small Enterprises upgrading plant and machinery "
            "with specified improved technologies."
        ],
        "eligibility_ta": [],
        "benefits_en": [
            "Interest subsidy assistance is described in the guidelines. "
            "The exact rate and limits need further extraction."
        ],
        "benefits_ta": [],
        "subsidy_details": "Interest subsidy rate and limits pending verification.",
        "required_documents_en": [
            "Udyam Registration Certificate",
            "Bank loan sanction letter",
            "Bank certificate for the interest claim for each quarter"
        ],
        "required_documents_ta": [],
        "application_process_en": "",
        "application_process_ta": "",
        "official_url": OFFICIAL_URL,
        "source_document": "MSME_002",
        "source_page": 38,
        "last_verified": "",
        "verification_status": "pending"
    },
    {
        "scheme_id": "TN_MSME_004",
        "scheme_name_en": "Generator Subsidy",
        "scheme_name_ta": "",
        "department": "Micro, Small and Medium Enterprises Department",
        "description_en": (
            "Generator purchase subsidy for eligible new and existing Micro "
            "Manufacturing Enterprises falling under rural feeders."
        ),
        "description_ta": "",
        "eligibility_en": [
            "New or existing Micro Manufacturing Enterprises falling under a rural feeder.",
            "Only brand-new generator equipment is eligible.",
            "A safety certificate from the Electrical Inspectorate is required.",
            "The generator must be purchased directly from the manufacturer "
            "or through an authorised dealer.",
            "The enterprise must have Udyam Registration."
        ],
        "eligibility_ta": [],
        "benefits_en": [
            "25% of the generator set cost, up to a maximum capacity of 320 KVA.",
            "Maximum subsidy of ₹5 lakh."
        ],
        "benefits_ta": [],
        "subsidy_details": "25% of generator cost; maximum ₹5 lakh; capacity up to 320 KVA.",
        "required_documents_en": [
            "Udyam Registration Certificate",
            "Safety certificate from the Electrical Inspectorate",
            "Authorised dealership certificate, where applicable"
        ],
        "required_documents_ta": [],
        "application_process_en": "",
        "application_process_ta": "",
        "official_url": OFFICIAL_URL,
        "source_document": "MSME_002",
        "source_page": 40,
        "last_verified": "",
        "verification_status": "pending"
    },
    {
        "scheme_id": "TN_MSME_005",
        "scheme_name_en": "Promotion of Energy Audit and Conservation of Energy (PEACE)",
        "scheme_name_ta": "",
        "department": "Micro, Small and Medium Enterprises Department",
        "description_en": (
            "A scheme to encourage MSMEs to undertake energy audits and adopt "
            "energy-efficient technologies and recommendations."
        ),
        "description_ta": "",
        "eligibility_en": [
            "For the energy-audit component: existing manufacturing MSMEs in Tamil Nadu "
            "undertaking an energy audit for the first time, or a subsequent audit "
            "after a minimum gap of three years.",
            "For implementation assistance: manufacturing MSMEs that have undertaken "
            "an energy audit and achieved at least 10% energy savings, subject to the guidelines."
        ],
        "eligibility_ta": [],
        "benefits_en": [
            "Energy audit: 75% of the audit cost, up to ₹1 lakh per energy audit.",
            "Implementation of audit recommendations: 50% of eligible component cost, "
            "up to ₹10 lakh."
        ],
        "benefits_ta": [],
        "subsidy_details": (
            "Energy audit: 75%, maximum ₹1 lakh. "
            "Implementation: 50%, maximum ₹10 lakh."
        ),
        "required_documents_en": [
            "Udyam Registration Certificate",
            "Proof of connected electrical load",
            "Documents relating to engagement of the energy auditor"
        ],
        "required_documents_ta": [],
        "application_process_en": (
            "For implementation assistance, the extracted guidelines state that "
            "MSMEs must apply online within three months after implementation "
            "of the energy-audit recommendations. The upper limit for claim "
            "submission is one year from implementation."
        ),
        "application_process_ta": "",
        "official_url": OFFICIAL_URL,
        "source_document": "MSME_002",
        "source_page": 41,
        "last_verified": "",
        "verification_status": "pending"
    },
    {
        "scheme_id": "TN_MSME_006",
        "scheme_name_en": "Scheme for Acquiring Quality Certifications (Q-CERT)",
        "scheme_name_ta": "",
        "department": "Micro, Small and Medium Enterprises Department",
        "description_en": (
            "Financial assistance to encourage MSMEs to obtain product, process "
            "and other quality certifications."
        ),
        "description_ta": "",
        "eligibility_en": [
            "All Micro, Small and Medium Enterprises in Tamil Nadu."
        ],
        "eligibility_ta": [],
        "benefits_en": [
            "100% reimbursement of certification and consulting charges.",
            "Maximum ₹2 lakh per unit for national certifications.",
            "Maximum ₹10 lakh per unit for international certifications."
        ],
        "benefits_ta": [],
        "subsidy_details": (
            "100% reimbursement; maximum ₹2 lakh for national certifications "
            "and ₹10 lakh for international certifications."
        ),
        "required_documents_en": [],
        "required_documents_ta": [],
        "application_process_en": "",
        "application_process_ta": "",
        "official_url": OFFICIAL_URL,
        "source_document": "MSME_002",
        "source_page": 47,
        "last_verified": "",
        "verification_status": "pending"
    },
    {
        "scheme_id": "TN_MSME_007",
        "scheme_name_en": "Stamp Duty and Registration Charges Assistance",
        "scheme_name_ta": "",
        "department": "Micro, Small and Medium Enterprises Department",
        "description_en": (
            "Assistance relating to stamp duty and registration charges for "
            "eligible new manufacturing enterprises."
        ),
        "description_ta": "",
        "eligibility_en": [
            "Eligible new manufacturing enterprises, subject to the guidelines."
        ],
        "eligibility_ta": [],
        "benefits_en": [
            "50% rebate on the actual value of stamp duty and registration charges paid.",
            "The admissible land area is generally up to five times the factory building's plinth area."
        ],
        "benefits_ta": [],
        "subsidy_details": "50% rebate on eligible stamp duty and registration charges.",
        "required_documents_en": [],
        "required_documents_ta": [],
        "application_process_en": (
            "The extracted guidelines state that the enterprise should apply online "
            "within six months from the date of commencement of commercial production."
        ),
        "application_process_ta": "",
        "official_url": OFFICIAL_URL,
        "source_document": "MSME_002",
        "source_page": 48,
        "last_verified": "",
        "verification_status": "pending"
    },
    {
        "scheme_id": "TN_MSME_008",
        "scheme_name_en": "Subsidy for Asset Creation for Intellectual Property",
        "scheme_name_ta": "",
        "department": "Micro, Small and Medium Enterprises Department",
        "description_en": (
            "Financial assistance for eligible patent, trademark and "
            "Geographical Indication registration costs."
        ),
        "description_ta": "",
        "eligibility_en": [],
        "eligibility_ta": [],
        "benefits_en": [
            "Patent registration: 75% subsidy on eligible filing and first-time "
            "maintenance costs, up to ₹3 lakh per registered patent.",
            "Trademark or Geographical Indication registration: 50% subsidy "
            "on eligible filing costs, up to ₹25,000 per registration."
        ],
        "benefits_ta": [],
        "subsidy_details": (
            "Patent: 75%, maximum ₹3 lakh. "
            "Trademark/GI: 50%, maximum ₹25,000."
        ),
        "required_documents_en": [],
        "required_documents_ta": [],
        "application_process_en": "",
        "application_process_ta": "",
        "official_url": OFFICIAL_URL,
        "source_document": "MSME_002",
        "source_page": 49,
        "last_verified": "",
        "verification_status": "pending"
    },
    {
        "scheme_id": "TN_MSME_009",
        "scheme_name_en": "Scheme for Fund Raising through SME Exchange",
        "scheme_name_ta": "",
        "department": "Micro, Small and Medium Enterprises Department",
        "description_en": (
            "One-time assistance intended to support eligible enterprises "
            "in raising equity capital through listing on an SME Exchange."
        ),
        "description_ta": "",
        "eligibility_en": [
            "Small and Medium Enterprises located in Tamil Nadu. "
            "Further qualification conditions need verification."
        ],
        "eligibility_ta": [],
        "benefits_en": [
            "One-time assistance of 20% of listing expenditure, "
            "up to a maximum of ₹5 lakh for successful listing on the SME Exchange."
        ],
        "benefits_ta": [],
        "subsidy_details": "20% of listing expenditure; maximum ₹5 lakh for successful listing.",
        "required_documents_en": [],
        "required_documents_ta": [],
        "application_process_en": "",
        "application_process_ta": "",
        "official_url": OFFICIAL_URL,
        "source_document": "MSME_002",
        "source_page": 50,
        "last_verified": "",
        "verification_status": "pending"
    }
]


def main():
    SCHEMES_FILE.parent.mkdir(parents=True, exist_ok=True)

    if SCHEMES_FILE.exists():
        with SCHEMES_FILE.open("r", encoding="utf-8") as file:
            existing_schemes = json.load(file)
    else:
        existing_schemes = []

    if not isinstance(existing_schemes, list):
        raise ValueError("schemes.json must contain a JSON list.")

    # Update matching MSME IDs and preserve all other scheme records.
    schemes_by_id = {
        scheme.get("scheme_id"): scheme
        for scheme in existing_schemes
        if isinstance(scheme, dict) and scheme.get("scheme_id")
    }

    for scheme in msme_schemes:
        schemes_by_id[scheme["scheme_id"]] = scheme

    final_schemes = list(schemes_by_id.values())

    with SCHEMES_FILE.open("w", encoding="utf-8") as file:
        json.dump(final_schemes, file, ensure_ascii=False, indent=4)

    print("MSME scheme data created successfully.")
    print(f"Total schemes in file: {len(final_schemes)}")
    print(f"MSME schemes added/updated: {len(msme_schemes)}")
    print(f"Output file: {SCHEMES_FILE}")


if __name__ == "__main__":
    main()