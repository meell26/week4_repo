from sqlalchemy import MetaData, Table, Column, Integer, String

metadata = MetaData()

students = Table(
   "students",
   metadata,
   Column("student_id", Integer, primary_key=True),
   Column("student_name", String(100)),
)
