import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="SPK Smartwatch | AHP",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
            
@import url('https://fonts.googleapis.com/css2?family=Lora:wght@500;600;700&family=DM+Sans:ital,wght@0,300;0,400;0,500;0,600;1,300&family=DM+Mono:wght@400;500&display=swap');

/* ====== VARIABLES ====== */
:root {
    --bg:           #1C1A17;
    --surface:      #252220;
    --surface-2:    #2E2B27;
    --surface-3:    #363129;
    --border:       #3A3630;
    --border-light: #4A4540;

    --text-1: #EDE8E0;
    --text-2: #B8B0A4;
    --text-3: #7A7268;

    --sage:         #4E7A3A;
    --sage-mid:     #6A9E52;
    --sage-light:   #A8C990;
    --sage-pale:    #2A3D22;
    --sage-border:  #3D5E2E;

    --amber:        #B8860B;
    --amber-light:  #D4A832;
    --amber-pale:   #332500;
    --amber-border: #5C4000;

    --rust:         #8B3A1E;
    --rust-light:   #C45A30;
    --rust-pale:    #2E1510;
    --rust-border:  #5C2810;

    --sidebar-bg:   #141210;
}

/* ====== GLOBAL ====== */
html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    background-color: var(--bg) !important;
    color: var(--text-1);
}
.stApp { background-color: var(--bg) !important; }
.main  { background-color: var(--bg) !important; }
.block-container {
    padding-top: 1.4rem !important;
    padding-bottom: 2.5rem !important;
    max-width: 1380px;
    background-color: var(--bg) !important;
}

/* ====== SIDEBAR ====== */
section[data-testid="stSidebar"] {
    background: var(--sidebar-bg) !important;
    border-right: 1px solid var(--border) !important;
}
section[data-testid="stSidebar"] * {
    color: var(--text-2) !important;
    font-family: 'DM Sans', sans-serif !important;
}
section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3 {
    color: var(--text-1) !important;
    font-family: 'Lora', serif !important;
}
section[data-testid="stSidebar"] label {
    color: var(--text-3) !important;
    font-size: 0.75rem !important;
    font-weight: 500 !important;
    letter-spacing: 0.08em !important;
    text-transform: uppercase !important;
}
section[data-testid="stSidebar"] [data-testid="stMetricValue"] {
    color: var(--sage-light) !important;
    font-family: 'DM Mono', monospace !important;
    font-size: 1.35rem !important;
}
section[data-testid="stSidebar"] [data-testid="stMetricLabel"] {
    color: var(--text-3) !important;
    font-size: 0.7rem !important;
    text-transform: uppercase;
    letter-spacing: 0.06em;
}
section[data-testid="stSidebar"] hr {
    border-color: var(--border) !important;
    margin: 0.8rem 0;
}
section[data-testid="stSidebar"] .stCheckbox label {
    text-transform: none !important;
    letter-spacing: 0 !important;
    font-size: 0.85rem !important;
    color: var(--text-2) !important;
}
section[data-testid="stSidebar"] [data-testid="stMetricContainer"] {
    background: var(--surface) !important;
    border: 1px solid var(--border) !important;
    border-top: 2px solid var(--sage) !important;
    border-radius: 3px !important;
    padding: 0.7rem 0.9rem !important;
}

/* ====== HEADER ====== */
.app-header {
    background: var(--sidebar-bg);
    border: 1px solid var(--border);
    border-bottom: 3px solid var(--sage);
    border-radius: 3px;
    padding: 1.8rem 2.2rem;
    margin-bottom: 1.4rem;
}
.app-header-label {
    font-size: 0.65rem;
    font-weight: 600;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: var(--sage-light);
    margin-bottom: 0.5rem;
}
.app-header h1 {
    color: var(--text-1) !important;
    margin: 0 0 0.4rem;
    font-family: 'Lora', serif !important;
    font-size: 1.75rem;
    font-weight: 700;
    line-height: 1.2;
}
.app-header p {
    color: var(--text-3);
    margin: 0;
    font-size: 0.86rem;
    font-weight: 300;
    letter-spacing: 0.01em;
}

/* ====== METRIC CARDS ====== */
[data-testid="metric-container"] {
    background: var(--surface) !important;
    border: 1px solid var(--border) !important;
    border-top: 3px solid var(--sage) !important;
    border-radius: 3px !important;
    padding: 0.9rem 1.1rem !important;
}
[data-testid="stMetricValue"] {
    color: var(--text-1) !important;
    font-family: 'DM Mono', monospace !important;
    font-weight: 500 !important;
    font-size: 1.4rem !important;
}
[data-testid="stMetricLabel"] {
    color: var(--text-3) !important;
    font-size: 0.69rem !important;
    text-transform: uppercase !important;
    letter-spacing: 0.08em !important;
    font-weight: 500 !important;
}

/* ====== TABS ====== */
.stTabs [data-baseweb="tab-list"] {
    gap: 0;
    background: transparent;
    border-bottom: 1px solid var(--border);
    border-radius: 0;
    padding: 0;
    margin-bottom: 1.4rem;
}
.stTabs [data-baseweb="tab"] {
    border-radius: 0;
    font-weight: 500;
    font-size: 0.78rem;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    padding: 0.65rem 1.3rem;
    color: var(--text-3) !important;
    background: transparent !important;
    border-bottom: 2px solid transparent;
    margin-bottom: -1px;
}
.stTabs [aria-selected="true"] {
    background: transparent !important;
    color: var(--sage-light) !important;
    border-bottom: 2px solid var(--sage-mid) !important;
    font-weight: 600 !important;
}

