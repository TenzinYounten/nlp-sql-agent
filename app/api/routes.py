# app/api/routes.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.nlp.query_parser import nlp_to_sql
from app.db.schemas.address_schema import address_schema
from app.db.database import engine
import sqlalchemy

router = APIRouter()

class QueryRequest(BaseModel):
    query: str

@router.post("/query/address")
async def process_address_query(request: QueryRequest):
    try:
        sql = nlp_to_sql(request.query, address_schema)
        with engine.connect() as connection:
            result = connection.execute(sqlalchemy.text(sql))
            # Convert binary and other special types safely
            rows = []
            for row in result:
                processed_row = {}
                for key, value in row._mapping.items():
                    if isinstance(value, bytes):
                        try:
                            processed_row[key] = value.decode('utf-8')
                        except UnicodeDecodeError:
                            processed_row[key] = str(value)
                    else:
                        processed_row[key] = value
                rows.append(processed_row)
        return {"query": request.query, "sql": sql, "results": rows}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))