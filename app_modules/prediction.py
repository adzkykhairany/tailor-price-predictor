import streamlit as st
import numpy as np
import joblib
import pandas as pd

# Load CSS for custom styling first to memastikan semua styling diterapkan
def load_css():
    with open("app_modules/style.css", "r") as f:
        css = f.read()
        st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

load_css()

# Load models and statistics from .pkl
loaded = joblib.load('models/model_akhir.pkl')
model = loaded['model_predict']  # Extract the model from the dictionary

# Title dan deskripsi
st.title("Model Prediksi")
st.write(
    "Dapatkan estimasi harga jasa jahit dan waktu pengerjaan berdasarkan model pakaian, jenis bahan, dan ornamen tambahan yang anda inginkan.")

# Sidebar Panduan
st.sidebar.header(":material/keep: Panduan Pengisian")
st.sidebar.info(
    ":material/looks_one: Isi semua kolom input sesuai dengan kebutuhan jahitan Anda.\n\n"
    ":material/looks_two: Klik tombol **Hitung Perkiraan** untuk mendapatkan estimasi biaya dan waktu."
)

# Initialize session states
if 'form_submitted' not in st.session_state:
    st.session_state.form_submitted = False
if 'prediction_done' not in st.session_state:
    st.session_state.prediction_done = False

# Function to predict price
def predict_price(model, model_input, bahan_input, ornamen_input):
    # Buat DataFrame input
    df_input = pd.DataFrame([{
        'model': model_input,
        'bahan': bahan_input,
        'ornamen': ornamen_input
    }])

    # Prediksi
    pred = model.predict(df_input)[0]
    waktu_mean = pred[0]
    harga_mean = pred[1]

    # Format hasil
    return int(round(waktu_mean)), int(round(harga_mean))

# Function to handle form submission
def handle_submit():
    st.session_state.form_submitted = True

with st.form("input_form"):
    model_input = st.selectbox(
        "👗 Model Pakaian", 
        ["Pilih Model Pakaian", "Kebaya Tradisional", "Kebaya Modern", "Blus", "Midi Dress", "Maxi Dress"],
        index=0,
        help="Pilih model pakaian yang sesuai dengan kebutuhan Anda."
    )
    # Display error only if form was submitted and input is invalid
    if st.session_state.form_submitted and model_input == "Pilih Model Pakaian":
        st.markdown('<p class="error-message">⚠ Harap pilih model pakaian.</p>', unsafe_allow_html=True)

    bahan_input = st.selectbox(
        "🧵 Jenis Bahan", 
        ["Pilih Jenis Bahan", "Katun", "Sutra", "Brokat", "Sifon", "Satin"],
        index=0,
        help="Pilih jenis bahan yang akan digunakan."
    )
    # Display error only if form was submitted and input is invalid
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
    # Display error only if form was submitted and input is invalid
    if st.session_state.form_submitted and ornamen_input == "Pilih Ornamen":
        st.markdown('<p class="error-message">⚠ Harap pilih ornamen tambahan.</p>', unsafe_allow_html=True)

    submit = st.form_submit_button(
        "Hitung Perkiraan", 
        help="Klik untuk menghitung estimasi biaya dan waktu.",
        use_container_width=True, 
        type="primary",
        on_click=handle_submit
    )

# Process form submission - move outside the form
if st.session_state.form_submitted and not st.session_state.prediction_done:
    errors = {}
    
    # Check for errors
    if model_input == "Pilih Model Pakaian":
        errors["model"] = True
    if bahan_input == "Pilih Jenis Bahan":
        errors["bahan"] = True
    if ornamen_input == "Pilih Ornamen":
        errors["ornamen"] = True

    if not errors:
        # Mapping untuk input pengguna
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

        # Process prediction
        with st.spinner("⏳ Sedang menghitung estimasi..."):
            waktu, harga = predict_price(
                model=model,
                model_input=mapping_model[model_input],
                bahan_input=mapping_bahan[bahan_input],
                ornamen_input=mapping_ornamen[ornamen_input]
            )
            # Mark prediction as done to prevent multiple runs
            st.session_state.prediction_done = True

        st.markdown(
            f"""
            <div style="background-color:#f0f8ff;padding:10px;border-radius:5px;">
                🕒 <b>Estimasi waktu pengerjaan:</b> {waktu} hari<br>
                💸 <b>Estimasi harga jasa:</b> Rp{harga:,}
            </div>
            """,
            unsafe_allow_html=True
        )