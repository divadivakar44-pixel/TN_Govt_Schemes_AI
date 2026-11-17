
import streamlit as st
import requests

# ----------------------------------
# PAGE CONFIGURATION
# ----------------------------------

st.set_page_config(
    page_title="Tamil Nadu Government Schemes AI",
    page_icon="🌾",
    layout="wide"
)

API_URL = "http://127.0.0.1:8000"

# ----------------------------------
# CUSTOM CSS
# ----------------------------------

st.markdown("""
<style>
.main-title {
    font-size: 32px;
    font-weight: bold;
    color: #16803c;
}
.subtitle {
    font-size: 16px;
    color: gray;
}
</style>
""", unsafe_allow_html=True)

# ----------------------------------
# HEADER
# ----------------------------------

st.markdown(
    '<div class="main-title">🌾 Tamil Nadu Government Schemes AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">AI-powered Agriculture, Farmers Welfare and MSME Scheme Assistant</div>',
    unsafe_allow_html=True
)

st.divider()

# ----------------------------------
# LANGUAGE SELECTION
# ----------------------------------

language = st.selectbox(
    "Select Language / மொழியைத் தேர்ந்தெடுக்கவும்",
    ["English", "தமிழ்"]
)

if language == "English":
    welcome = (
        "Hello! I can help you understand Tamil Nadu "
        "Government Agriculture, Farmers Welfare and MSME schemes. "
        "Ask me about eligibility, benefits and application procedures."
    )
    input_label = "Ask your question"
    placeholder = "Example: What subsidies are available for farmers?"
    button_label = "Submit Question"
else:
    welcome = (
        "வணக்கம்! தமிழ்நாடு அரசு வேளாண்மை, விவசாயிகள் நலன் "
        "மற்றும் குறு, சிறு மற்றும் நடுத்தர தொழில் திட்டங்கள் "
        "பற்றி கேள்விகள் கேட்கலாம்."
    )
    input_label = "உங்கள் கேள்வியைக் கேளுங்கள்"
    placeholder = "உதாரணம்: விவசாயிகளுக்கு என்ன மானியங்கள் உள்ளன?"
    button_label = "கேள்வியை சமர்ப்பிக்கவும்"

# ----------------------------------
# BACKEND STATUS
# ----------------------------------

try:
    health_response = requests.get(
        f"{API_URL}/health",
        timeout=5
    )

    if health_response.status_code == 200:
        st.success("Backend Connected")
    else:
        st.error("Backend is not responding correctly")

except requests.RequestException:
    st.error(
        "Backend Disconnected. "
        "Please start FastAPI in another CMD window."
    )

# ----------------------------------
# CHAT HISTORY
# ----------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

if not st.session_state.messages:
    with st.chat_message("assistant"):
        st.write(welcome)

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

        if message.get("sources"):
            st.markdown("**Official Sources:**")
            for source in message["sources"]:
                if isinstance(source, str) and source.startswith(
                    ("https://", "http://")
                ):
                    st.markdown(f"- [{source}]({source})")
                else:
                    st.write(f"- {source}")

# ----------------------------------
# QUESTION INPUT
# ----------------------------------

question = st.text_input(
    input_label,
    placeholder=placeholder,
    key="question_input"
)

if st.button(button_label, type="primary"):

    if not question.strip():
        st.warning("Please enter a question.")

    else:
        st.session_state.messages.append({
            "role": "user",
            "content": question
        })

        with st.spinner("Searching government scheme information..."):

            try:
                response = requests.post(
                    f"{API_URL}/chat",
                    json={"question": question},
                    timeout=180
                )

                response.raise_for_status()

                result = response.json()

                answer = result.get(
                    "answer",
                    "No answer returned by the backend."
                )

                sources = result.get("sources", [])

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": answer,
                    "sources": sources
                })

                st.rerun()

            except requests.exceptions.Timeout:
                st.error("Request timed out. Please try again.")

            except requests.exceptions.RequestException as error:
                st.error(f"Backend API error: {error}")

            except ValueError:
                st.error("The backend returned an invalid response.")

# ----------------------------------
# SIDEBAR
# ----------------------------------

with st.sidebar:
    st.title("About this Assistant")

    st.write(
        "This application helps users explore Tamil Nadu "
        "Government Agriculture, Farmers Welfare and MSME schemes."
    )

    st.divider()

    st.subheader("Supported Topics")

    st.write("- Agriculture schemes")
    st.write("- Farmer welfare")
    st.write("- Horticulture")
    st.write("- MSME incentives")
    st.write("- Eligibility")
    st.write("- Subsidies and benefits")

    st.divider()

    if st.button("Clear Chat History"):
        st.session_state.messages = []
        st.rerun()

    st.caption("Powered by LangChain, Neo4j, OpenAI, NeMo Guardrails and FastAPI.")
