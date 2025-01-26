# test_nlp.py
from app.nlp.query_parser import nlp_to_sql

query = "How many orders have not synced today?"
sql = nlp_to_sql(query)
print(sql)