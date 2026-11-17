
from nemoguardrails.actions import action

ALLOWED_KEYWORDS = [
    "scheme", "farmer", "agriculture", "agricultural",
    "subsidy", "farming", "horticulture", "irrigation",
    "msme", "business", "government", "eligibility",
    "benefit", "application", "விவசாயம்", "விவசாயி",
    "மானியம்", "திட்டம்", "தகுதி", "வேளாண்மை",
    "தோட்டக்கலை", "சிறு தொழில்"
]

@action(name="is_scheme_question")
async def is_scheme_question(question: str) -> bool:
    question = question.lower()

    return any(
        keyword in question
        for keyword in ALLOWED_KEYWORDS
    )
