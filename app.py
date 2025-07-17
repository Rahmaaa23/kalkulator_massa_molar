import streamlit as st
import re

# Data massa atom relatif
massa_atom = {
    "H": 1.008,
    "Li": 6.94,
    "Be": 9.01,
    "Na": 22.99,
    "Mg": 24.31,
    "K": 39.10,
    "Ca": 40.08,
    "Rb": 85.468,
    "Cs": 132.91,
    "Fr": 223.00,
    "Sr": 87.62,
    "Ba": 137.33,
    "Ra": 226.00,
    "Sc": 44.956,
    "Y": 88.906,
    "Ti": 47.867,
    "Zr": 91.224,
    "Hf": 178.49,
    "Rf": 267.00,
    "V": 50.942,
    "Nb": 92.906,
    "Ta": 180.95,
    "Db": 268.00,
    "Mn":  54.938,
    "Tc": 98.00,
    "Re": 186.21,
    "Bh": 270.00,
    "Fe": 55.845,
    "Ru": 101.07,
    "Os": 190.23,
    "Hs": 277.00,
    "Co": 58.933,
    "Rh": 102.91,
    "Ir": 192.22,
    "Mt": 278.00,
    "Ni": 58.693,
    "Pd": 106.42,
    "Pt": 195.08,
    "Ds": 281.00,
    "Cu": 63.546,
    "Ag": 107.87,
    "Au": 196.97,
    "Rg": 282.00,
    "Zn": 65.38,
    "Cd": 112.41,
    "Hg": 200.59,
    "Cn": 285.00,
    "B" : 10.81,
    "Al": 26.982,
    "Ga": 69.723,
    "In": 114.82,
    "Tl": 204.38,
    "Nh": 286.00,
    "C": 12.011,
    "Si": 28.085,
    "Ge": 72.630,
    "Sn": 118.71,
    "Pb": 207.20,
    "Fl": 289.00,
    "N": 14.007,
    "P": 30.974,
    "As": 74.922,
    "Sb": 121.76,
    "Bi": 208.98,
    "Mc": 290.00,
    "O": 15.999,
    "S": 32.06,
    "Se": 78.971,
    "Te": 127.60,
    "Po": 209.00,
    "Lv": 293.00,
    "F" : 18.998,
    "Cl": 35.45,
    "Br": 79.904,
    "I": 126.90,
    "At": 210.00,
    "Ts": 294.00,
    "He": 4.0026,
    "Ne": 20.180,
    "Ar": 39.948,
    "Kr": 83.798,
    "Xe": 131.29,
    "Rn": 222.00,
    "Og": 294.00,
    "La": 138.91,
    "Ce": 140.12,
    "Pr": 140.91,
    "Nd": 144.24,
    "Pm": 145.00,
    "Sm": 150.36,
    "Eu": 151.96,
    "Gd": 157.25,
    "Tb": 158.93,
    "Dy": 162.50,
    "Ho": 156.93,
    "Er": 167.26,
    "Tm": 168.93,
    "Yb": 173.05,
    "Lu": 174.97,
    "Ac": 227.00,
    "Th": 232.04,
    "Pa": 231.04,
    "U": 238.03,
    "Np": 237.00,
    "Pu": 244.00,
    "Am": 243.00,
    "Cm": 247.00,
    "Bk": 247.00,
    "Cf": 251.00,
    "Es": 252.00,
    "Fm": 257.00,
    "Md": 258.00,
    "No": 259.00,
    "Lr": 266.00
}
import streamlit as st
import streamlit as st

st.set_page_config(layout="wide")

# Sidebar Navigasi
halaman = st.sidebar.radio("📌 Navigasi", [
    "🏠 Beranda", 
    "🧪 Kalkulator Massa Molar", 
    "🧬 Tabel Periodik", 
    "ℹ️ Tentang Aplikasi"
])

# Konten Tiap Halaman
if halaman == "🏠 Beranda":
    st.title("🏠 Beranda")
    st.write("Selamat datang di **Aplikasi Kalkulator Kimia Interaktif**. Gunakan menu di sidebar untuk berpindah halaman.")
    st.image("data:image/jpeg;base64,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", use_container_width=True)

elif halaman == "🧪 Kalkulator Massa Molar":
    st.title("🧪 Kalkulator Massa Molar")
    st.write("Masukkan rumus senyawa untuk menghitung massa molarnya.")
    # Tambahkan kode kalkulator kamu di sini

# Fungsi parsing rumus kimia sederhana
def hitung_massa_molar(rumus):
    pattern = r'([A-Z][a-z]*)(\d*)'
    elemen = re.findall(pattern, rumus)
    massa_total = 0

    for simbol, jumlah in elemen:
        if simbol not in massa_atom:
            return None, f"Unsur '{simbol}' tidak ditemukan dalam database."
        n = int(jumlah) if jumlah else 1
        massa_total += massa_atom[simbol] * n

    return massa_total, None

