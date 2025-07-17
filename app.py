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
st.title("🧪 Kalkulator Massa Molar Senyawa Kimia")
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

# Judul
st.markdown('<div class="big-font">Kalkulator Massa Molar Senyawa Kimia</div>', unsafe_allow_html=True)
import streamlit as st
st.image("unsur kimia.jpg", caption="unsur kimia")
st.write("Masukkan rumus kimia senyawa seperti `H2O`, `NaCl`, `C6H12O6` untuk menghitung massa molarnya.")

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
            
