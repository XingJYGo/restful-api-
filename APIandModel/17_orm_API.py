#coding:UTF-8
from model import *

# dir
# ----1 connect
# ----2 create
# ----3 get==select
# ----4 get==select
# ----5 update

# ===================用可视化工具替代代码创建
# ----1 connect
# db.connect()
# db.create_tables([Post])
# db.connect()
#
# ----2 create
db.connect()
Post.create(title='first post',content='I do not care',)

# ----3 get
# post = Post.get(Post.title == 'frise post')
# print post.id
#
# # ----4 get==select
# Post.create(title='forth post',content='Rubt is butter than haha')
# get all Post files
posts = Post.select()
for post in posts:
    print(post.id)
    print(post.title)
    print(post.content)

# ----5 update
# Post.update(title='has been updated').where(Post.id == 1).execute()

# ----6 delete
# Post.get(Post.id == 1).delete_instance()







