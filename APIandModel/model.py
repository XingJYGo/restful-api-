from peewee import *

db = SqliteDatabase('posts.db')

class Post(Model):
    title = CharField(unique=True)
    content = TextField()
    job = CharField(unique=True)
    username = CharField(unique=True)
    password = IntegerField(unique=True)
    vip = BlobField(unique=True)
    class Meta:
        database = db



