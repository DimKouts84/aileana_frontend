import streamlit as st
from components import databases as db
# import databases as db
import pandas as pd
import plotly.express as px

# Visualization function for the LLM chatbot
def generate_visualization(df,generated_plot_figure):
    df = df
    fig = generated_plot_figure
    st.plotly_chart(fig)
    return

# Visualization function for the Home Page
def top_industries_treemap(): 
    query = """
        MATCH (i:INDUSTRY)-[:POSTS]->(j:JOB)
        RETURN i.industry_name AS industry, COUNT(j) AS job_postings
        ORDER BY job_postings DESC
        LIMIT 10
        """
    df = db.execute_query(query)
    fig = px.treemap(
        df,
        path=["industry"],
        values="job_postings",
        title="Top 10 Industries by Number of Job Postings",
        color_discrete_sequence=px.colors.sequential.Blues_r
        )
    fig.update_traces(marker=dict(cornerradius=5))
    st.plotly_chart(fig)
    # print(df.columns)
    return

''' ~~~~~~~~~~~~~~~~~~~~~~~~ Visualization function for the Analytics & Insights Page ~~~~~~~~~~~~~~~~~~~~~~~~ ''' 

# ~~~~~~~~~~~~~~~~~~~~~~~~ Analytics Charts with user input data ~~~~~~~~~~~~~~~~~~~~~~~~

# ~~~~~~~~ Based on Job title ~~~~~~~~
# A user can type a job title and see the top 10 skills required for that job title
def top_skills_for_job_title(job_title, color_scheme='lightgreen'):
    query = f"""
        MATCH (j:JOB)
        WHERE toLower(j.job_title) CONTAINS toLower('{job_title}')
        MATCH (j)-[r]->(s:SKILL)
        RETURN s.skill_name AS skill, COUNT(*) AS skill_count
        ORDER BY skill_count DESC
        LIMIT 10
        """
    df = db.execute_query(query)
    
    if df.empty:
        st.warning("No matching jobs found. Try a different search term.")
        return
        
    fig = px.line(
        df,
        x='skill',
        y='skill_count',
        title=f"Top Skills for '{job_title}'",
        color_discrete_sequence=px.colors.sequential.Mint,
    )
    
    fig.update_layout(
        xaxis_title="Skills",
        yaxis_title="Frequency",
        xaxis={'categoryorder':'total descending'},
        bargap=0.2
    )
    
    st.plotly_chart(fig, use_container_width=True)
    return

# A user can type a job title and see the top 10 industries that require that job title
def top_industries_for_job_title(job_title, color_scheme='lightgreen'):
    query = f"""
        MATCH (j:JOB)
        WHERE toLower(j.job_title) CONTAINS toLower('{job_title}')
        MATCH (j)<-[:POSTS]-(i:INDUSTRY)<-[:BELONGS_TO]-(in:INDUSTRY_NAME)
        RETURN in.industry_name AS industry, COUNT(*) AS job_count
        ORDER BY job_count DESC
        LIMIT 10
        """
    df = db.execute_query(query)
    
    if df.empty:
        st.warning("No matching jobs found. Try a different search term.")
        return
        
    fig = px.line(
        df,
        x='industry',
        y='job_count',
        title=f"Top Industries for '{job_title}'",
        color_discrete_sequence=px.colors.sequential.Mint
    )
    
    fig.update_layout(
        xaxis_title="Industries",
        yaxis_title="Number of Jobs",
        xaxis={'categoryorder':'total descending'},
        bargap=0.2
    )
    
    st.plotly_chart(fig, use_container_width=True)
    return


# A user can type a degree and see the top 10 job titles that require that degree
def top_job_titles_for_degree(degree_name, color_scheme='lightgreen'):
    query = f"""
        MATCH (d:ACADEMIC_DEGREE)
        WHERE toLower(d.degree_field) CONTAINS toLower("{degree_name}")
        MATCH (d)<-[:REQUIRES]-(j:JOB)
        RETURN j.standardized_occupation AS job_title, 
               COUNT(*) AS job_count
        ORDER BY job_count DESC
        LIMIT 10
        """
    df = db.execute_query(query)
    
    if df.empty:
        st.warning("No matching degrees found. Try a different search term.")
        return
        
    fig = px.bar(
        df,
        x='job_title',
        y='job_count',
        title=f"Top Job Titles for '{degree_name}'",
        color_discrete_sequence=px.colors.sequential.Mint
    )
    
    fig.update_layout(
        xaxis_title="Job Titles",
        yaxis_title="Number of Jobs",
        xaxis={'categoryorder':'total descending'},
        bargap=0.2
    )
    
    st.plotly_chart(fig, use_container_width=True)
    return