/* ====== STEP / FORMULA CARDS ====== */
.step-card {
    background: var(--surface-2);
    border: 1px solid var(--border);
    border-left: 3px solid var(--sage);
    border-radius: 2px;
    padding: 0.85rem 1.1rem;
    margin: 0.6rem 0;
    font-size: 0.84rem;
    line-height: 1.75;
    color: var(--text-2);
}
.formula-card {
    background: var(--amber-pale);
    border: 1px solid var(--amber-border);
    border-radius: 2px;
    padding: 0.9rem 1.2rem;
    font-family: 'DM Mono', monospace;
    font-size: 0.81rem;
    line-height: 1.85;
    margin: 0.6rem 0;
    color: var(--text-2);
}
.formula-card b { color: var(--amber-light); }

/* ====== CR BANNERS ====== */
.cr-banner {
    border-radius: 3px;
    padding: 1.2rem 1.5rem;
    margin: 0.8rem 0;
}
.cr-ok   {
    background: var(--sage-pale);
    border: 1px solid var(--sage-border);
    border-left: 4px solid var(--sage-mid);
}
.cr-fail {
    background: var(--rust-pale);
    border: 1px solid var(--rust-border);
    border-left: 4px solid var(--rust-light);
}
.cr-status-label {
    font-size: 0.62rem;
    font-weight: 600;
    letter-spacing: 0.16em;
    text-transform: uppercase;
    margin-bottom: 0.25rem;
}
.cr-ok   .cr-status-label { color: var(--sage-light); }
.cr-fail .cr-status-label { color: var(--rust-light); }
.cr-banner h4 { margin: 0 0 0.35rem; font-size: 0.95rem; font-weight: 600; }
.cr-ok   h4 { color: var(--sage-light); }
.cr-fail h4 { color: var(--rust-light); }
.cr-banner p { margin: 0; font-size: 0.84rem; color: var(--text-2); line-height: 1.6; }

/* ====== WINNER CARDS ====== */
.winner-grid { display: grid; grid-template-columns: repeat(3,1fr); gap: 1rem; margin: 0.8rem 0; }
.winner-card {
    border-radius: 3px;
    padding: 1.3rem 1.4rem;
    text-align: center;
    position: relative;
}
.winner-gold   { background: var(--amber-pale);  border: 1px solid var(--amber-border); border-top: 3px solid var(--amber-light); }
.winner-silver { background: var(--surface-2);   border: 1px solid var(--border-light); border-top: 3px solid var(--text-3); }
.winner-bronze { background: var(--rust-pale);   border: 1px solid var(--rust-border);  border-top: 3px solid var(--rust-light); }
.winner-place-label {
    font-size: 0.6rem;
    font-weight: 600;
    letter-spacing: 0.16em;
    text-transform: uppercase;
    margin-bottom: 0.5rem;
}
.winner-gold   .winner-place-label { color: var(--amber-light); }
.winner-silver .winner-place-label { color: var(--text-3); }
.winner-bronze .winner-place-label { color: var(--rust-light); }
.winner-card .name  {
    font-family: 'Lora', serif;
    font-weight: 600;
    font-size: 0.98rem;
    color: var(--text-1);
    margin: 0.2rem 0;
    line-height: 1.3;
}
.winner-card .score {
    font-family: 'DM Mono', monospace;
    font-size: 0.78rem;
    color: var(--text-3);
    margin-top: 0.45rem;
}

/* ====== SIDEBAR INFO BOX ====== */
.sidebar-info {
    background: rgba(78,122,58,0.06);
    border: 1px solid var(--sage-border);
    border-left: 2px solid var(--sage);
    border-radius: 2px;
    padding: 0.7rem 0.9rem;
    margin: 0.5rem 0;
    font-size: 0.79rem;
    color: var(--text-3);
    line-height: 1.65;
}
.sidebar-info b { color: var(--text-2); }

/* ====== DIVIDER ====== */
.divider {
    height: 1px;
    background: var(--border);
    margin: 1.4rem 0;
}

/* ====== DATAFRAME ====== */
.stDataFrame {
    border-radius: 2px !important;
    border: 1px solid var(--border) !important;
    overflow: hidden;
}
/* Dark table headers */
[data-testid="stDataFrame"] th {
    background: var(--surface-3) !important;
    color: var(--text-3) !important;
    font-size: 0.72rem !important;
    letter-spacing: 0.07em !important;
    text-transform: uppercase !important;
    border-bottom: 1px solid var(--border) !important;
}
[data-testid="stDataFrame"] td {
    background: var(--surface) !important;
    color: var(--text-2) !important;
    border-bottom: 1px solid var(--border) !important;
    font-size: 0.85rem !important;
}
[data-testid="stDataFrame"] tr:hover td {
    background: var(--surface-2) !important;
}

/* ====== BUTTONS ====== */
.stButton > button {
    background: var(--sage) !important;
    color: var(--text-1) !important;
    border: none !important;
    border-radius: 2px !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 0.8rem !important;
    font-weight: 600 !important;
    letter-spacing: 0.06em !important;
    text-transform: uppercase !important;
    padding: 0.5rem 1.2rem !important;
    transition: background 0.15s;
}
.stButton > button:hover {
    background: var(--sage-mid) !important;
}

/* ====== FORM / INPUT ====== */
.stTextInput input,
.stNumberInput input {
    background: var(--surface-2) !important;
    border: 1px solid var(--border-light) !important;
    border-radius: 2px !important;
    color: var(--text-1) !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 0.88rem !important;
}
.stSelectbox > div > div {
    background: var(--surface-2) !important;
    border: 1px solid var(--border-light) !important;
    border-radius: 2px !important;
    color: var(--text-1) !important;
}
.stMultiSelect > div > div {
    background: var(--surface-2) !important;
    border: 1px solid var(--border-light) !important;
    border-radius: 2px !important;
}

/* ====== EXPANDER ====== */
.streamlit-expanderHeader {
    background: var(--surface-2) !important;
    border: 1px solid var(--border) !important;
    border-radius: 2px !important;
    color: var(--text-2) !important;
    font-size: 0.83rem !important;
    font-weight: 600 !important;
    letter-spacing: 0.04em !important;
}
.streamlit-expanderContent {
    background: var(--surface) !important;
    border: 1px solid var(--border) !important;
    border-top: none !important;
}

