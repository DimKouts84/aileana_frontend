import streamlit as st

# Section to display the Logo of the project in html
# the relative path of the file is here: static\logo\aileana_logo_full_horizontal.png

    
def top_logo_section():
    with open('static/logo_full_horizontal_light_small.png', 'rb') as f:
        logo_full_horizontal = f.read()
    st.image(logo_full_horizontal)

def side_logo_section():
    with open('static/logo_full_horizontal_light_small.png', 'rb') as f:
        logo_full_horizontal = f.read()
    st.logo(logo_full_horizontal, size="large")

# Hero Section
def hero_section(title, subtitle):
    st.markdown(
            f"""
            <div class="hero-section" style="padding: 50px; text-align: center;">
                <h1 font-size: 63px;">{title}</h1>
                <p font-size: 36px;">{subtitle}</p>
            </div>
            """,
            unsafe_allow_html=True
       )
