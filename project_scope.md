# Aileana - Project & Features

**Overview**

The app will be build using Streamlit. It will have a basic user authentication system to access the app. The first page will have a basic analytics and visualizations dashbord with overall trends.
Another page will provide users with analytics and visualizations based on their interests: Standardized Job Titles, Industry, Skills, and name of the job title.
A chatbot will be able to answer questions about the job postings based on the following: Standardized Job Titles, Industry, Skills, and name of the job title.

---

## Pages

Page 1: Home & Analytics
Page 2: Data Analysis & Visualizations
Page 3: Chatbot
Page 4: What is Aileana & Contact

---

## Features

- User's must be authorized to access the app
- Analytics & Visualizaiton of job postings based on the following
- Chatbot that can answer questions about the job postings

### Main Data Analytics & Visualizations

- Bar chart of the top 10 job titles
- Bar chart of the top 10 industries
- Bar chart of the top 10 skills
- Word cloud of the job titles
- Word cloud of the industries
- Word cloud of the skills
- Scatter plot of the job titles and industries
- Scatter plot of the job titles and skills
- Scatter plot of the industries and skills
- Scatter plot of the job titles and industries and skills

### Data Analysis & Visualizations

A user must choose:

- The Field of interest: Standardized Job Titles, Industry, Skills
- Then a specific value from a dropdown list (as returnd from the database)
Then the user will see a visualization with all the relevant information based on their choice.

### LLM Chatbot

The chatbot will be able to answer questions about the job postings based on the following:

- Standardized Job Titles
- Industry
- Skills
- Name of the job title

The user queries will be stored to gather data for analytics.

### What is Aileana & Contact

Just a brief description of the app and a contact form to reach out to the developers.

### User Authorization

Users must:

- Provide an email and
- Agree to the terms and conditions

The user email will be stored into Postgress database to be used for future promotions and newletters.

The terms and conditions will mention that the user queries are stored for analysis and improvement of the app.

---

## Relevant Information

### Neo4J Database Schema

**Nodes**

``` CYPHER
[(:BENEFIT {name: "BENEFIT", indexes: [], constraints: []}), (:INDUSTRY {name: "INDUSTRY", indexes: [], constraints: []}), (:SKILL {name: "SKILL", indexes: [], constraints: []}), (:EXPERIENCE {name: "EXPERIENCE", indexes: [], constraints: []}), (:JOB {name: "JOB", indexes: ["embedding"], constraints: []}), (:RESPONSIBILITY {name: "RESPONSIBILITY", indexes: [], constraints: []})]
```

**Relationships**

``` CYPHER
[[:NEEDS {name: "NEEDS"}], [:REQUIRES {name: "REQUIRES"}], [:HAS {name: "HAS"}], [:OFFERS {name: "OFFERS"}], [:POSTS {name: "POSTS"}]]
```

