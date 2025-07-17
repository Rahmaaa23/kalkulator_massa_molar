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
# "with" notation
with st.sidebar:
    st.[Kalkulator massa molar]

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
- Massa molar air (H₂O) adalah sekitar 18.02 g/mol
- Massa molar natrium klorida (NaCl) adalah sekitar 58.44 g/mol

Massa molar diperoleh dengan menjumlahkan massa atom relatif dari unsur-unsur penyusun senyawa tersebut, dikalikan dengan jumlahnya masing-masing.
""")
with st.expander("📘 Bagaimana cara mencari massa molar?"):
    st.markdown("""
**Massa molar** senyawa dihitung dengan menjumlahkan massa atom relatif (Ar) tiap unsur dikalikan jumlah atomnya. Misalnya pada H₂O: hidrogen (Ar = 1) ada 2 atom, sehingga totalnya 2 × 1 = 2; oksigen (Ar = 16) ada 1 atom, jadi 1 × 16 = 16. Maka, massa molar H₂O adalah 2 + 16 = **18 g/mol**.

""")
    
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
