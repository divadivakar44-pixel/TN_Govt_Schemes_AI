
from utils.bilingual_answer import generate_answer

test_context = """
Scheme: Example Agriculture Scheme
Department: Agriculture
Benefit: Financial assistance as described in the official scheme data.
Official URL: https://www.tn.gov.in/
"""

question = "What is the benefit of this agriculture scheme?"

answer = generate_answer(question, test_context)

print("\nQuestion:", question)
print("\nAI Answer:", answer)
