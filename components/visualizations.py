import streamlit as st
from components import databases
# import databases as db
import pandas as pd
import plotly.express as px

# A Treemap visualization of the top 10 industries - based on the number of job postings
# the data come from the Neo4J database

def generate_visualization(df,generated_plot_figure):
    df = df
    fig = generated_plot_figure
    st.plotly_chart(fig)
    return

def top_industries_treemap():
    df = db.get_job_categories_data()
    fig = px.treemap(
        df,
        path=["industry"],
        values="job_postings",
        title="Top 10 Industries by Number of Job Postings",
    )
    fig.update_traces(marker=dict(cornerradius=5))
    st.plotly_chart(fig)
    # print(df.columns)
    return