# UI Streamlit
st.set_page_config(page_title="Kalkulator Massa Molar", page_icon="🧪")
st.title("Kalkulator Massa Molar Senyawa Kimia")
st.markdown("""
<style>
.big-font {
    font-size:32px !important;
    color: #4CAF50;
}
.result-box {
    padding: 1.2em;
    background-color: #e8f5e9;
    border-radius: 10px;
    border-left: 6px solid #4CAF50;
    font-size: 18px;
}
.error-box {
    padding: 1.2em;
    background-color: #ffebee;
    border-radius: 10px;
    border-left: 6px solid #f44336;
    font-size: 18px;
}
</style>
""", unsafe_allow_html=True)
# Form input
with st.form("form_kimia"):
    rumus = st.text_input("Rumus Kimia", placeholder="Contoh: H2O, NaCl, CH3COOH")
    submit = st.form_submit_button("Hitung Massa Molar")

# Hasil
if submit:
    if rumus.strip() == "":
        st.warning("Silakan masukkan rumus senyawa terlebih dahulu.")
    else:
        hasil, error = hitung_massa_molar(rumus.strip())
        if error:
            st.markdown(f'<div class="error-box">❌ {error}</div>', unsafe_allow_html=True)
        else:
            st.markdown(
                f'<div class="result-box">✅ Massa molar dari <strong>{rumus}</strong> adalah '
                f'<strong>{hasil:.3f} g/mol</strong>.</div>', 
                unsafe_allow_html=True
            )




    
elif halaman == "🧬 Tabel Periodik":
    st.title("🧬 Tabel Periodik Interaktif")
    st.write("Klik unsur untuk melihat massa atom relatifnya.")
    # Tambahkan kode tabel periodik kamu di sini



    
import streamlit as st

st.set_page_config(layout="wide")

st.markdown("""
    <style>
    button[kind="secondary"] {
        font-size: 10px !important;
        padding: 3px 4px !important;
        height: auto !important;
    }
    </style>
""", unsafe_allow_html=True)

# Dictionary Ar unsur (massa atom relatif)
massa_atom = {
    "H": 1.008, "He": 4.0026, "Li": 6.94, "Be": 9.0122, "B": 10.81, "C": 12.01, "N": 14.01,
    "O": 16.00, "F": 18.998, "Ne": 20.18, "Na": 22.99, "Mg": 24.305, "Al": 26.98, "Si": 28.09,
    "P": 30.97, "S": 32.07, "Cl": 35.45, "Ar": 39.95, "K": 39.10, "Ca": 40.08, "Sc": 44.96,
    "Ti": 47.87, "V": 50.94, "Cr": 52.00, "Mn": 54.94, "Fe": 55.85, "Co": 58.93, "Ni": 58.69,
    "Cu": 63.55, "Zn": 65.38, "Ga": 69.72, "Ge": 72.63, "As": 74.92, "Se": 78.96, "Br": 79.90,
    "Kr": 83.80, "Rb": 85.47, "Sr": 87.62, "Y": 88.91, "Zr": 91.22, "Nb": 92.91, "Mo": 95.95,
    "Tc": 98, "Ru": 101.1, "Rh": 102.9, "Pd": 106.4, "Ag": 107.9, "Cd": 112.4, "In": 114.8,
    "Sn": 118.7, "Sb": 121.8, "Te": 127.6, "I": 126.9, "Xe": 131.3, "Cs": 132.9, "Ba": 137.3,
    "La": 138.9, "Ce": 140.1, "Pr": 140.9, "Nd": 144.2, "Pm": 145, "Sm": 150.4, "Eu": 152.0,
    "Gd": 157.3, "Tb": 158.9, "Dy": 162.5, "Ho": 164.9, "Er": 167.3, "Tm": 168.9, "Yb": 173.0,
    "Lu": 175.0, "Hf": 178.5, "Ta": 180.9, "W": 183.8, "Re": 186.2, "Os": 190.2, "Ir": 192.2,
    "Pt": 195.1, "Au": 197.0, "Hg": 200.6, "Tl": 204.4, "Pb": 207.2, "Bi": 208.9, "Po": 209,
    "At": 210, "Rn": 222, "Fr": 223, "Ra": 226, "Ac": 227, "Th": 232.0, "Pa": 231.0, "U": 238.0,
    "Np": 237, "Pu": 244, "Am": 243, "Cm": 247, "Bk": 247, "Cf": 251, "Es": 252, "Fm": 257,
    "Md": 258, "No": 259, "Lr": 262, "Rf": 267, "Db": 270, "Sg": 271, "Bh": 270, "Hs": 277,
    "Mt": 276, "Ds": 281, "Rg": 280, "Cn": 285, "Nh": 284, "Fl": 289, "Mc": 288, "Lv": 293,
    "Ts": 294, "Og": 294
}

