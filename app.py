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
    "<p style='font-size:12px; color:gray;'>Dikembangkan oleh Yuhka Sundaya · Ekonomi Pembangunan · Universitas Islam Bandung</p>",
    unsafe_allow_html=True
)
st.caption("Power – Institution – Outcome Map")

# =========================
# SUMMARY PANEL
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
st.markdown("### Pertanyaan Kritis")

st.write("Siapa yang paling diuntungkan dari sistem ini?")
st.write("Siapa yang memiliki kekuasaan menentukan aturan?")
st.write("Apakah ada aktor yang dirugikan?")
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
st.markdown("### Pertanyaan Kritis")

st.write("Aturan apa yang secara formal mengatur sistem ini?")
st.write("Norma informal apa yang sebenarnya lebih dominan?")
st.write("Apakah aturan ini ditegakkan?")
# =========================
# STEP: INCENTIVE
# =========================
elif st.session_state.step == "Incentive":
    st.header("Incentive")

    st.session_state.incentive = st.text_area(
        "Apa insentif yang terbentuk?",
        value=st.session_state.incentive
    )
st.markdown("### Pertanyaan Kritis")

st.write("Apa yang membuat aktor memilih tindakan tertentu?")
st.write("Apakah usaha tinggi menghasilkan hasil lebih baik?")
st.write("Apakah sistem memberi reward atau justru toleransi?")
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
st.markdown("### Pertanyaan Kritis")

st.write("Apa yang membuat sistem ini tidak efisien?")
st.write("Apa biaya tersembunyi yang muncul?")
st.write("Apakah informasi mudah diakses?")
# =========================
# STEP: BEHAVIOR
# =========================
elif st.session_state.step == "Behavior":
    st.header("Behavior")

    st.session_state.behavior = st.text_area(
        "Perilaku yang muncul",
        value=st.session_state.behavior
    )
st.markdown("### Pertanyaan Kritis")

st.write("Bagaimana aktor merespons sistem ini?")
st.write("Apakah perilaku ini rasional?")
st.write("Apakah ada penyimpangan dari aturan?")
# =========================
# STEP: OUTCOME
# =========================
elif st.session_state.step == "Outcome":
    st.header("Outcome")

    st.session_state.outcome = st.text_area(
        "Apa hasil dari sistem ini?",
        value=st.session_state.outcome
    )
st.markdown("### Pertanyaan Kritis")

st.write("Apa dampak dari sistem ini?")
st.write("Apakah hasilnya efisien?")
st.write("Apakah hasilnya adil?")
# =========================
# STEP: DESIGN
# =========================
elif st.session_state.step == "Design":
    st.header("Institutional Design")

    st.session_state.design = st.text_area(
        "Apa solusi atau perbaikan yang diusulkan?",
        value=st.session_state.design
    )
st.markdown("### Pertanyaan Kritis")

st.write("Apa yang harus diubah dalam sistem?")
st.write("Bagaimana memperbaiki insentif?")
st.write("Bagaimana menurunkan biaya transaksi?")
# =========================
# STEP: OUTPUT
# =========================
elif st.session_state.step == "Output":
    st.header("Hasil Analisis")

    # ANALISIS OTOMATIS
    root, causal = analyze_piom()

    st.subheader("🧠 Analisis Inti")
    st.success(root)

    st.subheader("🔗 Rantai Kausal")
    st.write(causal)

    st.subheader("🎯 Prioritas Intervensi")

    if "insentif" in root:
        st.write("1. Reformasi sistem insentif (penilaian, reward)")
    if "biaya" in root:
        st.write("2. Turunkan biaya transaksi (akses, kemampuan)")
    st.write("3. Perkuat institusi & budaya akademik")

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
