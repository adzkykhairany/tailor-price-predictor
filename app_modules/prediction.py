import streamlit as st
import numpy as np

def load_css():
    with open("app_modules/style.css", "r") as f:  # Pastikan path ke style.css benar
        css = f.read()
        st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

# Panggil CSS sebelum membuat form
load_css()

def show():
    st.title("👗 Prediksi Harga Jasa Jahit")

    # Sidebar Panduan
    st.sidebar.header("📌 Panduan Pengisian")
    st.sidebar.info(
        "1️⃣ Isi semua kolom input sesuai dengan kebutuhan jahitan Anda.\n\n"
        "2️⃣ Klik tombol **🎯 Hitung Perkiraan Harga** untuk mendapatkan estimasi biaya."
    )

    errors = {} 

    with st.form("input_form"):
        col1, col2 = st.columns(2)
        with col1:
            model_pakaian = st.selectbox("👗 Model Pakaian", 
                                         ["Pilih Model Pakaian", "Kebaya Tradisional", "Kebaya Modern", "Blus", "Midi Dress", "Maxi Dress"],
                                         index=0)
            if model_pakaian == "Pilih Model Pakaian":
                errors["model_pakaian"] = "⚠ Harap pilih model pakaian."

        with col2:
            jenis_bahan = st.selectbox("🧵 Jenis Bahan", 
                                       ["Pilih Jenis Bahan", "Katun", "Sutra", "Lace", "Sifon", "Satin"],
                                       index=0)
            if jenis_bahan == "Pilih Jenis Bahan":
                errors["jenis_bahan"] = "⚠ Harap pilih jenis bahan."

        col3, col4 = st.columns(2)
        with col3:
            ornamen_tambahan = st.selectbox("✨ Ornamen Tambahan", 
                                            ["Pilih Ornamen", "Tanpa Ornamen", "Bordir", "Renda", "Lipitan", "Payet"],
                                            index=0)
            if ornamen_tambahan == "Pilih Ornamen":
                errors["ornamen_tambahan"] = "⚠ Harap pilih ornamen tambahan."

        with col4:
            waktu_penyelesaian = st.selectbox("⏳ Waktu Penyelesaian", 
                                              ["Pilih Waktu Penyelesaian", "Reguler (>14 hari)", "Ekspres (2-14 hari)"],
                                              index=0)
            if waktu_penyelesaian == "Pilih Waktu Penyelesaian":
                errors["waktu_penyelesaian"] = "⚠ Harap pilih waktu penyelesaian."
        
        col5, _ = st.columns([1, 1])
        with col5:
            pengalaman_penjahit = st.selectbox("👨‍🏭 Pengalaman Penjahit", 
                                               ["Pilih Pengalaman Penjahit", "Pemula (<5 tahun)", "Menengah (5-10 tahun)", "Mahir (>10 tahun)"],
                                               index=0)
            if pengalaman_penjahit == "Pilih Pengalaman Penjahit":
                errors["pengalaman_penjahit"] = "⚠ Harap pilih pengalaman penjahit."

        _, col_submit = st.columns([2, 1])
        with col_submit:
            submit = st.form_submit_button("🎯 Hitung Perkiraan Harga")

    # show error
    if submit:
        with col1:
            if "model_pakaian" in errors:
                st.markdown(f'<p class="error-message">{errors["model_pakaian"]}</p>', unsafe_allow_html=True)
        with col2:
            if "jenis_bahan" in errors:
                st.markdown(f'<p class="error-message">{errors["jenis_bahan"]}</p>', unsafe_allow_html=True)
        with col3:
            if "ornamen_tambahan" in errors:
                st.markdown(f'<p class="error-message">{errors["ornamen_tambahan"]}</p>', unsafe_allow_html=True)
        with col4:
            if "waktu_penyelesaian" in errors:
                st.markdown(f'<p class="error-message">{errors["waktu_penyelesaian"]}</p>', unsafe_allow_html=True)
        with col5:
            if "pengalaman_penjahit" in errors:
                st.markdown(f'<p class="error-message">{errors["pengalaman_penjahit"]}</p>', unsafe_allow_html=True)

        if not errors:
            mapping_model_pakaian = {"Kebaya Tradisional": 0, "Kebaya Modern": 1, "Blus": 2, "Midi Dress": 3, "Maxi Dress": 4}
            mapping_jenis_bahan = {"Katun": 0, "Sutra": 1, "Lace": 2, "Sifon": 3, "Satin": 4}
            mapping_ornamen_tambahan = {"Tanpa Ornamen": 0, "Bordir": 1, "Renda": 2, "Lipitan": 3, "Payet": 4}
            mapping_waktu_penyelesaian = {"Reguler (>14 hari)": 0, "Ekspres (2-14 hari)": 1}
            mapping_pengalaman_penjahit = {"Pemula (<5 tahun)": 0, "Menengah (5-10 tahun)": 1, "Mahir (>10 tahun)": 2}

            X_input = np.array([
                mapping_model_pakaian[model_pakaian],
                mapping_jenis_bahan[jenis_bahan],
                mapping_ornamen_tambahan[ornamen_tambahan],
                mapping_waktu_penyelesaian[waktu_penyelesaian],
                mapping_pengalaman_penjahit[pengalaman_penjahit]
            ]).reshape(1, -1)

            # dummy prediction
            def dummy_prediction():
                harga_min = np.random.randint(150000, 500000)  # Harga minimum
                harga_max = harga_min + np.random.randint(50000, 300000)  # Harga maksimum

                return harga_min, harga_max

            harga_min, harga_max = dummy_prediction()
            harga_prediksi = np.random.randint(100000, 1000000)

            st.success(f"💰 Perkiraan harga jasa jahit: **Rp {harga_min:,.0f} - Rp {harga_max:,.0f}**")