# NEO4J GRAPH DB Credentials and Connection
import os
from neo4j import GraphDatabase
import psycopg2
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

#  --------- Neo4J ---------
# Neo4J DB Credentials and Connection

neo4j_url = os.getenv("NEO4J_CONNECTION_URL")
neo4j_user = os.getenv("NEO4J_USER")
neo4j_password = os.getenv("NEO4J_PASSWORD")

# Connect to the neo4j database
driver = GraphDatabase.driver(neo4j_url, auth=(neo4j_user, neo4j_password))

#  --------- PostgreSQL ---------
# PostgreSQL DB Credentials and Connection
host = os.getenv("POSTGRES_HOST")
database = os.getenv("POSTGRES_DB")
username = os.getenv("POSTGRES_USER")
password = os.getenv("POSTGRES_PASS")

# Initiate a connection to the pgDB and return cur & conn
def connect_pg_conn(host, database, username, password):
    # Connect to Postgres
    conn = psycopg2.connect(
        host=host,
        database=database,
        user=username,
        password=password,
        # timeout=30  # Increase the connection timeout to 30 seconds
    )
    cur = conn.cursor()
    return cur, conn

def execute_query(query):
    # Execute the query and return the DataFrame
    with driver.session() as session:
        result = session.run(query)
        data = [record.data() for record in result]
        df = pd.DataFrame(data)
    driver.close()
    return df

# Get the top industries with the most job postings
def get_job_categories_data():
    query = """
        MATCH (i:INDUSTRY)-[:POSTS]->(j:JOB)
        RETURN i.industry_name AS industry, COUNT(j) AS job_postings
        ORDER BY job_postings DESC
        LIMIT 15
        """
    # Execute the query and return the DataFrame
    df = execute_query(query)
    # print(df)
    return df


def get_job_data_from_Cypher(query):
    with driver.session() as session:
        result = session.run(query)
        data = [record.data() for record in result]
    return data

# get_job_categories_data()