/* ====== ALERTS ====== */
.stWarning > div {
    background: var(--amber-pale) !important;
    border: 1px solid var(--amber-border) !important;
    border-left: 3px solid var(--amber-light) !important;
    color: var(--text-2) !important;
    border-radius: 2px !important;
}
.stInfo > div {
    background: var(--sage-pale) !important;
    border: 1px solid var(--sage-border) !important;
    border-left: 3px solid var(--sage-mid) !important;
    color: var(--text-2) !important;
    border-radius: 2px !important;
}
.stSuccess > div {
    background: var(--sage-pale) !important;
    border: 1px solid var(--sage-border) !important;
    border-left: 3px solid var(--sage-mid) !important;
    color: var(--text-2) !important;
    border-radius: 2px !important;
}
.stError > div {
    background: var(--rust-pale) !important;
    border: 1px solid var(--rust-border) !important;
    border-left: 3px solid var(--rust-light) !important;
    color: var(--text-2) !important;
    border-radius: 2px !important;
}

/* ====== RADIO ====== */
.stRadio > div { gap: 0.5rem; }
.stRadio label { font-size: 0.85rem !important; color: var(--text-2) !important; }

/* ====== SLIDER ====== */
[data-baseweb="slider"] [role="slider"] { background: var(--sage-mid) !important; }

/* ====== TYPOGRAPHY ====== */
h1, h2, h3, h4 {
    font-family: 'Lora', serif !important;
    color: var(--text-1) !important;
    letter-spacing: -0.01em;
}
h3 { font-size: 1.05rem !important; margin-bottom: 1rem; }
h4 { font-size: 0.92rem !important; margin-bottom: 0.7rem; }
p, span, li { font-family: 'DM Sans', sans-serif; color: var(--text-2); }
.stCaption, small { color: var(--text-3) !important; font-size: 0.76rem !important; }
</style>
""", unsafe_allow_html=True)

# ==========================================
# SESSION STATE & DATA
# ==========================================
@st.cache_data
def load_default_data():
    try:
        df = pd.read_csv("Smart_watch_prices.csv")
    except FileNotFoundError:
        data = {
            'Brand':  ['Apple','Samsung','Garmin','Fitbit','Huawei','Apple','Samsung','Fossil','Xiaomi','Polar'],
            'Model':  ['Watch Series 9','Galaxy Watch 6','Forerunner 255','Versa 4','GT 3 Pro',
                       'Watch SE 2','Galaxy Watch 5','Gen 6','Mi Band 8','Vantage V3'],
            'Price (USD)': [399,299,349,229,249,249,279,295,49,599],
            'Battery Life (days)': [1.5,3,14,6,14,2,4,1,14,40],
            'Water Resistance (meters)': [50,50,50,50,100,50,50,30,50,100],
            'Heart Rate Monitor': ['Yes','Yes','Yes','Yes','Yes','Yes','Yes','Yes','Yes','Yes'],
            'GPS': ['Yes','Yes','Yes','Yes','Yes','No','Yes','No','No','Yes'],
            'Display Size (mm)': [45,44,46,40,46,40,44,44,np.nan,47],
            'OS Compatibility': ['iOS/Android','Android','iOS/Android','iOS/Android','Android',
                                 'iOS/Android','Android','iOS/Android','Android','iOS/Android'],
        }
        return pd.DataFrame(data)
    return df

def preprocess(df):
    dc = df.copy()
    if 'Price (USD)' in dc.columns:
        dc['Price (USD)'] = pd.to_numeric(
            dc['Price (USD)'].astype(str)
              .str.replace('$','',regex=False).str.replace(',','',regex=False).str.strip(),
            errors='coerce')
    for col in ['Water Resistance (meters)','Battery Life (days)']:
        if col in dc.columns:
            dc[col] = pd.to_numeric(dc[col], errors='coerce').fillna(0)
    for col in ['Heart Rate Monitor','GPS']:
        if col in dc.columns:
            dc[col] = dc[col].astype(str).str.strip().str.lower().apply(lambda x: 1 if x=='yes' else 0)
    kriteria = ['Price (USD)','Battery Life (days)','Water Resistance (meters)','Heart Rate Monitor','GPS']
    dc = dc.dropna(subset=[c for c in kriteria if c in dc.columns])
    return dc.reset_index(drop=True)

if 'df_master' not in st.session_state:
    st.session_state['df_master'] = preprocess(load_default_data())
if 'crud_msg' not in st.session_state:
    st.session_state['crud_msg'] = None

df_master = st.session_state['df_master']

# ==========================================
# SIDEBAR
# ==========================================
with st.sidebar:
    st.markdown("### Panel Kontrol")
    st.markdown("---")

    st.markdown("#### Filter Produk")
    max_price   = st.number_input("Maks. Harga (USD)", min_value=10, value=1000, step=50)
    min_battery = st.number_input("Min. Baterai (Hari)", min_value=0.0, value=0.0, step=1.0)
    brand_opts  = sorted(df_master['Brand'].dropna().unique()) if len(df_master) > 0 else []
    sel_brands  = st.multiselect("Brand", options=brand_opts, placeholder="Semua brand")
    has_hrm     = st.checkbox("Wajib Heart Rate Monitor")
    has_gps     = st.checkbox("Wajib GPS")

    df_filtered = df_master.copy()
    if sel_brands:
        df_filtered = df_filtered[df_filtered['Brand'].isin(sel_brands)]
    df_filtered = df_filtered[df_filtered['Price (USD)'] <= max_price]
    df_filtered = df_filtered[df_filtered['Battery Life (days)'] >= min_battery]
    if has_hrm:
        df_filtered = df_filtered[df_filtered['Heart Rate Monitor'] == 1]
    if has_gps:
        df_filtered = df_filtered[df_filtered['GPS'] == 1]

    st.markdown("---")
    st.markdown("#### Ringkasan")
    c1, c2 = st.columns(2)
    c1.metric("Produk", len(df_filtered))
    c2.metric("Total DB", len(df_master))
    if len(df_filtered) > 0:
        st.metric("Harga Rata-rata", f"${df_filtered['Price (USD)'].mean():.0f}")
        pct_hrm = df_filtered['Heart Rate Monitor'].mean() * 100
        pct_gps = df_filtered['GPS'].mean() * 100
        st.markdown(f"""<div class="sidebar-info">
        HRM tersedia: <b>{pct_hrm:.0f}%</b> produk<br>
        GPS tersedia: <b>{pct_gps:.0f}%</b> produk
        </div>""", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("#### Tentang AHP")
    st.markdown("""<div class="sidebar-info">
    <b>Analytical Hierarchy Process</b> (Saaty, 1980) adalah metode pengambilan keputusan multi-kriteria
    melalui perbandingan berpasangan antar kriteria.<br><br>
    <b>Syarat konsistensi:</b> CR tidak boleh melebihi 0.10
    </div>""", unsafe_allow_html=True)

# ==========================================
# HEADER
# ==========================================
st.markdown("""
<div class="app-header">
  <div class="app-header-label">Sistem Pendukung Keputusan</div>
  <h1>Pemilihan Smartwatch</h1>
  <p>Metode Analytical Hierarchy Process (AHP) &mdash; Pembobotan kriteria dan perankingan alternatif produk smartwatch</p>
