import streamlit as st

def hero_section(title, subtitle, logo_path=None):
    logo_html = f'<img src="{logo_path}" style="max-width: 200px; margin-bottom: 20px; display: block; margin-left: auto; margin-right: auto;">' if logo_path else ''
    st.markdown(
            f"""
            <div class="hero-section" style="padding: 50px; text-align: center;">
                {logo_html}
                <h1 style="font-size: 48px;">{title}</h1>
                <p style="font-size: 24px;">{subtitle}</p>
            </div>
            """,
            unsafe_allow_html=True
        )