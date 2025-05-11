import datetime
from pydantic import BaseModel

class User(BaseModel):
    username: str
    password: str
    create_date: datetime.datetime

class TestTable(BaseModel):
    title: str
    body: str

    class Config:
       from_attributes = True

class TestTableId(TestTable):
    id: int

    class Config:
        from_attributes = True