# app/tests/test_schema_queries.py
from app.nlp.query_parser import nlp_to_sql
from app.db.schemas.address_schema import address_schema

test_queries = [
    "Show all addresses in district 'California'",
    "What is the phone number for address_id 5?",
    "Count how many addresses were updated today",
    "List all addresses with their city IDs that don't have a postal code"
]

for query in test_queries:
    print(f"\nQuery: {query}")
    sql = nlp_to_sql(query, address_schema)
    print(f"SQL: {sql}")