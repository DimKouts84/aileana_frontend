# Aileana - AI-Powered Job Market Analysis

> **Navigating the job market one prompt at a time** .


## Overview

Aileana is an advanced LLM chatbot that provides deep insights into the job market, helping individuals navigate career paths and keeping professionals updated on market trends. Using state-of-the-art LLMs and Retrieval-Augmented Generation (RAG), Aileana analyzes job postings to identify correlations between jobs, skills, requirements, benefits, experience, and responsibilities.


### Features

* 🤖 AI-powered job market analysis
* 📊 Interactive data visualizations
* 💬 Intelligent chatbot with market insights
* 🔍 Advanced search and filtering
* 📈 Real-time market trend analysis

---

## 💬 The Story

**Eleana** was nearly 18 years old, facing the critical decision of choosing her career and relevant academic studies.

She had a passion for Biology  *(or at least thought she did)* , but no one in her family or circle was familiar with this field, and the job prospects were uncertain 🤔.

Given my background in the health domain, she asked me if pursuing Biology was a good idea. My response was something like: " *If it is your passion, follow it.* "

However, this answer was *generic* and  *insincere* , to be honest. The truth was that *I had no idea.* This led me to ponder:

* Is it really good advice? Is 'liking' a subject the only criterion for choosing a field of study?
* What are the employment prospects after graduation?
* What related jobs are available, and what other skills are needed to qualify for these jobs?
* What benefits do such jobs usually offer?

As a data nerd 🤓, I realized the job market operates like any other market:

* Supply and demand are key driving forces.
* Higher qualifications/specializations generally lead to higher pay.

Only *data* can provide answers to these questions, not anecdotal experiences.

Thus,  ***Aileana*** , this project, was born.


---

## ⚡️Tech Stack

| Category                  | Technology                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Frontend**        | ![Streamlit](https://img.shields.io/badge/-Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)                                                                                                                                                                                                                                                                                                                                                                                              |
| **Backend**         | ![Python](https://img.shields.io/badge/-Python-3776AB?style=flat&logo=python&logoColor=white)                                                                                                                                                                                                                                                                                                                                                                                                       |
| **Databases**       | ![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-336791?style=flat&logo=postgresql&logoColor=white) ![Neo4j](https://img.shields.io/badge/-Neo4j-008CC1?style=flat&logo=neo4j&logoColor=white)                                                                                                                                                                                                                                                                                                  |
| **Web Scraping**    | ![Beautiful Soup](https://img.shields.io/badge/-Beautiful_Soup-FFD700?style=flat&logo=beautiful-soup&logoColor=black) ![Selenium](https://img.shields.io/badge/-Selenium-43B02A?style=flat&logo=selenium&logoColor=white)                                                                                                                                                                                                                                                                             |
| **Data Processing** | ![Pandas](https://img.shields.io/badge/-Pandas-150458?style=flat&logo=pandas&logoColor=white)                                                                                                                                                                                                                                                                                                                                                                                                       |
| **DevOps**          | ![Docker](https://img.shields.io/badge/-Docker-2496ED?style=flat&logo=docker&logoColor=white)                                                                                                                                                                                                                                                                                                                                                                                                       |
| **Testing**         | ![Pytest](https://img.shields.io/badge/-Pytest-0A9EDC?style=flat&logo=pytest&logoColor=white)                                                                                                                                                                                                                                                                                                                                                                                                       |
| **LLM Frameworks**  | ![Langchain](https://img.shields.io/badge/-Langchain-FF4B4B?style=flat&logo=langchain&logoColor=white) ![OpenAI](https://img.shields.io/badge/-OpenAI-02DE20?style=flat&logo=openai&logoColor=Green) ![Groq](https://img.shields.io/badge/-Groq-FFA200?style=flat&logo=groq&logoColor=Orange) ![Llama 3](https://img.shields.io/badge/-Llama_3-150458?style=flat&logo=llama3&logoColor=blue) ![Hugging Face](https://img.shields.io/badge/-Hugging_Face-FFD700?style=flat&logo=huggingface&logoColor=white) |


### Project Structure

**├── components/         # Reusable UI components**

**├── pages/             # Streamlit pages**

**├── static/            # Static assets**

**├── Home.py           # Main application entry**

**└── requirements.txt   # Python dependencies**

---

## Data Processing Pipeline

1. Web scraping of job listings
2. Translation to English
3. Storage in PostgreSQL
4. LLM processing for structured data
5. Neo4j graph database population
6. Vector embeddings creation
7. RAG-enhanced user interactions

More information on the data extraction and classification pipeline using LLM AI agents can be found [here](https://github.com/DimKouts84/aileana-data-backend).

### International Standards

* NACE V2 (Economic Activities)
* ISCED 2011 (Education Levels)
* ISCO-88 (Occupation Classifications)

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.

## Contact
 
Made with ❤️ by [Dimitris Koutsomichalis](https://www.linkedin.com/in/dimitris-koutsomichalis)
