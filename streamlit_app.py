import streamlit as st
import app_modules as app

# read css file
def load_css():
    with open("app_modules/style.css", "r") as f:
        css = f.read()
        st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

# load css
load_css()

# sidebar
st.sidebar.title("🔖 Menu")
page = st.sidebar.radio("Pilih Halaman", ["Tentang Aplikasi", "Prediksi Harga"])

if page == "Prediksi Harga":
    app.show_prediction()
elif page == "Tentang Aplikasi":
    app.show_about()