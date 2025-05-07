import streamlit as st

def load_css():
    with open("app_modules/style.css", "r") as f:
        css = f.read()
        st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

st.title("Tentang Aplikasi")
st.markdown('<div class="justified-text">Aplikasi ini dirancang untuk membantu pengguna memperkirakan harga jasa dan estimasi waktu pengerjaan layanan jahit, berdasarkan beberapa faktor utama, yaitu <b>Model Pakaian, Jenis Bahan, Ornamen Tambahan</b>. Dengan mempertimbangkan aspek-aspek tersebut, aplikasi ini memberikan estimasi harga dan waktu pengerjaan yang dapat digunakan sebagai referensi sebelum menggunakan jasa jahit.', unsafe_allow_html=True)

st.markdown('<div><br></div>', unsafe_allow_html=True)

st.markdown('<div class="justified-text">Data yang digunakan dalam aplikasi ini dikembangkan menggunakan metode <b>Multiple Linear Regression</b> dengan pendekatan <i>multi-output</i>. Model ini memungkinkan prediksi simultan terhadap harga dan waktu pengerjaan berdasarkan pola yang ditemukan dalam data. Sumber data berasal dari hasil survei terhadap <b>10 dari 105 pelaku usaha jahit jenis tailor</b> yang beroperasi di <b>Pasar Sunan Giri, Rawamangun, Jakarta Timur</b>.</div>', unsafe_allow_html=True)