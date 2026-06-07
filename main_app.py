import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="Crack the Black Box",
    page_icon="⬛",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# -----------------------------
# Hidden rule
# -----------------------------
def black_box_rule(word: str) -> str:
    """
    Hidden rule:
    The black box says YES if the English word contains the letter "a".
    """
    return "YES" if "a" in word.lower() else "NO"


INPUTS = [
    {"emoji": "🐱", "word": "cat"},
    {"emoji": "🐶", "word": "dog"},
    {"emoji": "🍕", "word": "pizza"},
    {"emoji": "🤖", "word": "robot"},
    {"emoji": "🍎", "word": "apple"},
    {"emoji": "🐯", "word": "tiger"},
    {"emoji": "🍌", "word": "banana"},
    {"emoji": "🚗", "word": "car"},
    {"emoji": "🌙", "word": "moon"},
    {"emoji": "📱", "word": "phone"},
    {"emoji": "🦓", "word": "zebra"},
    {"emoji": "🏫", "word": "school"},
    {"emoji": "💻", "word": "laptop"},
    {"emoji": "🪑", "word": "chair"},
    {"emoji": "📘", "word": "book"},
    {"emoji": "🎵", "word": "music"},
]

if "history" not in st.session_state:
    st.session_state.history = []

if "selected" not in st.session_state:
    st.session_state.selected = None

if "output" not in st.session_state:
    st.session_state.output = "?"


def test_input(item: dict) -> None:
    result = black_box_rule(item["word"])
    st.session_state.selected = item
    st.session_state.output = result
    st.session_state.history.insert(
        0,
        {
            "emoji": item["emoji"],
            "word": item["word"],
            "result": result,
            "time": datetime.now().strftime("%H:%M:%S"),
        },
    )


def reset_activity() -> None:
    st.session_state.history = []
    st.session_state.selected = None
    st.session_state.output = "?"