</div>
""", unsafe_allow_html=True)

# ==========================================
# TABS
# ==========================================
tab1, tab_crud, tab_ahp, tab_hasil = st.tabs([
    "Eksplorasi Data",
    "Manajemen Data",
    "Pembobotan AHP",
    "Hasil Rekomendasi",
])

# ============================================================
# TAB 1 — EKSPLORASI DATA
# ============================================================
with tab1:
    if len(df_filtered) == 0:
        st.info("Tidak ada produk yang sesuai filter. Ubah pengaturan di sidebar.")
    else:
        c1, c2, c3, c4, c5 = st.columns(5)
        c1.metric("Total Produk",    f"{len(df_filtered)}")
        c2.metric("Harga Terendah",  f"${df_filtered['Price (USD)'].min():.0f}")
        c3.metric("Harga Tertinggi", f"${df_filtered['Price (USD)'].max():.0f}")
        c4.metric("Baterai Terlama", f"{df_filtered['Battery Life (days)'].max():.0f} hr")
        c5.metric("Rata-rata Harga", f"${df_filtered['Price (USD)'].mean():.0f}")

        st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

        col_tbl, col_charts = st.columns([3, 2], gap="large")
        with col_tbl:
            st.markdown("#### Daftar Produk")
            dd = df_filtered.copy()
            dd['Heart Rate Monitor'] = dd['Heart Rate Monitor'].map({1:'Ya', 0:'Tidak'})
            dd['GPS']                = dd['GPS'].map({1:'Ya', 0:'Tidak'})
            show = [c for c in ['Brand','Model','Price (USD)','Battery Life (days)',
                                 'Water Resistance (meters)','Heart Rate Monitor','GPS'] if c in dd.columns]
            st.dataframe(dd[show].reset_index(drop=True), use_container_width=True, hide_index=True,
                column_config={
                    "Price (USD)":               st.column_config.NumberColumn("Harga (USD)", format="$%.2f"),
                    "Battery Life (days)":       st.column_config.NumberColumn("Baterai (Hari)", format="%.1f"),
                    "Water Resistance (meters)": st.column_config.NumberColumn("Tahan Air (m)", format="%d m"),
                })

        with col_charts:
            st.markdown("#### Distribusi Harga per Brand")
            st.bar_chart(df_filtered.groupby('Brand')['Price (USD)'].mean().sort_values(ascending=False),
                         use_container_width=True, color="#4E7A3A")
            st.markdown("#### Rata-rata Baterai per Brand")
            st.bar_chart(df_filtered.groupby('Brand')['Battery Life (days)'].mean().sort_values(ascending=False),
                         use_container_width=True, color="#B8860B")

        st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
        st.markdown("#### Statistik Deskriptif")
        stat_cols = [c for c in ['Price (USD)','Battery Life (days)','Water Resistance (meters)']
                     if c in df_filtered.columns]
        st.dataframe(df_filtered[stat_cols].describe().round(2), use_container_width=True)

# ============================================================
# TAB CRUD
# ============================================================
with tab_crud:
    if st.session_state['crud_msg']:
        mtype, mtxt = st.session_state['crud_msg']
        if mtype == 'success': st.success(mtxt)
        else:                  st.error(mtxt)
        st.session_state['crud_msg'] = None

    st.markdown("#### Pilih Operasi")
    aksi = st.radio("", ["Tambah", "Lihat Semua", "Edit", "Hapus"],
                    horizontal=True, label_visibility="collapsed")
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    if aksi == "Tambah":
        st.markdown("#### Tambah Produk Baru")
        with st.form("frm_tambah", clear_on_submit=True):
            st.markdown("**Informasi Dasar**")
            r1, r2, r3 = st.columns(3)
            brand_n = r1.text_input("Brand", placeholder="cth: Apple")
            model_n = r2.text_input("Model", placeholder="cth: Watch Series 9")
            harga_n = r3.number_input("Harga (USD)", min_value=1.0, value=299.0, step=10.0)
            st.markdown("**Spesifikasi Teknis**")
            s1, s2, s3, s4, s5 = st.columns(5)
            bat_n  = s1.number_input("Baterai (Hari)", min_value=0.1, value=3.0, step=0.5)
            air_n  = s2.number_input("Tahan Air (m)",  min_value=0, value=50, step=10)
            hrm_n  = s3.selectbox("Heart Rate Monitor", ["Yes","No"])
            gps_n  = s4.selectbox("GPS", ["Yes","No"])
            disp_n = s5.number_input("Layar (mm)", min_value=0.0, value=44.0, step=1.0)
            os_n   = st.selectbox("Kompatibilitas OS", ["iOS/Android","Android","iOS"])
            if st.form_submit_button("Simpan Produk", use_container_width=True, type="primary"):
                if not brand_n.strip() or not model_n.strip():
                    st.session_state['crud_msg'] = ('error', 'Brand dan Model tidak boleh kosong.')
                    st.rerun()
                else:
                    baru = {c: np.nan for c in df_master.columns}
                    baru.update({'Brand': brand_n.strip(), 'Model': model_n.strip(),
                                 'Price (USD)': float(harga_n), 'Battery Life (days)': float(bat_n),
                                 'Water Resistance (meters)': int(air_n),
                                 'Heart Rate Monitor': 1 if hrm_n=='Yes' else 0,
                                 'GPS': 1 if gps_n=='Yes' else 0})
                    if 'Display Size (mm)' in df_master.columns: baru['Display Size (mm)'] = float(disp_n)
                    if 'OS Compatibility'  in df_master.columns: baru['OS Compatibility']  = os_n
                    st.session_state['df_master'] = pd.concat(
                        [df_master, pd.DataFrame([baru])], ignore_index=True)
                    st.session_state['crud_msg'] = ('success', f"'{brand_n} {model_n}' berhasil ditambahkan.")
                    st.rerun()

    elif aksi == "Lihat Semua":
        st.markdown("#### Semua Data Tersimpan")
        if len(df_master) == 0:
            st.info("Belum ada data.")
        else:
            dv = df_master.copy().reset_index().rename(columns={"index":"ID"})
            dv['Heart Rate Monitor'] = dv['Heart Rate Monitor'].map({1:'Ya', 0:'Tidak'})
            dv['GPS']                = dv['GPS'].map({1:'Ya', 0:'Tidak'})
            st.dataframe(dv, use_container_width=True, hide_index=True,
                column_config={"Price (USD)": st.column_config.NumberColumn("Harga (USD)", format="$%.2f"),
                               "Battery Life (days)": st.column_config.NumberColumn("Baterai (Hari)", format="%.1f")})
            st.caption(f"Total {len(df_master)} produk tersimpan.")

    elif aksi == "Edit":
        st.markdown("#### Edit Data Produk")
        if len(df_master) == 0:
            st.info("Belum ada data.")
        else:
            dr   = df_master.reset_index(drop=True)
            opts = [f"[{i}]  {r['Brand']} {r['Model']}  —  ${r['Price (USD)']:.2f}" for i, r in dr.iterrows()]
            sel  = st.selectbox("Pilih produk:", opts)
            idx  = int(sel.split("]")[0].replace("[","").strip())
            row  = dr.iloc[idx]
            st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
            with st.form("frm_edit"):
                st.markdown("**Informasi Dasar**")
                e1, e2, e3 = st.columns(3)
                b_e = e1.text_input("Brand",     value=str(row.get('Brand','')))
                m_e = e2.text_input("Model",     value=str(row.get('Model','')))
                h_e = e3.number_input("Harga",   min_value=1.0, value=float(row.get('Price (USD)',0)), step=10.0)
                st.markdown("**Spesifikasi Teknis**")
                t1, t2, t3, t4 = st.columns(4)
                ba_e = t1.number_input("Baterai (Hari)", min_value=0.1, value=float(row.get('Battery Life (days)',1)), step=0.5)
                ai_e = t2.number_input("Tahan Air (m)",  min_value=0,   value=int(row.get('Water Resistance (meters)',0)), step=10)
                hr_e = t3.selectbox("HRM", ["Yes","No"], index=0 if row.get('Heart Rate Monitor',0)==1 else 1)
                gp_e = t4.selectbox("GPS", ["Yes","No"], index=0 if row.get('GPS',0)==1 else 1)
                if st.form_submit_button("Simpan Perubahan", use_container_width=True, type="primary"):
                    dm = st.session_state['df_master']
                    for col, val in {'Brand': b_e.strip(), 'Model': m_e.strip(),
                                     'Price (USD)': float(h_e), 'Battery Life (days)': float(ba_e),
                                     'Water Resistance (meters)': int(ai_e),
                                     'Heart Rate Monitor': 1 if hr_e=='Yes' else 0,
                                     'GPS': 1 if gp_e=='Yes' else 0}.items():
                        if col in dm.columns:
                            dm.iloc[idx, dm.columns.get_loc(col)] = val
                    st.session_state['df_master'] = dm
                    st.session_state['crud_msg'] = ('success', f"'{b_e} {m_e}' berhasil diperbarui.")
                    st.rerun()

    elif aksi == "Hapus":
        st.markdown("#### Hapus Produk")
        if len(df_master) == 0:
            st.info("Tidak ada data untuk dihapus.")
        else:
            dr   = df_master.reset_index(drop=True)
            opts = [f"[{i}]  {r['Brand']} {r['Model']}  —  ${r['Price (USD)']:.2f}" for i, r in dr.iterrows()]
            sel  = st.selectbox("Pilih produk:", opts)
            idx  = int(sel.split("]")[0].replace("[","").strip())
            row  = dr.iloc[idx]
            st.warning(f"Anda akan menghapus: **{row['Brand']} {row['Model']}** — ${row['Price (USD)']:.2f}")
            col_del, _ = st.columns([1, 4])
            with col_del:
                if st.button("Konfirmasi Hapus", type="primary", use_container_width=True):
                    nama = f"{row['Brand']} {row['Model']}"
                    st.session_state['df_master'] = dr.drop(index=idx).reset_index(drop=True)
                    st.session_state['crud_msg'] = ('success', f"'{nama}' berhasil dihapus.")
                    st.rerun()

# ============================================================
# TAB AHP
# ============================================================
with tab_ahp:
    kriteria_list = ["Harga", "Baterai", "Ketahanan Air", "Detak Jantung", "GPS"]
    n = len(kriteria_list)
    M = np.ones((n, n))

    pasangan = [
        (0,1,"Harga","Baterai"),         (0,2,"Harga","Ketahanan Air"),
        (0,3,"Harga","Detak Jantung"),   (0,4,"Harga","GPS"),
        (1,2,"Baterai","Ketahanan Air"), (1,3,"Baterai","Detak Jantung"),
        (1,4,"Baterai","GPS"),           (2,3,"Ketahanan Air","Detak Jantung"),
        (2,4,"Ketahanan Air","GPS"),     (3,4,"Detak Jantung","GPS"),
    ]

    with st.expander("Panduan Skala Saaty", expanded=False):
        st.dataframe(pd.DataFrame({
            "Nilai": [1,2,3,4,5,6,7,8,9],
            "Definisi": ["Sama penting","Antara sama dan sedikit lebih penting",
                         "Sedikit lebih penting","Antara sedikit dan cukup penting",
                         "Cukup lebih penting","Antara cukup dan sangat penting",
                         "Sangat lebih penting","Antara sangat dan mutlak penting",
                         "Mutlak/Ekstrim lebih penting"],
        }), use_container_width=True, hide_index=True)

    st.markdown("#### Perbandingan Berpasangan Antar Kriteria")
    st.caption("Geser ke kiri jika kriteria pertama lebih penting, ke kanan jika kriteria kedua lebih penting.")

    pw_cols = st.columns(2)
    for idx_p, (i, j, c1, c2) in enumerate(pasangan):
        with pw_cols[idx_p % 2]:
            lc, rc = st.columns([2, 1])
            lc.markdown(
                f"<span style='font-size:0.85rem;font-weight:600;color:var(--text-1)'>{c1}</span>"
                f"<span style='color:var(--text-3);font-size:0.8rem'> vs </span>"
                f"<span style='font-size:0.85rem;font-weight:600;color:var(--text-1)'>{c2}</span>",
                unsafe_allow_html=True)
            val = st.slider("", min_value=-8, max_value=8, value=0,
                            key=f"s_{i}_{j}", label_visibility="collapsed")
            if val < 0:
                sk = abs(val)+1; M[i][j] = sk; M[j][i] = 1/sk
                rc.markdown(f"<span style='color:var(--sage-light);font-size:0.76rem;font-weight:600'>{c1} ×{sk}</span>", unsafe_allow_html=True)
            elif val > 0:
                sk = val+1; M[i][j] = 1/sk; M[j][i] = sk
                rc.markdown(f"<span style='color:var(--sage-light);font-size:0.76rem;font-weight:600'>{c2} ×{sk}</span>", unsafe_allow_html=True)
            else:
                rc.markdown("<span style='color:var(--text-3);font-size:0.76rem'>Setara</span>", unsafe_allow_html=True)

    # AHP calc
    kolom_sum   = M.sum(axis=0)
    M_norm      = M / kolom_sum
    bobot_akhir = M_norm.mean(axis=1)
    vt          = M @ bobot_akhir
    rasio_lam   = vt / bobot_akhir
    lambda_max  = rasio_lam.mean()
    ci  = (lambda_max - n) / (n - 1)
    ri_tbl = {1:0.00,2:0.00,3:0.58,4:0.90,5:1.12,6:1.24,7:1.32,8:1.41,9:1.45,10:1.49}
    ri  = ri_tbl.get(n, 1.12)
    cr  = ci / ri if ri != 0 else 0.0

    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    st.markdown("### Detail Perhitungan AHP")

    with st.expander("Langkah 1 — Matriks Perbandingan Berpasangan (A)", expanded=True):
        st.markdown('<p>Matriks simetris resiprokal: diagonal = 1, elemen A[j,i] = 1/A[i,j].</p>', unsafe_allow_html=True)
        df_M = pd.DataFrame(M, index=kriteria_list, columns=kriteria_list)
        st.dataframe(df_M.style.format("{:.4f}").background_gradient(cmap='YlGn', axis=None),
                     use_container_width=True)
        st.markdown('<div class="step-card">Sifat resiprokal: jika A lebih penting dari B dengan skala 3, maka B terhadap A = 1/3 = 0.333</div>', unsafe_allow_html=True)

    with st.expander("Langkah 2 — Normalisasi dan Bobot Prioritas", expanded=True):
        l2a, l2b = st.columns([3, 2], gap="large")
        with l2a:
            st.markdown("**Jumlah Tiap Kolom**")
            st.dataframe(pd.DataFrame([kolom_sum], columns=kriteria_list, index=["Jumlah Kolom"]).style.format("{:.4f}"),
                         use_container_width=True)
            st.markdown("**Matriks Ternormalisasi** *(elemen dibagi jumlah kolom)*")
            st.dataframe(pd.DataFrame(M_norm, index=kriteria_list, columns=kriteria_list).style.format("{:.4f}").background_gradient(cmap='YlGn', axis=None),
                         use_container_width=True)
        with l2b:
            st.markdown("**Bobot Prioritas** *(rata-rata baris)*")
            df_w = pd.DataFrame({"Kriteria": kriteria_list,
                                 "Bobot": np.round(bobot_akhir,6),
                                 "Bobot (%)": np.round(bobot_akhir*100,3)}).sort_values("Bobot (%)", ascending=False)
            st.dataframe(df_w, use_container_width=True, hide_index=True,
                column_config={"Bobot (%)": st.column_config.ProgressColumn(
                    "Bobot (%)", min_value=0, max_value=100, format="%.2f%%")})
            st.markdown('<div class="formula-card">Jumlah Bobot = <b>{:.6f}</b> &asymp; 1.000</div>'.format(bobot_akhir.sum()), unsafe_allow_html=True)
            st.bar_chart(pd.DataFrame({"Bobot (%)": bobot_akhir*100}, index=kriteria_list),
                         use_container_width=True, color="#4E7A3A")

    with st.expander("Langkah 3 — Perhitungan Lambda Maksimum", expanded=True):
        st.dataframe(pd.DataFrame({
            "Kriteria": kriteria_list,
            "Vektor Tertimbang (Aw)": np.round(vt,6),
            "Bobot (w)": np.round(bobot_akhir,6),
            "Rasio (Aw/w)": np.round(rasio_lam,6),
        }), use_container_width=True, hide_index=True)
        st.markdown(f"""<div class="formula-card">
        lambda_max = ({" + ".join([f"{r:.4f}" for r in rasio_lam])}) / {n}<br>
        lambda_max = {rasio_lam.sum():.6f} / {n}<br>
        lambda_max = <b>{lambda_max:.6f}</b>
        </div>""", unsafe_allow_html=True)
        st.markdown('<div class="step-card">Semakin dekat lambda_max dengan n, semakin konsisten matriks. Jika lambda_max = n, maka konsistensi sempurna.</div>', unsafe_allow_html=True)

    with st.expander("Langkah 4 — CI, RI, dan CR", expanded=True):
        st.markdown("**Tabel Random Index (RI) — Saaty, 1980**")
        ri_html = "<div style='display:flex;gap:5px;flex-wrap:wrap;margin:0.5rem 0 1rem'>"
        for ni, riv in ri_tbl.items():
            active = ni == n
            bg  = "var(--sage)"       if active else "var(--surface-3)"
            fc  = "var(--text-1)"     if active else "var(--text-3)"
            brd = "var(--sage-mid)"   if active else "var(--border)"
            ri_html += (f"<div style='background:{bg};color:{fc};border:1px solid {brd};"
                        f"border-radius:2px;padding:0.35rem 0.7rem;font-family:DM Mono,monospace;"
                        f"font-size:0.78rem;font-weight:600;text-align:center;min-width:52px'>"
                        f"n={ni}<br>{riv}</div>")
        ri_html += "</div>"
        st.markdown(ri_html, unsafe_allow_html=True)
        st.caption(f"Kotak terang = nilai yang digunakan: n = {n}, RI = {ri}")

        st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
        col_ci, col_ri, col_cr = st.columns(3)
        with col_ci:
            st.markdown("##### Consistency Index (CI)")
            st.markdown(f"""<div class="formula-card">
            CI = (lambda_max &minus; n) / (n &minus; 1)<br>
            CI = ({lambda_max:.4f} &minus; {n}) / ({n} &minus; 1)<br>
            CI = {lambda_max-n:.6f} / {n-1}<br>
            CI = <b>{ci:.6f}</b>
            </div>""", unsafe_allow_html=True)
            st.info("CI = 0 artinya matriks sempurna konsisten.")
        with col_ri:
            st.markdown("##### Random Index (RI)")
            st.markdown(f"""<div class="formula-card">
            n = {n} kriteria<br>
            Lookup tabel Saaty:<br>
            RI = <b>{ri}</b>
            </div>""", unsafe_allow_html=True)
            st.info("RI = rata-rata CI dari 500 matriks acak berukuran n&times;n.")
        with col_cr:
            st.markdown("##### Consistency Ratio (CR)")
            st.markdown(f"""<div class="formula-card">
            CR = CI / RI<br>
            CR = {ci:.6f} / {ri}<br>
            CR = <b>{cr:.6f}</b> ({cr*100:.2f}%)
            </div>""", unsafe_allow_html=True)

        st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
        st.markdown("##### Status Konsistensi")
        if cr <= 0.10:
            st.markdown(f"""<div class="cr-banner cr-ok">
              <div class="cr-status-label">Status</div>
              <h4>Konsisten &mdash; CR = {cr:.4f} ({cr*100:.2f}%) tidak melebihi 10%</h4>
              <p>Preferensi penilaian Anda logis dan konsisten. Bobot kriteria ini dapat digunakan secara sah dalam pengambilan keputusan AHP.</p>
            </div>""", unsafe_allow_html=True)
        else:
            st.markdown(f"""<div class="cr-banner cr-fail">
              <div class="cr-status-label">Status</div>
              <h4>Tidak Konsisten &mdash; CR = {cr:.4f} ({cr*100:.2f}%) melebihi 10%</h4>
              <p>Terdapat kontradiksi logis dalam penilaian Anda. Tinjau kembali slider perbandingan dan pastikan preferensi konsisten satu sama lain.</p>
            </div>""", unsafe_allow_html=True)

        st.markdown("""<div class="step-card">
        <b>Panduan Interpretasi CR:</b><br>
        &nbsp;&nbsp;CR = 0.00 &mdash; Konsistensi sempurna (ideal, jarang terjadi)<br>
        &nbsp;&nbsp;CR &le; 0.10 &mdash; Dapat diterima, hasil dapat dipercaya<br>
        &nbsp;&nbsp;CR &gt; 0.10 &mdash; Tidak konsisten, perlu revisi penilaian<br><br>
        <i>Contoh inkonsistensi: Harga 3&times; lebih penting dari Baterai, Baterai 3&times; lebih penting dari GPS,
        namun Harga hanya 2&times; lebih penting dari GPS. Ini kontradiktif (seharusnya &asymp; 9&times;).</i>
        </div>""", unsafe_allow_html=True)

# ============================================================
# TAB HASIL
# ============================================================
with tab_hasil:
    if cr > 0.10:
        st.warning(f"CR = {cr:.4f} melebihi 0.10. Bobot tidak konsisten — hasil mungkin kurang representatif. Perbaiki penilaian di tab Pembobotan AHP.")

    if len(df_filtered) == 0:
        st.info("Tidak ada produk sesuai filter. Ubah pengaturan di sidebar.")
    else:
        dn = df_filtered.copy().reset_index(drop=True)
        inv_h = 1.0 / dn['Price (USD)'].replace(0, 0.01)
        dn['N_Harga'] = inv_h / inv_h.sum()

        def benefit(col):
            s = dn[col].sum()
            return dn[col] / s if s != 0 else pd.Series(1/len(dn), index=dn.index)

        dn['N_Baterai'] = benefit('Battery Life (days)')
        dn['N_Air']     = benefit('Water Resistance (meters)')
        dn['N_HRM']     = benefit('Heart Rate Monitor')
        dn['N_GPS']     = benefit('GPS')

        df_res = df_filtered.copy()
        df_res['Skor_AHP'] = (
            dn['N_Harga']   * bobot_akhir[0] +
            dn['N_Baterai'] * bobot_akhir[1] +
            dn['N_Air']     * bobot_akhir[2] +
            dn['N_HRM']     * bobot_akhir[3] +
            dn['N_GPS']     * bobot_akhir[4]
        ) * 100

        df_final = df_res.sort_values('Skor_AHP', ascending=False).reset_index(drop=True)
        df_final.index += 1
        df_final = df_final.reset_index().rename(columns={"index":"Peringkat"})

        st.markdown("#### Podium Rekomendasi")
        podium = st.columns(3)
        medals = [
            ("Peringkat Pertama",  "winner-gold"),
            ("Peringkat Kedua",    "winner-silver"),
            ("Peringkat Ketiga",   "winner-bronze"),
        ]
        for i, (lbl, cls) in enumerate(medals):
            if len(df_final) > i:
                r = df_final.iloc[i]
                with podium[i]:
                    st.markdown(f"""<div class="winner-card {cls}">
                      <div class="winner-place-label">{lbl}</div>
                      <div class="name">{r['Brand']}<br>{r['Model']}</div>
                      <div class="score">${r['Price (USD)']:.0f} &nbsp;&bull;&nbsp; Skor {r['Skor_AHP']:.3f}</div>
                    </div>""", unsafe_allow_html=True)

        st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

        col_tbl2, col_info = st.columns([3, 1], gap="large")
        with col_tbl2:
            st.markdown(f"#### Top 10 dari {len(df_final)} Produk")
            show_cols = [c for c in ['Peringkat','Brand','Model','Price (USD)',
                                     'Battery Life (days)','Water Resistance (meters)',
                                     'Heart Rate Monitor','GPS','Skor_AHP'] if c in df_final.columns]
            df_show = df_final[show_cols].head(10).copy()
            df_show['Heart Rate Monitor'] = df_show['Heart Rate Monitor'].map({1:'Ya', 0:'Tidak'})
            df_show['GPS']                = df_show['GPS'].map({1:'Ya', 0:'Tidak'})
            st.dataframe(df_show, use_container_width=True, hide_index=True,
                column_config={
                    "Price (USD)":               st.column_config.NumberColumn("Harga (USD)", format="$%.2f"),
                    "Battery Life (days)":       st.column_config.NumberColumn("Baterai (hr)", format="%.1f"),
                    "Water Resistance (meters)": st.column_config.NumberColumn("Tahan Air (m)"),
                    "Skor_AHP": st.column_config.ProgressColumn(
                        "Skor AHP", min_value=0,
                        max_value=float(df_final['Skor_AHP'].max()), format="%.3f"),
                })
        with col_info:
            st.markdown("#### Bobot Digunakan")
            df_w_show = pd.DataFrame({"Kriteria": kriteria_list,
                                      "Bobot (%)": np.round(bobot_akhir*100, 2)
                                      }).sort_values("Bobot (%)", ascending=False)
            st.dataframe(df_w_show, use_container_width=True, hide_index=True,
                column_config={"Bobot (%)": st.column_config.ProgressColumn(
                    "Bobot (%)", min_value=0, max_value=100, format="%.1f%%")})
            status_cr = "Konsisten" if cr <= 0.1 else "Tidak Konsisten"
            st.markdown(f'<div class="step-card">CR = <b>{cr:.4f}</b><br>{status_cr}</div>', unsafe_allow_html=True)

        st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
        st.markdown("#### Visualisasi Top 10")
        vc1, vc2 = st.columns(2)
        with vc1:
            st.markdown("**Skor AHP**")
            top10 = df_final.head(10).copy()
            top10['Nama'] = top10['Brand'] + " " + top10['Model']
            st.bar_chart(top10.sort_values('Skor_AHP').set_index('Nama')['Skor_AHP'],
                         use_container_width=True, color="#4E7A3A")
        with vc2:
            st.markdown("**Harga vs Skor AHP**")
            sc = df_final.head(10).copy()
            sc['Nama'] = sc['Brand'] + " " + sc['Model']
            st.scatter_chart(sc.set_index('Nama')[['Price (USD)','Skor_AHP']],
                             x='Price (USD)', y='Skor_AHP', use_container_width=True)

        with st.expander("Detail Skor Normalisasi Tiap Alternatif", expanded=False):
            dn_d = dn[['N_Harga','N_Baterai','N_Air','N_HRM','N_GPS']].copy()
            dn_d.columns = ['Norm.Harga','Norm.Baterai','Norm.Tahan Air','Norm.HRM','Norm.GPS']
            dn_d.insert(0,'Brand', df_filtered['Brand'].values)
            dn_d.insert(1,'Model', df_filtered['Model'].values)
            dn_d['Skor_AHP'] = df_res['Skor_AHP'].values
            dn_d = dn_d.sort_values('Skor_AHP', ascending=False).reset_index(drop=True)
            st.dataframe(dn_d.style.format({
                c: "{:.5f}" for c in dn_d.columns if c not in ['Brand','Model']
            }).background_gradient(cmap='YlGn', subset=['Skor_AHP']),
            use_container_width=True, hide_index=True)
            st.markdown("""<div class="step-card">
            <b>Metode normalisasi:</b><br>
            &nbsp;&nbsp;Harga (Cost): diinvers (1/harga) lalu dibagi total &mdash; produk lebih murah mendapat skor lebih tinggi.<br>
            &nbsp;&nbsp;Benefit lainnya: dibagi total kolom &mdash; nilai lebih besar mendapat skor lebih tinggi.
            </div>""", unsafe_allow_html=True)
