# app/db/schemas/address_schema.py
from app.db.schema_manager import TableSchema, ColumnInfo
address_schema = TableSchema(
   name="address",
   description="Stores address information for all locations",
   columns=[
       ColumnInfo(
           name="address_id",
           type="smallint unsigned",
           description="Unique identifier for each address",
           constraints=["PRIMARY KEY", "AUTO_INCREMENT"]
       ),
       ColumnInfo(
           name="address",
           type="varchar(50)",
           description="Primary address line with street number and name",
           constraints=["NOT NULL"]
       ),
       ColumnInfo(
           name="address2",
           type="varchar(50)",
           description="Secondary address line for additional details",
           constraints=["NULL"]
       ),
       ColumnInfo(
           name="district",
           type="varchar(20)",
           description="District or state name",
           constraints=["NOT NULL"]
       ),
       ColumnInfo(
           name="city_id",
           type="smallint unsigned",
           description="Foreign key reference to city table",
           constraints=["NOT NULL", "FOREIGN KEY REFERENCES city(city_id)"]
       ),
       ColumnInfo(
           name="postal_code",
           type="varchar(10)",
           description="ZIP or postal code",
           constraints=["NULL"]
       ),
       ColumnInfo(
           name="phone",
           type="varchar(20)",
           description="Contact phone number",
           constraints=["NOT NULL"]
       ),
       ColumnInfo(
           name="location",
           type="geometry",
           description="Geographic coordinates of the address",
           constraints=["NOT NULL", "SPATIAL INDEX"]
       ),
       ColumnInfo(
           name="last_update",
           type="timestamp",
           description="Timestamp of last record update",
           constraints=["NOT NULL", "DEFAULT CURRENT_TIMESTAMP ON UPDATE"]
       )
   ]
)