# A user can type a degree and see the top 10 industries that require that degree
def top_industries_for_degree(degree_name, color_scheme='lightgreen'):
    query = f"""
        MATCH (d:ACADEMIC_DEGREE)
        WHERE toLower(d.degree_field) CONTAINS toLower("{degree_name}")
        MATCH (d)-[r1]-(j:JOB)-[r2]-(i:INDUSTRY)
        RETURN i.standardized_industry_name AS industry, 
            COUNT(*) AS job_count
        ORDER BY job_count DESC
        LIMIT 10
        """
    df = db.execute_query(query)
    
    if df.empty:
        st.warning("No matching degrees found. Try a different search term.")
        return
        
    fig = px.bar(
        df,
        x='industry',
        y='job_count',
        title=f"Top Industries for '{degree_name}'",
        color_discrete_sequence=px.colors.sequential.Mint
    )
    
    fig.update_layout(
        xaxis_title="Industries",
        yaxis_title="Number of Jobs",
        xaxis={'categoryorder':'total descending'},
        bargap=0.2
    )
    
    st.plotly_chart(fig, use_container_width=True)


# ~~~~~~~~ Based on Skill name ~~~~~~~~
# A user can type a skill and see the top 10 job titles that require that skill
def top_job_titles_for_skill(skill_name, color_scheme='lightblue'):
    query = f"""
        MATCH (s:SKILL)
        WHERE toLower(s.skill_name) CONTAINS toLower('{skill_name}')
        MATCH (s)-[REQUIRES]-(j:JOB)
        RETURN j.standardized_occupation AS job_title, 
               COUNT(*) AS job_count
        ORDER BY job_count DESC
        LIMIT 10
        """
    df = db.execute_query(query)
    
    if df.empty:
        st.warning("No matching skills found. Try a different search term.")
        return
        
    # Add constant root for hierarchy
    df['skill'] = skill_name
    
    fig = px.treemap(
        df,
        path=[px.Constant("All Jobs"), 'job_title'],
        values='job_count',
        color='job_count',
        color_continuous_scale='Mint',
        title=f"Top Job Titles for {skill_name}",
    )
    
    fig.update_layout(
        margin=dict(t=50, l=25, r=25, b=25)
    )
    
    st.plotly_chart(fig, use_container_width=True)
    return


# A user can type a skill and see the top 10 industries that require that skill
def top_industries_for_skill(skill_name, color_scheme='lightblue'):
    query = f"""
        MATCH (s:SKILL)
        WHERE toLower(s.skill_name) CONTAINS toLower('{skill_name}')
        MATCH (s)-[REQUIRES]-(j:JOB)-[HAS]-(i:INDUSTRY)
        RETURN i.standardized_industry_name AS industry, 
               COUNT(*) AS job_count
        ORDER BY job_count DESC
        LIMIT 10
        """
    df = db.execute_query(query)
    
    if df.empty:
        st.warning("No matching skills found. Try a different search term.")
        return
        
    # Add constant root for hierarchy
    df['skill'] = skill_name
    
    fig = px.treemap(
        df,
        path=[px.Constant("All Industries"), 'industry'],
        values='job_count',
        color='job_count',
        color_continuous_scale='Mint',
        title=f"Top Industries for {skill_name}"
    )
    
    fig.update_layout(
        margin=dict(t=50, l=25, r=25, b=25)
    )
    
    st.plotly_chart(fig, use_container_width=True)
    return

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ "TOP" analytics Section accross industries and job titles ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 

