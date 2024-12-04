import streamlit as st

def hero_section(title, subtitle):
    st.markdown(
            f"""
            <div class="hero-section" style="padding: 40px; text-align: center;">
                <h1 font-size: 48px;">{title}</h1>
                <p font-size: 24px;">{subtitle}</p>
            </div>
            """,
            unsafe_allow_html=True
        )
