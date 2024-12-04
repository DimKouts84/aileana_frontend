import streamlit as st
from . import databases
import pandas as pd
import plotly.express as px

# A Treemap visualization of the top 10 industries - based on the number of job postings
# the data come from the Neo4J database

def top_industries_treemap():
    df = databases.get_job_categories_data()
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
