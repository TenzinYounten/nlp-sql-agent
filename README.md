# NLPSQL Agent

Convert natural language queries to SQL using OpenAI's language models with custom schema understanding.

## Tech Stack
- FastAPI: API framework
- OpenAI + LangChain: NLP processing
- SQLAlchemy: Database ORM
- MySQL: Database
- Pydantic: Data validation
- Python-dotenv: Environment management

## Prerequisites
- Python 3.8+
- MySQL Server
- OpenAI API key

## Installation

```bash
# Clone repository
git clone [repository-url]
cd nlp-sql-agent

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Unix
# or
.\venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt
```

## Configuration

Create `.env` file in root directory:
```env
DATABASE_URL=mysql+pymysql://user:password@localhost:3306/your_database
OPENAI_API_KEY=your-openai-key
```

## Project Structure
```
app/
├── api/
│   ├── routes.py        # API endpoints
├── core/
│   ├── config.py        # Configuration settings
├── db/
│   ├── database.py      # Database connection
│   ├── models.py        # SQLAlchemy models
│   ├── schemas/         # Table schema definitions
├── nlp/
│   ├── query_parser.py  # NLP processing
├── tests/              
└── main.py             # Application entry
```

## Schema Definition

Define table schemas in `app/db/schemas/`:

```python
from app.db.schema_manager import TableSchema, ColumnInfo

table_schema = TableSchema(
    name="table_name",
    description="Table description",
    columns=[
        ColumnInfo(
            name="column_name",
            type="data_type",
            description="Column description",
            constraints=["constraints"]
        ),
    ]
)
```

## Usage

1. Start server:
```bash
uvicorn app.main:app --reload
```

2. Send queries:
```bash
curl -X POST "http://localhost:8000/query/address" \
     -H "Content-Type: application/json" \
     -d '{"query": "Show all addresses in California"}'
```

Example Response:
```json
{
    "query": "Show all addresses in California",
    "sql": "SELECT * FROM address WHERE district = 'California'",
    "results": [...]
}
```

## API Endpoints

### POST /query/{table}
Convert natural language to SQL for specified table schema.

Request:
```json
{
    "query": "string"
}
```

Response:
```json
{
    "query": "string",
    "sql": "string",
    "results": []
}
```

## Error Handling
- 400: Invalid query or parsing error
- 500: Database or server error

## Testing
```bash
pytest app/tests/
```

## Contributing
1. Define new table schemas in `app/db/schemas/`
2. Update tests
3. Submit pull request

## Architecture
![nlp](https://github.com/user-attachments/assets/2d14f630-739c-4cf8-ae62-13e08f726f36)


## License
[Your License]
