import streamlit as st

# =========================
# HELPER FUNCTIONS
# =========================
def score_level(text):
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

# =========================
# SIDEBAR
# =========================
st.sidebar.title("PIOM Flow")

steps = [
    "Masalah","Power","Institution","Incentive",
    "Transaction Cost","Behavior","Outcome","Design","Output"
]

st.session_state.step = st.sidebar.radio("Langkah Analisis", steps)

# =========================
# HEADER
# =========================
st.title("PIOM Analyzer")
st.markdown(
    "<p style='font-size:12px;color:gray;'>Dikembangkan oleh Yuhka Sundaya · Ekonomi Pembangunan · Universitas Islam Bandung</p>",
    unsafe_allow_html=True
)

# =========================
# MASALAH
# =========================
if st.session_state.step == "Masalah":
    st.header("Identifikasi Masalah")

    st.text_area("Masalah", key="kasus")

# =========================
# POWER
# =========================
elif st.session_state.step == "Power":
    st.header("Power")

    st.session_state.power_aktor = st.text_area("Aktor")

    st.markdown("### Pertanyaan Kritis")
    st.write("Siapa yang diuntungkan?")
    st.write("Siapa punya kekuasaan?")
    st.write("Siapa dirugikan?")

# =========================
# INSTITUTION
# =========================
elif st.session_state.step == "Institution":
    st.header("Institution")

    st.session_state.institution_formal = st.text_area("Formal")
    st.session_state.institution_informal = st.text_area("Informal")

    st.markdown("### Pertanyaan Kritis")
    st.write("Aturan apa berlaku?")
    st.write("Norma apa dominan?")
    st.write("Apakah ditegakkan?")

# =========================
# INCENTIVE
# =========================
elif st.session_state.step == "Incentive":
    st.header("Incentive")

    st.session_state.incentive = st.text_area("Insentif")

    st.markdown("### Pertanyaan Kritis")
    st.write("Apa yang memotivasi?")
    st.write("Apakah effort dihargai?")
    st.write("Ada reward?")

# =========================
# COST
# =========================
elif st.session_state.step == "Transaction Cost":
    st.header("Transaction Cost")

    st.session_state.cost = st.text_area("Biaya")

    st.markdown("### Pertanyaan Kritis")
    st.write("Apa yang membuat sulit?")
    st.write("Ada biaya tersembunyi?")
    st.write("Info mudah diakses?")

# =========================
# BEHAVIOR
# =========================
elif st.session_state.step == "Behavior":
    st.header("Behavior")

    st.session_state.behavior = st.text_area("Perilaku")

    st.markdown("### Pertanyaan Kritis")
    st.write("Bagaimana respon aktor?")
    st.write("Apakah rasional?")

# =========================
# OUTCOME
# =========================
elif st.session_state.step == "Outcome":
    st.header("Outcome")

    st.session_state.outcome = st.text_area("Hasil")

    st.markdown("### Pertanyaan Kritis")
    st.write("Efisien?")
    st.write("Adil?")

# =========================
# DESIGN
# =========================
elif st.session_state.step == "Design":
    st.header("Design")

    st.session_state.design = st.text_area("Solusi")

    st.markdown("### Pertanyaan Kritis")
    st.write("Apa diubah?")
    st.write("Bagaimana insentif diperbaiki?")
    st.write("Bagaimana cost diturunkan?")

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
