import streamlit as st
st.title("kalkulator massa molar:")
import streamlit as st

# Judul Aplikasi
st.title("Kalkulator Massa Molar")

# Input rumus kimia (sangat sederhana)
unsur = st.text_input("Masukkan simbol unsur (contoh: Na, Cl, H, O):")
jumlah = st.number_input("Jumlah atom unsur", min_value=1, step=1)

# Tabel massa atom (sangat terbatas)
massa_atom = {
    "H": 1.008,
    "C": 12.01,
    "O": 16.00,
    "Na": 22.99,
    "Cl": 35.45,
    "N": 14.01,
    "S": 32.07
}

# Kalkulasi
if unsur in massa_atom:
    total_massa = massa_atom[unsur] * jumlah
    st.success(f"Massa molar dari {jumlah} atom {unsur} adalah {total_massa:.2f} g/mol")
elif unsur != "":
    st.error("Unsur tidak ditemukan dalam database.")

st.markdown("---")
st.caption("Versi sederhana – tambahkan lebih banyak fitur sesuai kebutuhan.")
