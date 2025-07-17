import streamlit as st
import re

# Data massa atom dasar (bisa ditambah)
massa_atom = {
    "H": 1.008,
    "He": 4.003,
    "Li": 6.94,
    "Be": 9.01,
    "B": 10.81,
    "C": 12.01,
    "N": 14.01,
    "O": 16.00,
    "F": 18.998,
    "Na": 22.99,
    "Mg": 24.31,
    "Al": 26.98,
    "Si": 28.09,
    "P": 30.97,
    "S": 32.07,
    "Cl": 35.45,
    "K": 39.10,
    "Ca": 40.08,
    "Fe": 55.85,
    "Cu": 63.55,
    "Zn": 65.38
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
st.markdown("Masukkan rumus kimia (misal: `H2O`, `NaCl`, `C6H12O6`)")

input_rumus = st.text_input("Rumus Kimia:")

if input_rumus:
    hasil, error = hitung_massa_molar(input_rumus)
    if error:
        st.error(error)
    else:
        st.success(f"Massa molar dari {input_rumus} adalah {hasil:.3f} g/mol")

st.markdown("---")
st.caption("Versi sederhana | Dibuat dengan ❤️ oleh Streamlit")
