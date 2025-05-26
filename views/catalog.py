import streamlit as st
from PIL import Image
import os

def load_css():
    with open("views/style.css", "r") as f:
        css = f.read()
        st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

load_css()

st.markdown("<h1 class='catalog-title'>Referensi Model Pakaian</h1>", unsafe_allow_html=True)
st.markdown("<p class='catalog-subtitle'>Contoh referensi model pakaian, jenis bahan, dan ornamen yang dapat dipadukan dalam pemilihan.</p>", unsafe_allow_html=True)

# Fungsi untuk menampilkan gambar dengan kualitas HD
def display_hd_image(image_path):
    try:
        if os.path.exists(image_path):
            img = Image.open(image_path)
            # Menampilkan gambar asli tanpa resizing otomatis
            return img
        else:
            return None
    except Exception as e:
        st.error(f"Error membaca gambar: {e}")
        return None

model_data = [
    {
        "category": "Kebaya",
        "models": [
            {
                "name": "Kebaya Tradisional",
                "image": "images/kebaya_tradisional.png",
                "description": "Model kebaya klasik dengan desain tradisional, biasa digunakan untuk acara formal dan adat."
            },
            {
                "name": "Kebaya Modern",
                "image": "images/kebaya_modern.png",
                "description": "Kebaya dengan sentuhan modern, desain lebih variatif dan siluet yang lebih kontemporer namun tetap elegan."
            }
        ]
    },
    {
        "category": "Dress",
        "models": [
            {
                "name": "Midi Dress",
                "image": "images/midi_dress.png", 
                "description": "Gaun dengan panjang selutut atau betis, sering digunakan untuk acara semi-formal dan pesta."
            },
            {
                "name": "Maxi Dress",
                "image": "images/maxi.jpg",
                "description": "Gaun panjang hingga mata kaki dengan siluet yang memanjang, cocok untuk acara formal dan semi-formal."
            }
        ]
    },
    {
        "category": "Blus",
        "models": [
            {
                "name": "Blus",
                "image": "images/blus.png",
                "description": "Atasan wanita yang dapat dipadukan dengan rok atau celana, tersedia dalam berbagai gaya dan potongan. Cocok digunakan untuk acara formal, semi-formal, maupun kasual sehari-hari."
            }
        ]
    },
    {
        "category": "Jenis Bahan",
        "is_info": True,
        "info_items": [
            {
                "name": "Katun",
                "description": "Kain yang terbuat dari serat kapas, memiliki tekstur lembut, ringan, dan menyerap keringat. Cocok untuk pakaian sehari-hari dan iklim tropis."
            },
            {
                "name": "Sutra",
                "description": "Bahan mewah dengan kilau alami dan tekstur halus. Memiliki ketahanan tinggi dan sangat nyaman dipakai, umumnya digunakan untuk pakaian formal dan acara khusus."
            },
            {
                "name": "Brokat",
                "description": "Kain dengan tekstur timbul dan motif bordir yang indah. Sering digunakan untuk busana pesta, kebaya, dan gaun formal berkat tampilannya yang mewah."
            },
            {
                "name": "Sifon",
                "description": "Bahan tipis, ringan, dan transparan dengan jatuhnya yang lembut dan mengalir. Ideal untuk busana lapisan atau gaun yang membutuhkan efek melayang."
            },
            {
                "name": "Satin",
                "description": "Kain dengan permukaan halus dan mengkilap di satu sisi. Memberikan kesan mewah dan elegan, sering digunakan untuk gaun formal dan busana pesta."
            }
        ]
    },
    {
        "category": "Ornamen Tambahan",
        "is_info": True,
        "info_items": [
            {
                "name": "Bordir",
                "description": "Teknik hiasan dengan benang di atas kain menggunakan jarum atau mesin bordir. Dapat berupa motif bunga, daun, geometris, atau abstrak dengan berbagai ukuran dan tingkat kompleksitas."
            },
            {
                "name": "Payet",
                "description": "Hiasan berupa manik-manik kecil yang dijahit pada kain untuk memberikan efek berkilau. Bisa berupa aksen sederhana atau motif yang menutupi sebagian besar kain."
            },
            {
                "name": "Opneisel",
                "description": "Teknik jahit yang membentuk barisan lipatan rapi pada kain, dengan arah horizontal, vertikal, atau diagonal, untuk menambah dimensi dan tekstur halus pada pakaian."
            },
            {
                "name": "Renda",
                "description": "Kain jaring halus dan rumit yang dibuat dari benang katun, sutra, atau sintetis. Biasanya dipasang di tepi kain atau sebagai lapisan untuk menambah kesan feminin dan elegan."
            }
        ]
    }
]

# Tampilkan model per kategori
for category in model_data:
    # Adding less vertical space above categories
    st.markdown("<div style='margin-top: 5px;'></div>", unsafe_allow_html=True)
    st.markdown(f"<div class='simple-category'>{category['category']}</div>", unsafe_allow_html=True)
    
    # Cek apakah kategori adalah info (bahan atau ornamen)
    if category.get("is_info", False):
        # Tambahkan spasi di atas kategori info
        st.markdown("<div style='margin-top: 15px;'></div>", unsafe_allow_html=True)
        
        # Tampilkan info item dalam format list card
        for i, item in enumerate(category["info_items"]):
            # Tambahkan spasi tambahan sebelum item pertama
            if i == 0:
                st.markdown("<div style='margin-top: 10px;'></div>", unsafe_allow_html=True)
                
            with st.container():
                st.markdown(f"""
                <div style="background-color: #f9f9f9; padding: 12px 15px; border-radius: 5px; margin-bottom: 10px;">
                    <p style="font-weight: 600; margin: 0 0 6px 0; color: #333; font-size: 16px;">{item['name']}</p>
                    <p style="margin: 0; font-size: 14px; color: #555; text-align: justify;">{item['description']}</p>
                </div>
                """, unsafe_allow_html=True)
    else:
        # Buat kolom berdasarkan jumlah model dalam kategori, minimal 2 kolom
        col_count = max(2, len(category["models"]))
        cols = st.columns(col_count)
        
        for i, model in enumerate(category["models"]):
            with cols[i]:
                st.markdown(f"<div class='image-container'>", unsafe_allow_html=True)
                
                # Tampilkan gambar dengan kualitas HD
                img = display_hd_image(model["image"])
                if img:
                    st.markdown(f"<div class='img-wrapper'>", unsafe_allow_html=True)
                    # Gunakan quality=100 untuk memastikan kualitas maksimum
                    st.image(img, use_container_width=True, output_format="PNG")
                    st.markdown("</div>", unsafe_allow_html=True)
                else:
                    st.error(f"Gambar tidak ditemukan: {model['image']}")
                
                # Tampilkan nama dan deskripsi model dengan desain yang dipercantik
                st.markdown(f"<p class='model-name'>{model['name']}</p>", unsafe_allow_html=True)
                st.markdown(f"<p class='model-description justified-text'>{model['description']}</p>", unsafe_allow_html=True)
                
                st.markdown("</div>", unsafe_allow_html=True)
    
    # Using a slimmer horizontal line with less margin for category separation
    st.markdown("<hr style='margin: 10px 0; opacity: 0.1;'>", unsafe_allow_html=True)