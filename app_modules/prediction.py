import streamlit as st
import numpy as np
import joblib
import pandas as pd

# Load models
rf_model = joblib.load('models/model.pkl')

def load_css():
    with open("app_modules/style.css", "r") as f:  # Pastikan path ke style.css benar
        css = f.read()
        st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

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
            model = st.selectbox("👗 Model Pakaian", 
                                         ["Pilih Model Pakaian", "Kebaya Tradisional", "Kebaya Modern", "Blus", "Midi Dress", "Maxi Dress"],
                                         index=0)
            if model == "Pilih Model Pakaian":
                errors["model"] = "⚠ Harap pilih model pakaian."

        with col2:
            bahan = st.selectbox("🧵 Jenis Bahan", 
                                       ["Pilih Jenis Bahan", "Katun", "Sutra", "Brokat", "Sifon", "Satin"],
                                       index=0)
            if bahan == "Pilih Jenis Bahan":
                errors["bahan"] = "⚠ Harap pilih jenis bahan."

        col3, col4 = st.columns(2)
        with col3:
            ornamen = st.selectbox("✨ Ornamen Tambahan", 
                                            ["Pilih Ornamen", "Tanpa Ornamen", "Bordir", "Renda", "Lipitan", "Payet"],
                                            index=0)
            if ornamen == "Pilih Ornamen":
                errors["ornamen"] = "⚠ Harap pilih ornamen tambahan."

        with col4:
            waktu_pengerjaan = st.number_input("⏳ Waktu Penyelesaian (dalam hari)", min_value=1, step=1)
        
        # col5 = st.columns(1)[0]
        # with col5:
        #     model_pilih = st.selectbox("Pilih Model", ["Multiple Linear Regression", "Random Forest"])
        
        _, col_submit = st.columns([2, 1])
        with col_submit:
            submit = st.form_submit_button("🎯 Hitung Perkiraan Harga")

    # show error
    if submit:
        with col1:
            if "model" in errors:
                st.markdown(f'<p class="error-message">{errors["model"]}</p>', unsafe_allow_html=True)
        with col2:
            if "bahan" in errors:
                st.markdown(f'<p class="error-message">{errors["bahan"]}</p>', unsafe_allow_html=True)
        with col3:
            if "ornamen" in errors:
                st.markdown(f'<p class="error-message">{errors["ornamen"]}</p>', unsafe_allow_html=True)
        with col4:
            if "waktu_pengerjaan" in errors:
                st.markdown(f'<p class="error-message">{errors["waktu_pengerjaan"]}</p>', unsafe_allow_html=True)

        if not errors:
            # Mapping untuk input pengguna
            mapping_model = {"Kebaya Tradisional": "kebaya tradisional", "Kebaya Modern": "kebaya modern", "Blus": "blus", "Midi Dress": "midi dress", "Maxi Dress": "maxi dress"}
            mapping_bahan = {"Katun": "katun", "Sutra": "sutra", "Brokat": "brokat", "Sifon": "sifon", "Satin": "satin"}
            mapping_ornamen = {"Tanpa Ornamen": "none", "Bordir": "bordir", "Renda": "renda", "Lipitan": "opneisel", "Payet": "payet"}

            # Input untuk model prediksi
            X_input = pd.DataFrame([{
                "model": mapping_model[model],
                "bahan": mapping_bahan[bahan],
                "ornamen": mapping_ornamen[ornamen],
                "waktu_pengerjaan": waktu_pengerjaan
            }])
                
            pred = rf_model.predict(X_input)[0]
            rentang = (int(pred - 100000), int(pred + 100000))
            st.success(f"💸 Estimasi harga jasa jahit: Rp{rentang[0]:,} - Rp{rentang[1]:,}")