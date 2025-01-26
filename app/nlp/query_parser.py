from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from app.core.config import settings
from sqlalchemy import inspect
from app.db.database import engine
from app.db.schema_manager import TableSchema


def get_schema_description():
    inspector = inspect(engine)
    schema = []
    for table_name in inspector.get_table_names():
        columns = inspector.get_columns(table_name)
        schema.append(f"Table: {table_name}")
        for column in columns:
            schema.append(f"- {column['name']} ({column['type']})")
    return "\n".join(schema)


def format_schema_for_llm(table_schema: TableSchema) -> str:
    schema_text = f"Table: {table_schema.name}\n"
    schema_text += f"Description: {table_schema.description}\n\n"

    for col in table_schema.columns:
        schema_text += f"Column: {col.name}\n"
        schema_text += f"Type: {col.type}\n"
        schema_text += f"Description: {col.description}\n"
        if col.constraints:
            schema_text += f"Constraints: {', '.join(col.constraints)}\n"
        schema_text += "\n"

    return schema_text

def nlp_to_sql(query: str, table_schema: TableSchema) -> str:
    schema = format_schema_for_llm(table_schema)
    prompt = PromptTemplate(
        input_variables=["query", "schema"],
        template=(
            "Using this table schema with column descriptions:\n{schema}\n\n"
            "Convert this question to SQL:\n{query}\n\n"
            "SQL:"
        )
    )
    llm = OpenAI(api_key="")
    return llm.predict(prompt.format(query=query, schema=schema))
