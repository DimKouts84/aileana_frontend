import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Analytics & Insights",
    page_icon="🔎",
    layout="wide",
    initial_sidebar_state="expanded",
)

from components import sidebar_auth, visualizations as viz, widgets
import streamlit.components.v1 as components

# Initialize auth in sidebar
user_email = sidebar_auth.init_sidebar_auth()

# Rest of your page code
if not user_email:
    # Show page content for authenticated users
    st.warning("Please login to access this page")
    st.write(f"")
    
    # Say enjoy to users 
    st.write("---") # Division Line
    st.caption("Made with ❤️ by [Dimitris Koutsomichalis](https://github.com/DimKouts84/)")
    
    st.stop()
elif user_email:
    widgets.hero_section(
        title="Analytics & Insights",
        subtitle="📊 🔎 Explore the data and gain insights into the job market.",
    )

    st.write(" ") # Space
    
    # ~~~~~~~~~~~~~~~~~~~~~~~~ Visualizations based on user Input ~~~~~~~~~~~~~~~~~~~~~~~~
    # Job analytics based on user input
    with st.container(border = True):
        st.write("### Analytics based on your interests")
        with st.container():
            st.write("**Type a job title and see the top skills and industries for this job.**")
            st.write(" ")
            job_title = st.text_input("Enter a job title below:", "Accountant")
            
            # Create two columns
            col1, col2 = st.columns(2)
            
            with col1:
                viz.top_skills_for_job_title(job_title, color_scheme='lightgreen')
                
            with col2:
                viz.top_industries_for_job_title(job_title, color_scheme='lightgreen')
    
        st.write("---") # Division Line
        
        # Skills analytics based on user input
        with st.container():
            st.write("**Type a skill and see the top job titles and industries for this skill.**")
            st.write(" ")
            skill = st.text_input("Enter a skill below:", "English")
            
            # Create two columns
            col1, col2 = st.columns(2)
            
            with col1:
                viz.top_job_titles_for_skill(skill, color_scheme='lightblue')
                
            with col2:
                viz.top_industries_for_skill(skill, color_scheme='lightblue')
    
        st.write("---") # Division Line
            
        # Degree analytics based on user input
        with st.container():
            st.write("**Type a degree and see the top job titles and industries for this degree.**")
            st.write(" ")
            degree = st.text_input("Enter a degree below:", "Accounting")
            
            # Create two columns
            col1, col2 = st.columns(2)
            
            with col1:
                viz.top_job_titles_for_degree(degree, color_scheme='lightcoral')
                
            with col2:
                viz.top_industries_for_degree(degree, color_scheme='lightcoral')
    
    st.write(" ") # Space
    st.write(" ") # Space
    st.write(" ") # Space
    st.write(" ") # Space
        
    # ~~~~~~~~~~~~~~~~~~~~~~~~ "TOP" analytics Section accross industries and job titles ~~~~~~~~~~~~~~~~~~~~~~~~   
    with st.container(border = True):
        st.write("### Data Analytics Across Industries, Jobs and Skills")

        st.write("---") # Division Line
        with st.container():
            col3, col4 = st.columns(2)
            with col3:
                viz.top_job_titles_pie_chart()
            with col4:
                viz.top_skills_pie_chart()
                
        st.write("---") # Division Line
        with st.container():
            col5, col6 = st.columns(2)
            with col5:
                viz.job_titles_treemap()
            with col6:
                viz.standardized_industries_treemap()
                
        st.write("---")
        with st.container():
            col7, col8 = st.columns(2)
            with col7:
                viz.top_industries_skills_scatter()
            with col8:
                viz.top_job_titles_industries_skills_scatter()
                        
                
        st.write("---") # Division Line
        with st.container():
            viz.top_job_titles_and_industry_bubble_chart()
            st.write("---") # Division Line
            viz.top_job_titles_skills_scatter()
 

    # ~~~~~~~~~~~~~~~~~~~~~~~~ Footer ~~~~~~~~~~~~~~~~~~~~~~~~   
    st.write("---") # Division Line
    st.caption("Made with ❤️ by [Dimitris Koutsomichalis](https://github.com/DimKouts84/)")
