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
    "H": 1.008, "He": 4.0026, "Li": 6.94, "Be": 9.0122, "B": 10.81, "C": 12.01, "N": 14.01,
    "O": 16.00, "F": 18.998, "Ne": 20.18, "Na": 22.99,…
[00.51, 18/7/2025] Rahma: def tampilkan_baris(baris, baris_id):
    cols = st.columns(18)
    for i in range(18):
        elemen = baris[i] if i < len(baris) else ""
        if elemen:
            with cols[i]:
                st.markdown(
                    f"""
                    <style>
                    .element-button {{
                        font-size: 12px;
                        padding: 6px 2px;
                        width: 100%;
                        height: 45px;
                        background-color: #f0f0f0;
                        border-radius: 6px;
                        border: 1px solid #ccc;
                        text-align: center;
                    }}
                    </style>
                    """, unsafe_allow_html=True
                )
                if st.button(elemen, key=f"{baris_id}{i}{elemen}"):
                    st.session_state.selected = elemen
        else:
            cols[i].markdown("")
