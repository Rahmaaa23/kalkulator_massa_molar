import streamlit as st

# Massa atom dasar (bisa ditambah)
massa_atom = {
    "H": 1.008,
    "C": 12.01,
    "O": 16.00,
    "Na": 22.99,
    "Cl": 35.45,
    "N": 14.01,
    "S": 32.07,
    "K": 39.10,
    "Ca": 40.08
}

st.title("🧪 Kalkulator Kimia Sederhana")

# Navigasi
menu = st.sidebar.selectbox("Pilih fitur kalkulator", (
    "Massa Molar Unsur", 
    "Konsentrasi Larutan", 
    "pH Asam/Basa Kuat"
))

# ========== Fitur 1: Massa Molar Unsur ==========
if menu == "Massa Molar Unsur":
    st.header("🔬 Massa Molar Unsur")
    unsur = st.text_input("Masukkan simbol unsur (misal: Na, Cl, O):").capitalize()
    jumlah = st.number_input("Jumlah atom unsur", min_value=1, step=1)

    if unsur in massa_atom:
        massa_total = massa_atom[unsur] * jumlah
        st.success(f"Massa molar dari {jumlah} atom {unsur} = {massa_total:.2f} g/mol")
    elif unsur:
        st.error("Unsur tidak ditemukan dalam database.")

# ========== Fitur 2: Konsentrasi Larutan ==========
elif menu == "Konsentrasi Larutan":
    st.header("💧 Konsentrasi Larutan (Molaritas)")
    mol = st.number_input("Jumlah mol zat (mol)", min_value=0.0, step=0.01)
    volume = st.number_input("Volume larutan (liter)", min_value=0.0001, step=0.01)

    if volume > 0:
        M = mol / volume
        st.success(f"Konsentrasi larutan = {M:.3f} M")
    else:
        st.warning("Volume tidak boleh nol.")

# ========== Fitur 3: pH Asam/Basa Kuat ==========
elif menu == "pH Asam/Basa Kuat":
    st.header("🧪 Perhitungan pH (Asam/Basa Kuat)")
    jenis = st.selectbox("Pilih jenis larutan", ["Asam kuat", "Basa kuat"])
    konsentrasi = st.number_input("Konsentrasi larutan (M)", min_value=0.0, step=0.01)

    import math
    if konsentrasi > 0:
        if jenis == "Asam kuat":
            pH = -math.log10(konsentrasi)
            st.success(f"pH = {pH:.2f}")
        else:
            pOH = -math.log10(konsentrasi)
            pH = 14 - pOH
            st.success(f"pH = {pH:.2f}")
    elif konsentrasi == 0:
        st.info("Larutan netral → pH = 7")

# Footer
st.markdown("---")
st.caption("Dibuat dengan ❤️ menggunakan Streamlit | Versi sederhana")
