import streamlit as st
from PIL import Image
import os

def load_css():
    with open("views/style.css", "r") as f:
        css = f.read()
        st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

load_css()

st.markdown("<h1 class='catalog-title'>Referensi Model Pakaian</h1>", unsafe_allow_html=True)
st.markdown("<p class='catalog-subtitle'>Referensi model pakaian yang tersedia pada model prediksi harga dan waktu pengerjaan.</p>", unsafe_allow_html=True)

model_data = [
    {
        "category": "Kebaya",
        "models": [
            {
                "name": "Kebaya Tradisional",
                "image": "images/kebaya_tradisional.png",
                "description": "Model kebaya klasik dengan potongan longgar dan desain tradisional, biasa digunakan untuk acara formal dan adat."
            },
            {
                "name": "Kebaya Modern",
                "image": "images/kebaya_modern.png",
                "description": "Kebaya dengan sentuhan modern, desain lebih ramping dan siluet yang lebih kontemporer namun tetap elegan."
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
                "image": "images/maxi_dress.png",
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
    }
]

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

# Tampilkan model per kategori
for category in model_data:
    # Adding less vertical space above categories
    st.markdown("<div style='margin-top: 5px;'></div>", unsafe_allow_html=True)
    st.markdown(f"<div class='simple-category'>{category['category']}</div>", unsafe_allow_html=True)
    
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
            st.markdown(f"<p class='model-description; justified-text'>{model['description']}</p>", unsafe_allow_html=True)
            
            st.markdown("</div>", unsafe_allow_html=True)
    
    # Using a slimmer horizontal line with less margin for category separation
    st.markdown("<hr style='margin: 10px 0; opacity: 0.1;'>", unsafe_allow_html=True)