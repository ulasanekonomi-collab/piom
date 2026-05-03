import streamlit as st

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="PIOM Analyzer",
    layout="wide"
)

# =========================
# SESSION STATE INIT
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
# SIDEBAR NAVIGATION
# =========================
st.sidebar.title("PIOM Flow")

steps = [
    "Masalah",
    "Power",
    "Institution",
    "Incentive",
    "Transaction Cost",
    "Behavior",
    "Outcome",
    "Design",
    "Output"
]

selected = st.sidebar.radio("Langkah Analisis", steps)
st.session_state.step = selected

# =========================
# HEADER
# =========================
st.title("PIOM Analyzer")
st.markdown(
    "<p style='font-size:12px; color:gray;'>Dikembangkan oleh Yuhka Sundaya, Ekonomi Pembangunan, Universitas Islam Bandung</p>",
    unsafe_allow_html=True
)
st.caption("Power – Institution – Outcome Map")

# =========================
# HELPER: SUMMARY PANEL
# =========================
def summary():
    st.sidebar.markdown("### 🧠 Ringkasan Sementara")
    st.sidebar.write("**Masalah:**", st.session_state.kasus)
    st.sidebar.write("**Power:**", st.session_state.power_aktor)
    st.sidebar.write("**Institution:**", st.session_state.institution_formal)
    st.sidebar.write("**Outcome:**", st.session_state.outcome)

summary()

# =========================
# STEP: MASALAH
# =========================
if st.session_state.step == "Masalah":
    st.header("Identifikasi Masalah")

    st.session_state.kasus = st.text_area(
        "Tuliskan masalah yang ingin dianalisis",
        value=st.session_state.kasus
    )

    st.session_state.kategori = st.selectbox(
        "Kategori",
        ["Publik", "Bisnis", "Kewirausahaan"]
    )

# =========================
# STEP: POWER
# =========================
elif st.session_state.step == "Power":
    st.header("Power (Kekuasaan)")

    st.session_state.power_aktor = st.text_area(
        "Siapa aktor utama?",
        value=st.session_state.power_aktor
    )

    st.session_state.power_peran = st.text_area(
        "Apa peran mereka?",
        value=st.session_state.power_peran
    )

# =========================
# STEP: INSTITUTION
# =========================
elif st.session_state.step == "Institution":
    st.header("Institution (Kelembagaan)")

    st.session_state.institution_formal = st.text_area(
        "Institusi formal",
        value=st.session_state.institution_formal
    )

    st.session_state.institution_informal = st.text_area(
        "Institusi informal",
        value=st.session_state.institution_informal
    )

# =========================
# STEP: INCENTIVE
# =========================
elif st.session_state.step == "Incentive":
    st.header("Incentive")

    st.session_state.incentive = st.text_area(
        "Apa insentif yang terbentuk?",
        value=st.session_state.incentive
    )

# =========================
# STEP: TRANSACTION COST
# =========================
elif st.session_state.step == "Transaction Cost":
    st.header("Transaction Cost & Informasi")

    st.session_state.cost = st.text_area(
        "Biaya transaksi",
        value=st.session_state.cost
    )

    st.session_state.informasi = st.text_area(
        "Masalah informasi",
        value=st.session_state.informasi
    )

# =========================
# STEP: BEHAVIOR
# =========================
elif st.session_state.step == "Behavior":
    st.header("Behavior")

    st.session_state.behavior = st.text_area(
        "Perilaku yang muncul",
        value=st.session_state.behavior
    )

# =========================
# STEP: OUTCOME
# =========================
elif st.session_state.step == "Outcome":
    st.header("Outcome")

    st.session_state.outcome = st.text_area(
        "Apa hasil dari sistem ini?",
        value=st.session_state.outcome
    )

# =========================
# STEP: DESIGN
# =========================
elif st.session_state.step == "Design":
    st.header("Institutional Design")

    st.session_state.design = st.text_area(
        "Apa solusi atau perbaikan yang diusulkan?",
        value=st.session_state.design
    )

# =========================
# STEP: OUTPUT
# =========================
elif st.session_state.step == "Output":
    st.header("Hasil Analisis")

    st.subheader("📊 Ringkasan PIOM")

    st.write(f"""
    **Masalah:** {st.session_state.kasus}

    **Power:** {st.session_state.power_aktor}

    **Institution:** {st.session_state.institution_formal}

    **Incentive:** {st.session_state.incentive}

    **Transaction Cost:** {st.session_state.cost}

    **Behavior:** {st.session_state.behavior}

    **Outcome:** {st.session_state.outcome}

    **Design:** {st.session_state.design}
    """)

    st.subheader("📝 Draft Policy Brief")

    policy = f"""
Masalah:
{st.session_state.kasus}

Analisis:
Sistem dipengaruhi oleh aktor {st.session_state.power_aktor}, 
dengan aturan {st.session_state.institution_formal}. 
Insentif yang terbentuk adalah {st.session_state.incentive}, 
dengan hambatan berupa {st.session_state.cost}.

Rekomendasi:
{st.session_state.design}
"""

    st.text_area("Policy Brief", policy, height=300)

    st.download_button(
        "Download Policy Brief",
        policy,
        file_name="piom_policy_brief.txt"
    )
