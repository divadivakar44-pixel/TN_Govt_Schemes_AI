
from pathlib import Path
from dotenv import load_dotenv
from nemoguardrails import RailsConfig, LLMRails

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent
CONFIG_DIR = BASE_DIR / "guardrails"

config = RailsConfig.from_path(str(CONFIG_DIR))

from guardrails.actions import is_scheme_question

rails = LLMRails(config)
rails.register_action(is_scheme_question)

questions = [
    "What government schemes are available for farmers?",
    "தமிழ்நாட்டில் விவசாயிகளுக்கு என்ன திட்டங்கள் உள்ளன?",
    "Who won yesterday's cricket match?"
]

for question in questions:
    print("\nQuestion:", question)

    response = rails.generate(
        messages=[
            {"role": "user", "content": question}
        ]
    )

    print("Response:", response["content"])

