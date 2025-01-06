# Aileana - Project & Features

**Overview**

The app will be build using Streamlit. It will have a basic user authentication system to access the app. The first page will have a basic analytics and visualizations dashbord with overall trends.
Another page will provide users with analytics and visualizations based on their interests: Standardized Job Titles, Industry, Skills, and name of the job title.
A chatbot will be able to answer questions about the job postings based on the following: Standardized Job Titles, Industry, Skills, and name of the job title.

---

---

## Neo4J Database Schema

**Nodes & labels**

```CYPHER
["INDUSTRY"] : ["industry_name", "standardized_industry_name"]

["JOB"] : ["employment_type", "employment_model", "job_seniority", "minimum_level_of_education", "standardized_occupation", "job_title", "country", "job_reference", "job_description"]

["SKILL"] : ["skill_name", "skill_category", "skill_type"]

["EXPERIENCE"] : ["minimum_years", "years_required"]

["BENEFIT"] : ["benefit_name"]

["RESPONSIBILITY"] " ["description"]

["ACADEMIC_DEGREE"] : ["degree_name", "degree_type", "degree_category"]

["CERTIFICATION"] : ["certification_name", "certification_type", "certification_category"]

```

**Relationships and Nodes**

```CYPHER
(j:JOB)-[:REQUIRES]->(ad:ACADEMIC_DEGREE)

(j:JOB)-[:HAS]->(r:RESPONSIBILITY)

(j:JOB)-[:OFFERS]->(b:BENEFIT)

(j:JOB)-[:REQUIRES]->(e:EXPERIENCE)

(j:JOB)-[:NEEDS]->(s:SKILL)

(j:JOB)-[:REQUIRES]->(c:CERTIFICATION)

(j:JOB)<-[:POSTS]-(i:INDUSTRY)

(i:INDUSTRY)<-[:BELONGS_TO]-(in:INDUSTRY_NAME)

```
