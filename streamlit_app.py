import streamlit as st

# read css file
def load_css():
    with open("app_modules/style.css", "r") as f:
        css = f.read()
        st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

# load css
load_css()

# sidebar
about_page = st.Page(
    page="app_modules/about.py",
    title="Tentang Aplikasi",
    icon=":material/info:",
    default=True
)

prediction_page = st.Page(
    page="app_modules/prediction.py",
    title="Prediksi",
    icon=":material/apparel:",
) 

pg = st.navigation(pages=[about_page, prediction_page])
pg.run()

# footer
st.markdown(
    "<hr><div class='copyright'>© 2025 Athiyya Adzky Khairany.</div>",
    unsafe_allow_html=True
)