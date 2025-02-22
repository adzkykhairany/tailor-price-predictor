import streamlit as st

def show():
    st.title("ℹ️ Tentang Aplikasi")

    st.write(
        """
        Aplikasi ini dirancang untuk membantu pengguna memperkirakan harga jasa jahit berdasarkan beberapa faktor utama, yaitu **model pakaian, jenis bahan, ornamen tambahan, waktu penyelesaian, dan pengalaman penjahit**. Dengan mempertimbangkan aspek-aspek tersebut, aplikasi ini memberikan estimasi harga yang dapat digunakan sebagai referensi sebelum memesan jasa jahit.

        Data yang digunakan dalam aplikasi ini dikembangkan dengan metode **Multiple Linear Regression** untuk memprediksi harga berdasarkan pola yang ditemukan dalam data. Sumber data berasal dari hasil survei terhadap **10 dari 105 pelaku usaha jahit jenis tailor** yang beroperasi di **Pasar Sunan Giri, Rawamangun, Jakarta Timur**.
        """
    )


    st.markdown(
        """
        <div class="copyright">
        © 2025 Athiyya Adzky Khairany
        </div>
        """, 
        unsafe_allow_html=True
    )    