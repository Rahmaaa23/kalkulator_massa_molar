import streamlit as st
import re
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://mmc.tirto.id/image/2021/07/05/istock-1208824917_ratio-16x9.jpg");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }

    .block-container {
        background-color: rgba(255, 255, 255, 0.65); /* putih semi-transparan untuk konten */
        padding: 2rem;
        border-radius: 12px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# =========================
# DATA MASSA ATOM RELATIF
# =========================
massa_atom = {
   
# =========================
# SIDEBAR NAVIGASI
# =========================
st.set_page_config(page_title="Kimia Interaktif", layout="wide", page_icon="🧪")

halaman = st.sidebar.radio("Navigasi", [ "🧪 Kalkulator Massa Molar", "🧬 Tabel Periodik", "🏠 Dasar Teori", "ℹ️ Tentang Aplikasi"])


# =========================
# HALAMAN KALKULATOR
# =========================
if halaman == "🧪 Kalkulator Massa Molar":
    st.title("🧪 Kalkulator Massa Molar Senyawa Kimia")
    st.markdown("""
Selamat datang di *Aplikasi Kimia Interaktif* berbasis Streamlit!  
Di sini kamu dapat:

- Menghitung *massa molar* senyawa kimia  
- Menelusuri *tabel periodik interaktif*  
- Mempelajari unsur dan Ar (massa atom relatif)-nya dengan mudah  
""")


    with st.expander("📘 Apa itu Massa Molar?"):
        st.markdown("""
*Massa molar* adalah jumlah massa dari semua atom dalam satu mol senyawa, dinyatakan dalam g/mol.

Contoh:
- H₂O → 2×H + 1×O = 2×1.008 + 15.999 ≈ *18.015 g/mol*
- NaCl → Na + Cl = 22.99 + 35.45 = *58.44 g/mol*
        """)

    rumus = st.text_input("Masukkan Rumus Kimia", placeholder="Contoh: H2O, NaCl, C6H12O6")

    def hitung_massa_molar(rumus):
        pattern = r'([A-Z][a-z])(\d)'
        elemen = re.findall(pattern, rumus)
        massa_total = 0
        for simbol, jumlah in elemen:
            if simbol not in massa_atom:
                return None, f"Unsur '{simbol}' tidak ditemukan."
            n = int(jumlah) if jumlah else 1
            massa_total += massa_atom[simbol] * n
        return massa_total, None

    if st.button("Hitung Massa Molar"):
        if rumus.strip() == "":
            st.warning("⚠️ Masukkan rumus terlebih dahulu.")
        else:
            hasil, error = hitung_massa_molar(rumus.strip())
            if error:
                st.error(error)
            else:
                st.success(f"Massa molar dari *{rumus}* adalah *{hasil:.3f} g/mol*")

# =========================
# HALAMAN TABEL PERIODIK
# =========================
elif halaman == "🧬 Tabel Periodik":

    st.title("🔬 Tabel Periodik Unsur")

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

    if "selected" not in st.session_state:
        st.session_state.selected = None

    def tampilkan_baris(baris, baris_id):
        cols = st.columns(18)
        for i in range(18):
            elemen = baris[i] if i < len(baris) else ""
            if elemen:
                if cols[i].button(elemen, key=f"{baris_id}{i}{elemen}"):
                    st.session_state.selected = elemen
            else:
                cols[i].markdown("")

    for idx, baris in enumerate(grid):
        tampilkan_baris(baris + [""] * (18 - len(baris)), f"main_{idx}")

    st.markdown("### Lanthanida")
    tampilkan_baris(lanthanida + [""] * (18 - len(lanthanida)), "lanthanida")

    st.markdown("### Aktinida")
    tampilkan_baris(aktinida + [""] * (18 - len(aktinida)), "aktinida")

    if st.session_state.selected:
        sim = st.session_state.selected
        ar = massa_atom.get(sim, "Tidak ditemukan")
        st.success(f"*{sim}* → Ar = *{ar}*")
        st.markdown(f"<h1 style='text-align: center; font-size: 80px;'>{sim}</h1>", unsafe_allow_html=True)
# =========================
# HALAMAN BERANDA
# =========================
elif halaman == "🏠 Dasar Teori":
      st.title("Dasar teori massa molar")
      st.markdown("""
Massa molar adalah massa dari satu mol suatu zat (unsur atau senyawa), yang dinyatakan dalam satuan gram per mol (g/mol). Konsep ini merupakan turunan dari hukum Avogadro yang menyatakan bahwa satu mol zat mengandung 6,022 × 10²³ partikel (atom, ion, atau molekul).

✅ Pada Unsur
Massa molar unsur sama dengan massa atom relatif (Ar) dalam satuan gram/mol. Misalnya:

Hidrogen (H) memiliki Ar = 1,008 → maka massa molar H = 1,008 g/mol

Karbon (C) memiliki Ar = 12,011 → massa molarnya = 12,011 g/mol

Nilai Ar ini diperoleh dari rata-rata massa isotop unsur tersebut yang terdapat di alam, disesuaikan dengan kelimpahannya.

✅ Pada Senyawa
Massa molar senyawa adalah jumlah dari massa molar tiap unsur penyusunnya, dikalikan dengan jumlah atom dari masing-masing unsur. Contohnya:

Air (H₂O):

2 atom H × 1,008 = 2,016

1 atom O × 15,999 = 15,999

Total massa molar = 18,015 g/mol

Karbon dioksida (CO₂):

1 atom C × 12,011 = 12,011

2 atom O × 15,999 = 31,998

Total massa molar = 44,009 g/mol

Perhitungan ini penting dalam stoikiometri kimia, analisis kuantitatif, dan perhitungan reaksi kimia.

🔍 Pentingnya Massa Molar
Massa molar digunakan untuk:

Mengonversi antara jumlah mol dan massa dalam gram.

Menghitung pereaksi dan hasil dalam reaksi kimia.

Analisis laboratorium dan preparasi larutan.
""")

    
    
# =========================
# HALAMAN TENTANG
# =========================
elif halaman == "ℹ️ Tentang Aplikasi":
    st.title("ℹ️ Tentang Aplikasi Kimia Interaktif")
    st.markdown("""
Aplikasi ini dibuat untuk membantu pelajar memahami konsep dasar *massa molar* dan *tabel periodik*.  
Fitur:
- Hitung massa molar dari senyawa kimia
- Tabel periodik interaktif (klik unsur untuk lihat Ar)
- Mobile-friendly dan dapat digunakan tanpa instalasi tambahan

Dikembangkan menggunakan Python dan Streamlit.
""")
