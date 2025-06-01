import streamlit as st

def load_css():
    with open("views/style.css", "r") as f:
        css = f.read()
        st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

# Load CSS from style.css
load_css()

# Header
st.markdown("""
    <div class="header-area">
        <h1 class="header-title">Tentang Aplikasi</h1>
        <p class="header-subtitle">Ringkasan singkat menganai aplikasi perkiraan harga jasa dan estimasi waktu pengerjaan jasa jahit.</p>

    </div>
""", unsafe_allow_html=True)

# Tentang Aplikasi
st.markdown("""
    <div class="section-container">
        <h3 class="section-title"><span>📱</span>Aplikasi</h3>
        <div class="content-card">
            <p class="section-description">
                Aplikasi ini dirancang untuk membantu pengguna memperkirakan <b>harga jasa</b> dan 
                <b>estimasi waktu pengerjaan</b> layanan jahit berdasarkan kombinasi parameter berikut:
            </p>
            <div class="info-grid">
                <div class="info-item">
                    <div>👗<b> Model Pakaian</b><br><span class="item-description">Jenis dan gaya pakaian</span></div>
                </div>
                <div class="info-item">
                    <div>🧵<b> Jenis Bahan</b><br><span class="item-description">Material kain yang digunakan</span></div>
                </div>
                <div class="info-item">
                    <div>💎 <b>Ornamen Tambahan</b><br><span class="item-description">Detail tambahan pada pakaian</span></div>
                </div>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# Teknologi
st.markdown("""
    <div class="section-container">
        <h3 class="section-title"><span>⚙️</span>Teknologi</h3>
        <div class="content-card">
            <p class="section-description">
                Aplikasi ini dikembangkan dengan pendekatan berbasis data dan algoritma prediktif:
            </p>
            <div class="info-grid">
                <div class="info-item">
                    <div>🧮<b> Metode Prediksi</b><br><span class="item-description">Menggunakan algoritma Multiple Linear Regression dengan pendekatan multi-output</span></div>
                </div>
                <div class="info-item">
                    <div>📊<b> Sumber Data</b><br><span class="item-description">Berasal dari 10 penjahit (dari total 105) yang beroperasi di Pasar Sunan Giri, Rawamangun, Jakarta Timur</span></div>
                </div>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# Panduan Penggunaan
st.markdown("""
    <div class="section-container">
        <h3 class="section-title"><span>📝</span>Panduan Penggunaan</h3>
        <div class="content-card">
            <p class="section-description">
                Ikuti langkah-langkah di bawah untuk memperkirakan harga dan estimas waktu pengerjaan layanan jahit pada halaman <a href="/prediction" style="color:#1976d2; text-decoration: none; font-weight: bold;">Prediksi</a>:
            </p>
            <div class="info-grid">
                <div class="info-item">
                    <div><span class="info-number">1</span><b>Pilih model pakaian</b><br><span class="item-description">Tentukan jenis pakaian yang ingin dijahit, seperti kebaya, blus, atau dress sesuai kebutuhan Anda.</span></div>
                </div>
                <div class="info-item">
                    <div><span class="info-number">2</span><b>Tentukan bahan</b><br><span class="item-description">Pilih bahan utama yang diinginkan, misalnya katun, satin, sifon, atau jenis kain lainnya.</span></div>
                </div>
                <div class="info-item">
                    <div><span class="info-number">3</span><b>Tambahkan ornamen</b><br><span class="item-description">Pilih ornamen tambahan seperti bordir, payet, renda, atau pilih tanpa ornamen untuk hasil yang sederhana.</span></div>
                </div>
                <div class="info-item">
                    <div><span class="info-number">4</span><b>Klik "Hitung Perkiraan"</b><br><span class="item-description">Sistem akan menampilkan estimasi harga dan lama pengerjaan berdasarkan pilihan Anda.</span></div>
                </div>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# Footer dengan info kontak yang lebih minimalis
st.markdown("""
    <div class="minimalist-footer">
        <div class="footer-links" style="margin-bottom: 5px;">
            <span>Tailor Predictor v1.0</span>
            <a href="https://github.com/adzkykhairany/tailoring-predictor" target="_blank">GitHub</a>
            <a href="mailto:athiyya.adzky@ui.ac.id">Kontak</a>
        </div>
        <div class="footer-links" style="margin-top: 0;">
            <span>© 2025 Athiyya Adzky Khairany • ML + Streamlit</span>
        </div>
    </div>
""", unsafe_allow_html=True)