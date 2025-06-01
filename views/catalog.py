import streamlit as st
from PIL import Image
import os

def load_css():
    with open("views/style.css", "r") as f:
        css = f.read()
        st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

load_css()

# Header
st.markdown("""
    <div class="header-area">
        <h1 class="header-title">Referensi Pakaian</h1>
        <p class="header-subtitle">Contoh referensi model pakaian, jenis bahan, dan ornamen yang dapat dipadukan dalam pemilihan</p>

    </div>
""", unsafe_allow_html=True)

# Fungsi untuk menampilkan gambar dengan kualitas HD
def display_hd_image(image_path):
    try:
        if os.path.exists(image_path):
            img = Image.open(image_path)
            return img
        else:
            return None
    except Exception as e:
        st.error(f"Error membaca gambar: {e}")
        return None

model_data = [
    {
        "category": "Model Pakaian",
        "subcategories": [
            {
                "name": "Kebaya",
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
                "name": "Dress",
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
                "name": "Blus",
                "models": [
                    {
                        "name": "Blus",
                        "image": "images/blus.png",
                        "description": "Atasan wanita yang dapat dipadukan dengan rok atau celana, tersedia dalam berbagai gaya dan potongan. Cocok digunakan untuk acara formal, semi-formal, maupun kasual sehari-hari."
                    }
                ]
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
for category in model_data:    # Tambahkan margin lebih besar untuk kategori selain yang pertama
    if category != model_data[0]:
        # Add more space before "Jenis Bahan" category
        if category['category'] == "Jenis Bahan":
            st.markdown("<div style='margin-top: 30px;'></div>", unsafe_allow_html=True)
        else:
            st.markdown("<div style='margin-top: 15px;'></div>", unsafe_allow_html=True)
    else:
        st.markdown("<div style='margin-top: 5px;'></div>", unsafe_allow_html=True)
    
    # Add ID for Model Pakaian category to target with CSS
    if category['category'] == "Model Pakaian":
        st.markdown(f"<div id='model-pakaian' class='simple-category'>{category['category']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='simple-category'>{category['category']}</div>", unsafe_allow_html=True)
    
    if category.get("subcategories"):
        # Ini adalah "Model Pakaian" dengan subkategori (tanpa judul subkategori)
        for subcategory in category["subcategories"]:
            # Hapus margin untuk mengurangi jarak antara kategori dan gambar
            # Subkategori title dihapus
            
            col_count = max(2, len(subcategory["models"]))
            cols = st.columns(col_count)
            
            for i, model in enumerate(subcategory["models"]):
                with cols[i]:
                    img = display_hd_image(model["image"])
                    if img:                    
                        st.markdown(f"<div class='img-wrapper'>", unsafe_allow_html=True)
                        st.image(img, use_container_width=True, output_format="PNG")
                        st.markdown("</div>", unsafe_allow_html=True)
                    else:                
                        st.error(f"Gambar tidak ditemukan: {model['image']}")
                    
                    st.markdown(f"<p class='model-name'>{model['name']}</p>", unsafe_allow_html=True)
                    st.markdown(f"<p class='model-description justified-text'>{model['description']}</p>", unsafe_allow_html=True)
            
            # Tambahkan pemisah setelah setiap subkategori kecuali yang terakhir
            if subcategory != category["subcategories"][-1]:
                st.markdown("<hr style='margin: 15px 0; border: 1px solid #e2e8f0; opacity: 0.3;'>", unsafe_allow_html=True)
    
    elif category.get("is_info", False):
        # Tidak perlu margin tambahan karena sudah ada dari category header
        for i, item in enumerate(category["info_items"]):
            # Menambahkan margin yang sangat kecil untuk item pertama
            if i == 0:
                st.markdown("<div style='margin-top: 2px;'></div>", unsafe_allow_html=True)
            else:
                st.markdown("<div style='margin-top: 5px;'></div>", unsafe_allow_html=True)
                
            with st.container():
                st.markdown(
                    f"""
                    <div class="catalog-item-container">
                        <p class="catalog-item-name">{item['name']}</p>
                        <p class="catalog-item-description">{item['description']}</p></div>
                    """,
                    unsafe_allow_html=True)
    else:
        col_count = max(2, len(category["models"]))
        cols = st.columns(col_count)
        
        for i, model in enumerate(category["models"]):
            with cols[i]:
                img = display_hd_image(model["image"])
                if img:                    
                    st.markdown(f"<div class='img-wrapper'>", unsafe_allow_html=True)
                    st.image(img, use_container_width=True, output_format="PNG")
                    st.markdown("</div>", unsafe_allow_html=True)
                else:                    
                    st.error(f"Gambar tidak ditemukan: {model['image']}")
                
                st.markdown(f"<p class='model-name'>{model['name']}</p>", unsafe_allow_html=True)
                st.markdown(f"<p class='model-description justified-text'>{model['description']}</p>", unsafe_allow_html=True)