# ~~~~ PIE charts ~~~~
# Top job titles by number of job postings
def top_job_titles_pie_chart():
    query = """
        MATCH (j:JOB)
        RETURN j.job_title AS job_title, COUNT(j) AS job_postings
        ORDER BY job_postings DESC
        LIMIT 20
        """
    df = db.execute_query(query)
    fig = px.pie(
        df,
        names="job_title",
        values="job_postings",
        title="Top Job Titles by Number of Job Postings",
        color_discrete_sequence=px.colors.sequential.Oranges
    )
    st.plotly_chart(fig, use_container_width=True)
    return


# - Pie chart of the top 10 skills found in job postings
def top_skills_pie_chart():
    query = """
        MATCH (s:SKILL)-[r]-(j:JOB)
        RETURN s.skill_name AS skill, COUNT(s) AS skill_count
        ORDER BY skill_count DESC
        LIMIT 20
        """
    df = db.execute_query(query)
    fig = px.pie(
        df,
        names="skill",
        values="skill_count",
        title="Top Skills by Frequency",
        color_discrete_sequence=px.colors.sequential.Oranges
    )
    st.plotly_chart(fig, use_container_width=True)
    return


# ~~~~ Treemaps ~~~~
# - Treemap of the top job titles
def job_titles_treemap():
    query = """
        MATCH (j:JOB)
        WITH j.job_title AS job_title, COUNT(*) as count
        ORDER BY count DESC
        RETURN job_title, count
        LIMIT 20
        """
    df = db.execute_query(query)
    fig = px.treemap(
        df,
        path=["job_title"],
        values="count",
        title="Top Job Titles by Frequency",
        color="count",
        color_continuous_scale="Blues"
    )
    st.plotly_chart(fig)
    return


# - Tree map of the top industries with standardized names
def standardized_industries_treemap():
    query = """
        MATCH (i:INDUSTRY)-[r]->(j:JOB)
        RETURN i.standardized_industry_name AS industry, COUNT(i) AS count
        ORDER BY count DESC
        LIMIT 20
        """
    df = db.execute_query(query)
    
    # Ensure the DataFrame has the correct column names
    df.columns = ['industry', 'count']
    
    fig = px.treemap(
        df,
        path=["industry"],
        values="count",
        title="Top Industries by Frequency",
        color="count",
        color_continuous_scale="Blues"
    )
    st.plotly_chart(fig)
    return



# ~~~~ Bubble Charts ~~~~
def top_job_titles_and_industry_bubble_chart():
    query = """
        MATCH (j:JOB)-[r]-(i:INDUSTRY)
        WITH j.job_title AS job_title, COUNT(j) AS job_count, COLLECT(i.standardized_industry_name) AS industries
        RETURN job_title, job_count, industries
        ORDER BY job_count DESC
        LIMIT 20
    """
    df = db.execute_query(query)
    
    if df.empty:
        st.warning("No data available for visualization")
        return
    
    # Flatten the industries list for each job title
    df = df.explode('industries')
    
    fig = px.scatter(
        df,
        x='job_title',
        y='industries',
        size='job_count',
        color='job_count',
        hover_data=['job_count'],
        title="Top Job Titles and Associated Industries",
        labels={
            'job_title': 'Job Title',
            'industries': 'Industry',
            'job_count': 'Number of Job Postings'
        },
        color_continuous_scale='Greens'  # Change color to gradients of green
    )
    
    fig.update_layout(
        showlegend=True,
        xaxis_tickangle=-45,
        height=800
    )

    st.plotly_chart(fig, use_container_width=True)
    return


# - Scatter plot of the TOP  job titles and skills
def top_job_titles_skills_scatter():
    query = """
        MATCH (s:SKILL)-[r]-(j:JOB)
        WITH s.skill_name AS skill, COUNT(s) AS skill_count, COLLECT(j.job_title) AS job_titles
        RETURN skill, skill_count, job_titles
        ORDER BY skill_count DESC
        LIMIT 20
    """
    df = db.execute_query(query)
    
    if df.empty:
        st.warning("No data available for visualization")
        return
    
    # Flatten the job_titles list for each skill
    df = df.explode('job_titles')
    
    fig = px.scatter(
        df,
        x='skill',
        y='job_titles',
        size='skill_count',
        color='skill_count',
        hover_data=['skill_count'],
        title="Top Skills and Associated Job Titles",
        labels={
            'skill': 'Skill',
            'job_titles': 'Job Title',
            'skill_count': 'Number of Job Postings'
        },
        color_continuous_scale='Greens'  # Change color to gradients of green
    )
    
    fig.update_layout(
        showlegend=True,
        xaxis_tickangle=-45,
        height=800
    )

    st.plotly_chart(fig, use_container_width=True)
    return


