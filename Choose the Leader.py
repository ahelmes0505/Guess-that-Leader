import streamlit as st
import random

# ----------------------------
# PAGE CONFIG (FUN LOOK)
# ----------------------------
st.set_page_config(
    page_title="Match the Leader 🎯",
    page_icon="🎉",
    layout="centered"
)

st.markdown(
    """
    <style>
    .fact-box {
        background-color: #f0f6ff;
        padding: 15px;
        border-radius: 12px;
        margin-bottom: 12px;
        font-size: 17px;
    }
    .leader-button button {
        width: 100%;
        border-radius: 10px;
        font-size: 14px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ----------------------------
# DATA
# ----------------------------
leaders = [
    "Danny", "Emily", "Ellis", "Sharad",
    "Maggie", "Michelle", "Luis", "Mary", "Wes"
]

facts = [
    ("Once slept on the roof of their house in a sleeping bag", "Danny"),
    ("Has 30 aunts and uncles and 50 cousins", "Emily"),
    ("First concert was the Backstreet Boys", "Ellis"),
    ("Chose math over biology and became the only engineer among doctors", "Sharad"),
    ("Was a PBS kids show tap‑dancing TV star at age five", "Maggie"),
    ("Applied to be on The Amazing Race", "Michelle"),
    ("Former soccer player until a high‑school injury", "Luis"),
    ("Teaches a 6am bootcamp several mornings a week", "Mary"),
    ("Kindergarten marriage → best man years later", "Wes"),
]

# Shuffle once
if "shuffled_facts" not in st.session_state:
    st.session_state.shuffled_facts = random.sample(facts, len(facts))
    st.session_state.answers = {}

# ----------------------------
# HEADER
# ----------------------------
st.title("🎯 Match the Leader")
st.caption("Can you guess which fun fact belongs to who?")

st.divider()

# ----------------------------
# GAME UI
# ----------------------------
for idx, (fact, _) in enumerate(st.session_state.shuffled_facts):
    st.markdown(f"<div class='fact-box'>❓ <b>Fact {idx+1}:</b> {fact}</div>", unsafe_allow_html=True)

    cols = st.columns(3)
    for i, leader in enumerate(leaders):
        with cols[i % 3]:
            if st.button(leader, key=f"{idx}_{leader}"):
                st.session_state.answers[fact] = leader

# ----------------------------
# SUBMIT
# ----------------------------
st.divider()

if st.button("✅ Submit Answers"):
    score = 0
    st.subheader("Results 🏆")

    for fact, correct in st.session_state.shuffled_facts:
        guess = st.session_state.answers.get(fact, "No guess")
        if guess == correct:
            st.success(f"✅ {fact} → {correct}")
            score += 1
        else:
            st.error(f"❌ {fact} → You guessed {guess}, correct was {correct}")

    st.metric("Final Score", f"{score} / {len(facts)}")

    if score == len(facts):
        st.balloons()
        