import streamlit as st

# read css file
def load_css():
    with open("views/style.css", "r") as f:
        css = f.read()
        st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

# load css
load_css()

# sidebar
about_page = st.Page(
    page="views/about.py",
    title="Tentang Aplikasi",
    icon=":material/info:"
)

prediction_page = st.Page(
    page="views/prediction.py",
    title="Prediksi",
    icon=":material/batch_prediction:",
    default=True
) 

catalog_page = st.Page(
    page="views/catalog.py",
    title="Model Pakaian",
    icon=":material/laundry:"
)

pg = st.navigation(pages=[prediction_page, catalog_page, about_page])
pg.run()

st.markdown(
    "<hr><div class='copyright'>© 2025 Athiyya Adzky Khairany.</div>",
    unsafe_allow_html=True
)