st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .stApp {
        background:
            radial-gradient(circle at 7% 4%, rgba(14, 165, 233, 0.16), transparent 24rem),
            radial-gradient(circle at 92% 8%, rgba(99, 102, 241, 0.16), transparent 28rem),
            linear-gradient(180deg, #f8fafc 0%, #eef4ff 100%);
        color: #0f172a;
    }

    .block-container {
        max-width: 1240px;
        padding-top: 1.6rem;
        padding-bottom: 2.6rem;
    }

    #MainMenu, footer, header {
        visibility: hidden;
    }

    .hero {
        border-radius: 32px;
        padding: 2.65rem 3rem;
        background:
            radial-gradient(circle at 15% 18%, rgba(56, 189, 248, 0.18), transparent 16rem),
            radial-gradient(circle at 88% 22%, rgba(129, 140, 248, 0.20), transparent 18rem),
            linear-gradient(135deg, #020617 0%, #0f172a 54%, #312e81 100%);
        border: 1px solid rgba(255, 255, 255, 0.14);
        box-shadow: 0 28px 76px rgba(15, 23, 42, 0.24);
        margin-bottom: 1.5rem;
    }

    .hero h1 {
        margin: 0;
        color: white;
        font-size: clamp(2.8rem, 5vw, 4.5rem);
        line-height: 0.95;
        letter-spacing: -0.075em;
        font-weight: 950;
    }

    .hero p {
        max-width: 820px;
        color: #dbeafe;
        font-size: 1.08rem;
        line-height: 1.72;
        margin-top: 1rem;
        margin-bottom: 0;
    }

    .glass {
        background: rgba(255, 255, 255, 0.76);
        border: 1px solid rgba(148, 163, 184, 0.22);
        border-radius: 30px;
        padding: 1.55rem;
        box-shadow: 0 18px 46px rgba(15, 23, 42, 0.075);
        backdrop-filter: blur(18px);
        -webkit-backdrop-filter: blur(18px);
        height: 100%;
    }

    .glass h2 {
        margin-top: 0;
        letter-spacing: -0.04em;
        font-size: 1.7rem;
        color: #0f172a;
    }

    .muted {
        color: #64748b;
        line-height: 1.62;
        font-size: 1rem;
    }

    .blackbox {
        min-height: 392px;
        border-radius: 34px;
        padding: 2.4rem;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
        color: white;
        background:
            radial-gradient(circle at 20% 18%, rgba(6, 182, 212, 0.20), transparent 15rem),
            radial-gradient(circle at 84% 18%, rgba(124, 58, 237, 0.22), transparent 15rem),
            linear-gradient(145deg, #020617 0%, #0b1220 60%, #111827 100%);
        border: 1px solid rgba(255, 255, 255, 0.12);
        box-shadow: 0 30px 72px rgba(2, 6, 23, 0.30);
    }

    .blackbox-label {
        font-size: 0.78rem;
        letter-spacing: 0.28em;
        font-weight: 950;
        color: #7dd3fc;
        margin-bottom: 1.2rem;
    }

    .blackbox-small {
        font-size: 0.94rem;
        font-weight: 800;
        color: #cbd5e1;
    }

    .selected-input {
        font-size: clamp(2.5rem, 4vw, 3.7rem);
        font-weight: 950;
        line-height: 1.05;
        letter-spacing: -0.05em;
        margin: 0.85rem 0 1.25rem;
        min-height: 4.5rem;
    }

    .output-unknown, .output-yes, .output-no {
        font-size: clamp(4.4rem, 7vw, 6.4rem);
        font-weight: 950;
        line-height: 1;
        letter-spacing: -0.06em;
        margin-top: 0.55rem;
    }

    .output-unknown {
        color: #e2e8f0;
    }

    .output-yes {
        color: #4ade80;
        text-shadow: 0 0 30px rgba(74, 222, 128, 0.35);
    }

    .output-no {
        color: #fb7185;
        text-shadow: 0 0 30px rgba(251, 113, 133, 0.35);
    }

    /* Force all Streamlit button wrappers and buttons to be full, equal-size cards */
    div[data-testid="column"] {
        padding: 0 0.25rem;
    }

    div[data-testid="stButton"] {
        width: 100% !important;
        display: block !important;
    }

    div[data-testid="stButton"] > button {
        width: 100% !important;
        height: 104px !important;
        min-height: 104px !important;
        max-height: 104px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        text-align: center !important;
        border-radius: 22px !important;
        border: 1.5px solid rgba(148, 163, 184, 0.32) !important;
        background:
            linear-gradient(180deg, rgba(255, 255, 255, 0.98), rgba(248, 250, 252, 0.97)) !important;
        color: #0f172a !important;
        font-size: 1.02rem !important;
        font-weight: 800 !important;
        line-height: 1.3 !important;
        box-shadow:
            0 14px 28px rgba(15, 23, 42, 0.08),
            inset 0 1px 0 rgba(255, 255, 255, 0.9) !important;
        transition: all 0.16s ease !important;
        white-space: pre-line !important;
        padding: 0.4rem !important;
        margin: 0 !important;
    }

    div[data-testid="stButton"] > button:hover {
        border-color: rgba(37, 99, 235, 0.72) !important;
        transform: translateY(-3px);
        box-shadow:
            0 20px 40px rgba(37, 99, 235, 0.18),
            inset 0 1px 0 rgba(255, 255, 255, 1) !important;
        color: #1d4ed8 !important;
        background:
            radial-gradient(circle at 50% 0%, rgba(219, 234, 254, 0.8), transparent 70%),
            linear-gradient(180deg, #ffffff, #f8fbff) !important;
    }

    div[data-testid="stButton"] > button:active {
        transform: translateY(0px);
    }

    .history-row {
        display: flex;
        align-items: center;
        justify-content: space-between;
        background: rgba(248, 250, 252, 0.96);
        border: 1px solid rgba(226, 232, 240, 0.95);
        border-radius: 18px;
        padding: 0.88rem 0.95rem;
        margin-bottom: 0.62rem;
    }

    .history-word {
        color: #0f172a;
        font-weight: 850;
    }

    .badge-yes, .badge-no {
        border-radius: 999px;
        padding: 0.35rem 0.8rem;
        font-weight: 950;
        font-size: 0.78rem;
    }

    .badge-yes {
        background: #dcfce7;
        color: #166534;
    }

    .badge-no {
        background: #ffe4e6;
        color: #9f1239;
    }

    .empty-state {
        background: #eff6ff;
        border: 1px solid #bfdbfe;
        color: #1e40af;
        border-radius: 18px;
        padding: 1rem;
        line-height: 1.55;
        font-weight: 650;
    }

    .reflection-box {
        background: #f8fafc;
        border: 1px solid #dbeafe;
        border-radius: 22px;
        padding: 1.05rem;
        line-height: 1.65;
        color: #1e3a8a;
    }

    .takeaway {
        background:
            radial-gradient(circle at top left, rgba(56, 189, 248, 0.16), transparent 12rem),
            linear-gradient(135deg, #eef2ff, #ecfeff);
        border: 1px solid #c7d2fe;
        border-radius: 22px;
        padding: 1.1rem;
        color: #312e81;
        font-weight: 850;
        line-height: 1.6;
    }

    .soft-divider {
        height: 1px;
        background: linear-gradient(90deg, transparent, rgba(148, 163, 184, 0.42), transparent);
        margin: 1.1rem 0;
    }

    /* Smaller reset button only */
    .reset-button-wrapper div[data-testid="stButton"] > button {
        height: 48px !important;
        min-height: 48px !important;
        max-height: 48px !important;
        border-radius: 14px !important;
        font-size: 0.95rem !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# Hero
# -----------------------------
st.markdown(
    """
    <div class="hero">
        <h1>Crack the Black Box</h1>
        <p>
            You are testing a mysterious AI system. It only answers <b>YES</b> or <b>NO</b>.
            Your mission is to collect evidence and figure out the hidden pattern.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# Main layout
# -----------------------------
left, right = st.columns([1.08, 0.92], gap="large")

with left:
    st.markdown("## 1. Test an input")
    st.markdown(
        '<p class="muted">Click a card. The black box will answer only <b>YES</b> or <b>NO</b>. Your goal is to find one rule that explains every result.</p>',
        unsafe_allow_html=True,
    )

    cols_per_row = 4
    for i in range(0, len(INPUTS), cols_per_row):
        cols = st.columns(cols_per_row, gap="medium")
        for col, item in zip(cols, INPUTS[i:i + cols_per_row]):
            with col:
                if st.button(f"{item['emoji']}\n{item['word']}", key=f"input_{item['word']}", use_container_width=True):
                    test_input(item)
                    st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)

with right:
    selected = st.session_state.selected
    selected_text = "Choose a card" if selected is None else f"{selected['emoji']} {selected['word']}"
    output_value = st.session_state.output

    if output_value == "YES":
        output_class = "output-yes"
    elif output_value == "NO":
        output_class = "output-no"
    else:
        output_class = "output-unknown"

    st.markdown(
        f"""
        <div class="blackbox">
            <div class="blackbox-label">BLACK BOX AI</div>
            <div class="blackbox-small">Input</div>
            <div class="selected-input">{selected_text}</div>
            <div class="blackbox-small">Output</div>
            <div class="{output_class}">{output_value}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.write("")

# -----------------------------
# Evidence + reflection
# -----------------------------
bottom_left, bottom_right = st.columns([1, 1], gap="large")

with bottom_left:
    st.markdown("## 2. Evidence Board")

    if not st.session_state.history:
        st.markdown(
            """
            <div class="empty-state">
                No evidence yet. Test a few cards and watch which inputs get YES or NO.
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        for row in st.session_state.history[:16]:
            badge_class = "badge-yes" if row["result"] == "YES" else "badge-no"
            st.markdown(
                f"""
                <div class="history-row">
                    <span><span style="font-size:1.35rem;">{row["emoji"]}</span>
                    <span class="history-word">{row["word"]}</span></span>
                    <span class="{badge_class}">{row["result"]}</span>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown("</div>", unsafe_allow_html=True)

with bottom_right:  
    st.markdown("## 3. Reflection")

    st.markdown(
        """
        <div class="reflection-box">
            <b>Think like a researcher:</b><br>
            A good rule should explain both the YES examples and the NO examples.
            If one example breaks your rule, your rule needs to change.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<div class="soft-divider"></div>', unsafe_allow_html=True)

    st.markdown("#### Discussion questions")
    st.markdown(
        """
        1. Did the black box use the pattern you expected?  
        2. How many tests were enough to feel confident?  
        3. Why can hidden patterns be risky in real AI systems?
        """
    )

    st.markdown(
        """
        <div class="takeaway">
            Takeaway: AI can find patterns, but not always the pattern humans want.
            That is why we need evidence, testing, and explainability.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")
    st.markdown('<div class="reset-button-wrapper">', unsafe_allow_html=True)
    if st.button("Start Over", key="reset_button", use_container_width=False):
        reset_activity()
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)
