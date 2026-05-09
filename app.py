import streamlit as st
import json
import os

SAVE_FILE = "piom_autosave.json"

FIELDS = [
    "kasus",
    "power_aktor",

    "institution_formal",
    "institution_informal",

    "incentive",
    "cost",

    "behavior",
    "outcome",
    "design",

    # tambahan baru
    "informasi",
    "nilai",

    # simulation variables
    "benefit_score",
    "cost_score",
    "info_score",
    "moral_score"
]
def autosave():
    data = {k: st.session_state.get(k, "") for k in FIELDS}
    try:
        with open(SAVE_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except Exception as e:
        st.write("Error autosave:", e)
def autoload():
    try:
        if os.path.exists(SAVE_FILE):
            with open(SAVE_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)

            for k in FIELDS:
                if k in data:
                    st.session_state[k] = data[k]
    except Exception as e:
        st.write("Error autoload:", e)        
# =========================
# HELPER FUNCTIONS
# =========================
def score_level(text):
    if not text:
        return 0

    length = len(text.split())

    if length < 10:
        return 1
    elif length < 30:
        return 2
    else:
        return 3
# =========================
# PIOM SIMULATION ENGINE
# =========================

def calculate_behavior_score(B, C, N, M):

    # Formula PIOM
    S = B + N + M - C

    return S


def interpret_score(S):

    if S <= 0:
        return "Perilaku sulit berubah"

    elif S <= 5:
        return "Perubahan mungkin terjadi"

    elif S <= 10:
        return "Perubahan cukup kuat"

    else:
        return "Perubahan sangat mungkin terjadi"
    if not text:
        return 0
    length = len(text.split())
    if length < 10:
        return 1
    elif length < 25:
        return 2
    else:
        return 3


def analyze_piom():
    ins_score = score_level(st.session_state.incentive)
    cost_score = score_level(st.session_state.cost)

    if ins_score >= 2 and cost_score >= 2:
        root = "Masalah didorong oleh kombinasi insentif yang tidak tepat dan biaya transaksi yang tinggi."
    elif ins_score >= 2:
        root = "Masalah terutama disebabkan oleh insentif yang tidak selaras."
    elif cost_score >= 2:
        root = "Masalah terutama disebabkan oleh biaya transaksi yang tinggi."
    else:
        root = "Masalah belum cukup teridentifikasi secara struktural."

    causal = f"""
Institusi: {st.session_state.institution_formal}
→ menciptakan insentif: {st.session_state.incentive}
→ memengaruhi perilaku: {st.session_state.behavior}
→ menghasilkan outcome: {st.session_state.outcome}
"""

    return root, causal


# =========================
# PAGE CONFIG
# =========================
st.set_page_config(page_title="PIOM Analyzer", layout="wide")

# =========================
# SESSION STATE
# =========================
def init_state():
    defaults = {
        "step": "Masalah",
        "kasus": "",
        "kategori": "Publik",
        "power_aktor": "",
        "power_peran": "",
        "institution_formal": "",
        "institution_informal": "",
        "incentive": "",
        "cost": "",
        "informasi": "",
        "behavior": "",
        "outcome": "",
        "design": "",
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

init_state()
autoload()

# =========================
# SIDEBAR
# =========================
st.sidebar.title("PIOM Flow")

steps = [
    "Masalah","Power","Institution","Incentive",
    "Transaction Cost","Behavior","Outcome","Design","Simulation","Output"
]

st.session_state.step = st.sidebar.radio("Langkah Analisis", steps)

# =========================
# HEADER
# =========================
st.title("PIOM Analyzer")
# ✅ DEBUG DI SINI
st.sidebar.write("DEBUG kasus:", st.session_state.get("kasus"))
st.markdown(
    "<p style='font-size:12px;color:gray;'>Dikembangkan oleh Yuhka Sundaya · Ekonomi Pembangunan · Universitas Islam Bandung</p>",
    unsafe_allow_html=True
)

# =========================
# MASALAH
# =========================
if st.session_state.step == "Masalah":
    st.header("Identifikasi Masalah")

    st.text_area("Masalah", key="kasus", on_change=autosave)

# =========================
# POWER
# =========================
elif st.session_state.step == "Power":
    st.header("Power")

    st.text_area("Aktor", key="power_aktor", on_change=autosave)

    st.markdown("### Pertanyaan Kritis")
    st.write("Siapa yang diuntungkan?")
    st.write("Siapa punya kekuasaan?")
    st.write("Siapa dirugikan?")

# =========================
# INSTITUTION
# =========================
elif st.session_state.step == "Institution":
    st.header("Institution")

    st.text_area("Formal", key="institution_formal", on_change=autosave)
    st.text_area("Informal", key="institution_informal", on_change=autosave)

    st.markdown("### Pertanyaan Kritis")
    st.write("Aturan apa berlaku?")
    st.write("Norma apa dominan?")
    st.write("Apakah ditegakkan?")

# =========================
# INCENTIVE
# =========================
elif st.session_state.step == "Incentive":
    st.header("Incentive")

    st.text_area("Insentif", key="incentive", on_change=autosave)

    st.markdown("### Pertanyaan Kritis")
    st.write("Apa yang memotivasi?")
    st.write("Apakah effort dihargai?")
    st.write("Ada reward?")

# =========================
# COST
# =========================
elif st.session_state.step == "Transaction Cost":
    st.header("Transaction Cost")

    st.text_area("Biaya", key="cost", on_change=autosave)

    st.markdown("### Pertanyaan Kritis")
    st.write("Apa yang membuat sulit?")
    st.write("Ada biaya tersembunyi?")
    st.write("Info mudah diakses?")

# =========================
# BEHAVIOR
# =========================
elif st.session_state.step == "Behavior":
    st.header("Behavior")

    st.text_area("Perilaku", key="behavior", on_change=autosave)

    st.markdown("### Pertanyaan Kritis")
    st.write("Bagaimana respon aktor?")
    st.write("Apakah rasional?")

# =========================
# OUTCOME
# =========================
elif st.session_state.step == "Outcome":
    st.header("Outcome")

    st.text_area("Outcome", key="outcome", on_change=autosave)
    st.markdown("### Pertanyaan Kritis")
    st.write("Efisien?")
    st.write("Adil?")

# =========================
# DESIGN
# =========================
elif st.session_state.step == "Design":
    st.header("Design")

    st.text_area("Solusi", key="design", on_change=autosave)

    st.markdown("### Pertanyaan Kritis")
    st.write("Apa diubah?")
    st.write("Bagaimana insentif diperbaiki?")
    st.write("Bagaimana cost diturunkan?")
# =========================
# SIMULATION
# =========================

elif st.session_state.step == "Simulation":

    st.header("PIOM Simulation Engine")

    st.markdown("""
    Simulasi perubahan perilaku berdasarkan:
    - Benefit / Incentive
    - Transaction Cost
    - Information
    - Moral Support
    """)

    # INPUT SIMULASI
    B = st.slider("Benefit / Incentive", 0, 10, 5)
    C = st.slider("Transaction Cost", 0, 10, 5)
    N = st.slider("Information / Framing", 0, 10, 5)
    M = st.slider("Moral / Normative Support", 0, 10, 5)

    # HITUNG
    S = calculate_behavior_score(B, C, N, M)

    # OUTPUT
    st.subheader("Behavior Score")

    st.metric("Score", S)

    st.success(interpret_score(S))

    # MATRIX
    st.subheader("PIOM Design Matrix")

    st.table({
        "Variable": ["Benefit", "Cost", "Information", "Moral"],
        "Score": [B, C, N, M]
    })
# =========================
# OUTPUT
# =========================
elif st.session_state.step == "Output":
    st.header("Hasil Analisis")

    root, causal = analyze_piom()

    st.subheader("Analisis Inti")
    st.success(root)

    st.subheader("Rantai Kausal")
    st.write(causal)
