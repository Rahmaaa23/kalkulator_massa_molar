import streamlit as st
import re

# =========================
# BACKGROUND
# =========================

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

# =========================
# SIDEBAR NAVIGASI
# =========================
st.set_page_config(page_title="Kalkulator Massa Molar", layout="wide", page_icon="🧪")

halaman = st.sidebar.radio("MENU", [  "🏠 Dasar Teori", "🧪 Kalkulator Massa Molar", "🧬 Tabel Periodik", "ℹ️ Tentang Aplikasi"])

# =========================
# HALAMAN DASAR TEORI
# =========================
if halaman == "🏠 Dasar Teori":
    st.title("Selamat datang di Aplikasi Kimia berbasis Streamlit!")
    st.header("""**Aplikasi ini menawarkan beberapa fitur pada kolom menu yang dapat digunakan yaitu:**
- **Menghitung massa molar senyawa kimia** 
- **Menelusuri tabel periodik** 
- **Mempelajari unsur dan Ar (massa atom relatif)-nya dengan mudah**
""")
    st.title("Dasar Teori massa molar")
    st.header("📖Pengertian Massa Molar")
    st.markdown("""
Massa molar adalah massa dari satu mol suatu zat (unsur atau senyawa), yang dinyatakan dalam satuan gram per mol (g/mol). Konsep ini merupakan turunan dari hukum Avogadro yang menyatakan bahwa satu mol zat mengandung 6,022 × 10²³ partikel (atom, ion, atau molekul).

Pada Unsur
Massa molar unsur sama dengan massa atom relatif (Ar) dalam satuan gram/mol. Misalnya:

Hidrogen (H) memiliki Ar = 1,008 → maka massa molar H = 1,008 g/mol

Karbon (C) memiliki Ar = 12,011 → massa molarnya = 12,011 g/mol

Nilai Ar ini diperoleh dari rata-rata massa isotop unsur tersebut yang terdapat di alam, disesuaikan dengan kelimpahannya.
""")
    st.header("💯Perhitungan Massa Molar")
    st.markdown("""
Pada Senyawa
Massa molar senyawa adalah jumlah dari massa molar tiap unsur penyusunnya, dikalikan dengan jumlah atom dari masing-masing unsur. Contohnya:

**Air (H₂O)**:

2 atom H × 1,008 = 2,016

1 atom O × 15,999 = 15,999

Total massa molar = 18,015 g/mol

**Karbon dioksida (CO₂)**:

1 atom C × 12,011 = 12,011

2 atom O × 15,999 = 31,998

Total massa molar = 44,009 g/mol

Perhitungan ini penting dalam stoikiometri kimia, analisis kuantitatif, dan perhitungan reaksi kimia.
""")
    st.header("🔍Kegunaan Massa Molar")
    st.markdown("""
Pentingnya Massa Molar
Massa molar digunakan untuk:
- Mengonversi antara jumlah mol dan massa dalam gram.
- Menghitung pereaksi dan hasil dalam reaksi kimia.
- Analisis laboratorium dan preparasi larutan.
""")

 
    

# =========================
# HALAMAN KALKULATOR
# =========================
elif halaman == "🧪 Kalkulator Massa Molar":
    st.title("🧪 Kalkulator Massa Molar Senyawa Kimia")

    with st.expander("📌 Petunjuk penggunaan fitur massa molar"):
        st.markdown("""
📌 Petunjuk Penggunaan Fitur Massa Molar:
- Pengguna dapat menghitung massa molar dengan memasukkan rumus senyawa kimia pada kolom input yang telah disediakan.
- Penulisan rumus harus sesuai dengan aturan kimia, menggunakan simbol unsur dan angka indeks. 
- Contoh penulisan: 
  - Untuk senyawa sederhana: NaCl
  - Untuk senyawa dengan jumlah atom lebih dari satu: H2O (untuk air), CO2 (karbon dioksida)
- Gunakan huruf kapital dan angka dengan benar. Hindari penulisan seperti nacl, h2o, atau C o 2.
""")
        
    rumus = st.text_input("Masukkan Rumus Kimia", placeholder="Contoh: H2O, NaCl, C6H12O6")

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

    if st.button("Hitung Massa Molar"):
        if rumus.strip() == "":
            st.warning("⚠️ Masukkan rumus terlebih dahulu.")
        else:
            hasil, error = hitung_massa_molar(rumus.strip())
            if error:
                st.error(error)
            else:
                st.success(f"Massa molar dari {rumus} adalah {hasil:.3f} g/mol")
                
    
    st.info("Aplikasi ini belum mendukung input senyawa kimia yang mengandung tanda kurung, seperti: Fe(OH)3")                      
   

# =========================
# HALAMAN TABEL PERIODIK
# =========================
elif halaman == "🧬 Tabel Periodik":
    
    st.info("klik unsur, scroll kebawah untung melihat massa atom relatif.")
    st.markdown("""
    <h1 style='text-align: center; color: #2c3e50; font-family: Arial, sans-serif; margin-top: 10px;'>
    🔬 Tabel Periodik Unsur
    </h1>
    """, unsafe_allow_html=True)


    
    grid = [
        ["H", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "He"],
        ["Li", "Be", "", "", "", "", "", "", "", "", "", "", "B", "C", "N", "O", "F", "Ne"],
        ["Na", "Mg", "", "", "", "", "", "", "", "", "", "", "Al", "Si", "P", "S", "Cl", "Ar"],
        ["K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr"],
        ["Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "I", "Xe"],
        ["Cs", "Ba", "", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi", "Po", "At", "Rn"],
        ["Fr", "Ra", "", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds", "Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og"]
    ]

    lanthanida = ["La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu"]
    aktinida = ["Ac", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md", "No", "Lr"]

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
        st.success(f"{sim} → Ar = {ar}")
        st.markdown(f"<h1 style='text-align: center; font-size: 80px;'>{sim}</h1>", unsafe_allow_html=True)
        
    st.markdown("### 🖼️ Referensi Gambar")
    st.image(
    "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEijgeH1Dc3KYGXmDhfr8cGhOouAOTXK5VTsewxpW9fLFfzVFmnZ0h-UsjFNOJgPw1qKLW6s9f2c9POTIinYEXCaRVR9fVjFYOEJKK0A_aspTnDXB54o0q4IKsFnrWyela5qqFR1GZvkvVJ-/s1600/sistem-periodik-unsur.jpg",
    use_container_width=True,
    caption="Tabel Periodik Lengkap"
        )



# =========================
# HALAMAN TENTANG APLIKASI
# =========================
elif halaman == "ℹ️ Tentang Aplikasi":
    st.title("ℹ️ Tentang Aplikasi Kimia")
    st.markdown("""
Aplikasi ini dibuat untuk membantu pelajar memahami konsep dasar massa molar dan tabel periodik.  
**Fitur**:
- Hitung massa molar dari senyawa kimia
- Tabel periodik interaktif (klik unsur untuk lihat Ar)
- Mobile-friendly dan dapat digunakan tanpa instalasi tambahan

**Kekurangan** aplikasi ini adalah masih berada dalam tahap pengembangan dan penyempurnaan, sehingga beberapa fitur belum berfungsi secara optimal. Sebagai contoh, fitur perhitungan massa molar belum dapat menangani senyawa dengan struktur bercabang atau yang menggunakan tanda kurung seperti Fe(OH)₃ secara akurat.

Dikembangkan menggunakan Python dan Streamlit.
""")
