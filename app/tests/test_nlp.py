import pytest
from app.nlp.query_parser import nlp_to_sql

def test_nlp_conversion():
    query = "How many orders have not synced today?"
    sql = nlp_to_sql(query)
    print(f"Generated SQL: {sql}")
    assert isinstance(sql, str)
    assert "SELECT" in sql.upper()