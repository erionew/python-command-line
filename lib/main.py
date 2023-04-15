from peewee import *

db = PostgresqlDatabase(
    'contacts',
    user='',
    password = '',
    host = 'localhost',
    port = 5432
    )


db.connect()

class BaseModel(Model):
    class Meta:
        database = db