import streamlit as st
import numpy as np
import joblib
import pandas as pd
import math

def load_css():
    with open("views/style.css", "r") as f:
        css = f.read()
        st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

load_css()

model = joblib.load('models/model_akhir.pkl')

st.title("Prediksi Harga & Waktu")
st.write(
    "Dapatkan estimasi harga jasa jahit dan waktu pengerjaan berdasarkan model pakaian, jenis bahan, dan ornamen tambahan yang anda inginkan.")

# Panduan pengisian dengan design cantik
st.markdown("""
<div class="info-box">
    <div class="info-title"><b>Panduan Pengisian</b></div>
    <div class="info-content">
        <p><span class="info-number">1.</span><span style="margin-right:6px;"></span>Isi semua kolom input sesuai kebutuhan jahitan Anda</p>
        <p><span class="info-number">2.</span><span style="margin-right:6px;"></span>Klik tombol<span style="margin-right:6px;"></span><b>Hitung Perkiraan</b><span style="margin-right:6px;"></span>untuk estimasi biaya dan waktu</p>
    </div>
</div>
""", unsafe_allow_html=True)

if 'form_submitted' not in st.session_state:
    st.session_state.form_submitted = False

def round_to_nearest(value, base=500):
    return round(value / base) * base

def predict(model, model_input, bahan_input, ornamen_input):
    df_input = pd.DataFrame([{
        'model': model_input,
        'bahan': bahan_input,
        'ornamen': ornamen_input
    }])

    waktu_mean, harga_mean = model.predict(df_input)[0]
    return round(waktu_mean), round_to_nearest(harga_mean)

def handle_submit():
    st.session_state.form_submitted = True

with st.form("input_form", clear_on_submit=False):
    model_input = st.selectbox(
        "👗 Model Pakaian", 
        ["Pilih Model Pakaian", "Kebaya Tradisional", "Kebaya Modern", "Blus", "Midi Dress", "Maxi Dress"],
        index=0,
        help="Pilih model pakaian yang sesuai dengan kebutuhan Anda."
    )

    if st.session_state.form_submitted and model_input == "Pilih Model Pakaian":
        st.markdown('<p class="error-message">⚠ Harap pilih model pakaian.</p>', unsafe_allow_html=True)

    bahan_input = st.selectbox(
        "🧵 Jenis Bahan", 
        ["Pilih Jenis Bahan", "Katun", "Sutra", "Brokat", "Sifon", "Satin"],
        index=0,
        help="Pilih jenis bahan yang akan digunakan."
    )

    if st.session_state.form_submitted and bahan_input == "Pilih Jenis Bahan":
        st.markdown('<p class="error-message">⚠ Harap pilih jenis bahan.</p>', unsafe_allow_html=True)

    ornamen_input = st.selectbox(
        "✨ Ornamen Tambahan", 
        ["Pilih Ornamen", "Tanpa Ornamen", "Bordir Kecil", "Bordir Sedang", "Bordir Besar", "Bordir Tempel", 
         "Renda", "Opneisel Tertutup", "Opneisel Terbuka", "Payet Aksen Kecil", "Payet Aksen Sedang", 
         "Payet Aksen Besar", "Payet Motif Sedang", "Payet Motif Besar"],
        index=0,
        help="Pilih ornamen tambahan untuk pakaian Anda."
    )

    if st.session_state.form_submitted and ornamen_input == "Pilih Ornamen":
        st.markdown('<p class="error-message">⚠ Harap pilih ornamen tambahan.</p>', unsafe_allow_html=True)

    submit = st.form_submit_button(
        "Hitung Perkiraan", 
        help="Klik untuk menghitung estimasi biaya dan waktu.",
        use_container_width=True, 
        type="primary",
        on_click=handle_submit
    )

if st.session_state.form_submitted:
    errors = {}
    
    if model_input == "Pilih Model Pakaian":
        errors["model"] = True
    if bahan_input == "Pilih Jenis Bahan":
        errors["bahan"] = True
    if ornamen_input == "Pilih Ornamen":
        errors["ornamen"] = True

    if not errors:
        mapping_model = {
            "Kebaya Tradisional": "Kebaya Tradisional", 
            "Kebaya Modern": "Kebaya Modern", 
            "Blus": "Blus", 
            "Midi Dress": "Midi Dress", 
            "Maxi Dress": "Maxi Dress"
        }
        mapping_bahan = {
            "Katun": "Katun", 
            "Sutra": "Sutra", 
            "Brokat": "Brokat", 
            "Sifon": "Sifon", 
            "Satin": "Satin"
        }
        mapping_ornamen = {
            "Tanpa Ornamen": "None", 
            "Bordir Kecil": "Bordir Kecil", 
            "Bordir Sedang": "Bordir Sedang", 
            "Bordir Besar": "Bordir Besar", 
            "Bordir Tempel": "Bordir Tempel", 
            "Renda": "Renda", 
            "Opneisel Tertutup": "Opneisel Tertutup", 
            "Opneisel Terbuka": "Opneisel Terbuka", 
            "Payet Aksen Kecil": "Payet Aksen Kecil", 
            "Payet Aksen Sedang": "Payet Aksen Sedang", 
            "Payet Aksen Besar": "Payet Aksen Besar", 
            "Payet Motif Sedang": "Payet Motif Sedang", 
            "Payet Motif Besar": "Payet Motif Besar"
        }

        with st.spinner("⏳ Sedang menghitung estimasi..."):
            waktu, harga = predict(
                model=model,
                model_input=mapping_model[model_input],
                bahan_input=mapping_bahan[bahan_input],
                ornamen_input=mapping_ornamen[ornamen_input]
            )
            st.session_state.form_submitted = False

        st.markdown(
            f"""
            <div style="background-color:#f0f8ff;padding:10px;border-radius:5px;">
                🕒 <b>Estimasi waktu pengerjaan:</b> {waktu} hari<br>
                💸 <b>Estimasi harga jasa:</b> Rp{harga:,}
            </div>
            """,
            unsafe_allow_html=True
        )