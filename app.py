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