# Struktur grid periodik
grid = [
    ["H", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "He"],
    ["Li", "Be", "", "", "", "", "", "", "", "", "", "", "B", "C", "N", "O", "F", "Ne"],
    ["Na", "Mg", "", "", "", "", "", "", "", "", "", "", "Al", "Si", "P", "S", "Cl", "Ar"],
    ["K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr"],
    ["Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "I", "Xe"],
    ["Cs", "Ba", "La", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi", "Po", "At", "Rn"],
    ["Fr", "Ra", "Ac", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds", "Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og"]
]

lanthanida = ["Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu"]
aktinida = ["Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md", "No", "Lr"]

# Init session_state
if "selected" not in st.session_state:
    st.session_state.selected = None

st.set_page_config(layout="wide")
st.title("🔬 Tabel Periodik")
st.markdown("Klik salah satu unsur untuk menampilkan Ar-nya (massa atom relatif).")


# Fungsi tampilkan baris
def tampilkan_baris(baris, baris_id):
    cols = st.columns(18)
    for i in range(18):
        elemen = baris[i] if i < len(baris) else ""
        if elemen:
            if cols[i].button(elemen, key=f"{baris_id}_{i}_{elemen}"):
                st.session_state.selected = elemen
        else:
            cols[i].markdown("")
# Tampilkan seluruh baris
for baris_index, baris in enumerate(grid):
    # tambahkan padding kosong jika kurang dari 18
    padding = 18 - len(baris)
    tampilkan_baris(baris + [""] * padding, f"main_{baris_index}")

# Lanthanida
st.markdown("### Lanthanida")
tampilkan_baris(lanthanida + [""] * (18 - len(lanthanida)), "lanthanida")

# Aktinida
st.markdown("### Aktinida")
tampilkan_baris(aktinida + [""] * (18 - len(aktinida)), "aktinida")

# Hasil klik
if st.session_state.selected:
    sim = st.session_state.selected
    ar = massa_atom.get(sim, "Tidak ditemukan")
    st.success(f"**{sim}** → Ar = **{ar}**")
    st.markdown(f"<h1 style='text-align: center; font-size: 80px;'>{sim}</h1>", unsafe_allow_html=True)

elif halaman == "ℹ️ Tentang Aplikasi":
    st.title("ℹ️ Tentang Aplikasi")
    st.markdown("""
    Aplikasi ini dibuat menggunakan **Python + Streamlit** untuk membantu pelajar dan mahasiswa dalam mempelajari konsep kimia seperti massa molar dan tabel periodik. """)
    #gambar
col1, col2 = st.columns([1, 2])
with col1:
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSVx1ePJuorDta4eJJvcLPiKPyvGLUFU2PFIznnQqQ5ghkbeiGO8ssJxHu64vbv0IoVvfo&usqp=CAU", use_container_width=True)
with col2:
    st.markdown('<div class="big-font">🧪 Kalkulator Massa Molar Senyawa</div>', unsafe_allow_html=True)
    st.write("Website ini digunakan untuk menghitung **massa molar** senyawa kimia berdasarkan rumus kimia yang Anda masukkan. Rumus kimia senyawa yang dimasukkan seperti `H2O`, `NaCl`, `C6H12O6` untuk menghitung massa molarnya. Adapun acuan tabel periodik yang digunakan yaitu pada bagian akhir web")

# ===============================
# PENJELASAN MASSA MOLAR
# ===============================

with st.expander("📘 Apa itu Massa Molar?"):
    st.markdown("""
**Massa molar** adalah massa satu mol suatu zat (unsur atau senyawa), biasanya dinyatakan dalam satuan gram per mol (g/mol).  
Contohnya:
- Massa molar air (H2O) adalah sekitar 18.02 g/mol
- Massa molar natrium klorida (NaCl) adalah sekitar 58.44 g/mol

Massa molar diperoleh dengan menjumlahkan massa atom relatif dari unsur-unsur penyusun senyawa tersebut, dikalikan dengan jumlahnya masing-masing.
""")
with st.expander("📘 Bagaimana cara mencari massa molar?"):
    st.markdown("""
**Massa molar** senyawa dihitung dengan menjumlahkan massa atom relatif (Ar) tiap unsur dikalikan jumlah atomnya. Misalnya pada H2O: hidrogen (Ar = 1) ada 2 atom, sehingga totalnya 2 x 1 = 2; oksigen (Ar = 16) ada 1 atom, jadi 1 x 16 = 16. Maka, massa molar H2O adalah 2 + 16 = **18 g/mol**.

""")


  