# ~~~~ Sunburst Plots ~~~~
# A Sunburst Plot of the top 10 job titles by number of job postings and the skills required for each job title
def top_job_titles_and_skils_sunburst():
    query = """
        MATCH (j:JOB)-[r]->(s:SKILL)
        WITH j.job_title AS job_title, s.skill_name AS skill, COUNT(*) AS skill_count
        RETURN job_title, skill, skill_count
        ORDER BY skill_count DESC
        Limit 500
        """
    df = db.execute_query(query)
    
    if df.empty:
        st.warning("No data available for visualization")
        return
    
    # Group by job_title and get the top 10 skills for each job
    df = df.groupby('job_title').apply(lambda x: x.nlargest(10, 'skill_count')).reset_index(drop=True)
    
    # Flatten the skills list for each job title
    df = df.explode('skill')
    
    fig = px.sunburst(
        df,
        path=['job_title', 'skill'],
        values='skill_count',
        title="Top Job Titles and Required Skills",
        color='skill_count',
        color_continuous_scale='RdBu',
    )
    
    fig.update_layout(
        margin=dict(t=50, l=25, r=25, b=25)
    )
    
    st.plotly_chart(fig, use_container_width=True)
    return


# ~~~~ 3D Scatter Plots ~~~~
# - Scatter plot of the TOP 20 industries and skills
def top_industries_skills_scatter():
    query = """
        MATCH (s:SKILL)-[REQUIRES]-(j:JOB)-[HAS]-(i:INDUSTRY)
        WITH s.skill_name AS skill, i.standardized_industry_name AS industry, 
             COUNT(*) AS frequency
        RETURN skill, industry, frequency
        ORDER BY frequency DESC
        LIMIT 20
    """
    df = db.execute_query(query)
    
    if df.empty:
        st.warning("No data available for visualization")
        return
    
    fig = px.scatter_3d(
        df,
        x='industry',
        y='skill',
        z='frequency',
        size='frequency',
        color='frequency',
        hover_data=['frequency'],
        title="3D View: Top Industries and Required Skills",
        labels={
            'industry': 'Industry',
            'skill': 'Skill',
            'frequency': 'Frequency'
        },
        color_continuous_scale='balance'
    )
    
    fig.update_layout(
        scene = dict(
            xaxis_title='Industry',
            yaxis_title='Skill',
            zaxis_title='Frequency'
        ),
        width=1000,
        height=800,
        margin=dict(l=0, r=0, b=0, t=30)
    )

    st.plotly_chart(fig, use_container_width=True)
    return


# - Scatter plot of the TOP 20 job titles and industries and skills
def top_job_titles_industries_skills_scatter():
    query = """
        MATCH (s:SKILL)-[r1]-(j:JOB)-[r2]-(i:INDUSTRY)
        WITH j.job_title AS job_title, 
             i.standardized_industry_name AS industry,
             s.skill_name AS skill,
             COUNT(*) AS frequency
        RETURN job_title, industry, skill, frequency
        ORDER BY frequency DESC
        LIMIT 20
    """
    df = db.execute_query(query)
    
    if df.empty:
        st.warning("No data available for visualization")
        return
    
    fig = px.scatter_3d(
        df,
        x='job_title',
        y='industry',
        z='skill',
        size='frequency',
        color='frequency',
        hover_data=['frequency'],
        title="3D View: Jobs, Industries, and Skills Relationship",
        labels={
            'job_title': 'Job Title',
            'industry': 'Industry',
            'skill': 'Skill',
            'frequency': 'Frequency'
        },
        color_continuous_scale='balance'
    )
    
    fig.update_layout(
        scene = dict(
            xaxis_title='Job Titles',
            yaxis_title='Industries',
            zaxis_title='Skills'
        ),
        width=1000,
        height=800,
        margin=dict(l=0, r=0, b=0, t=30)
    )

    st.plotly_chart(fig, use_container_width=True)
    return
