#coding: utf-8
from flask import Flask, request, g
from flask.ext.restful import reqparse, abort, Api, Resource
from model import *
import time
# 格式
app = Flask(__name__)
api = Api(app)
app.debug = True

from peewee import *
# 创建数据库posts.db 的对象
db = SqliteDatabase('posts.db')
# 创建数据库中Post表的类
class Post(Model):
    title = CharField(unique=True)
    content = TextField()
    job = CharField(unique=True)
    username = CharField(unique=True)
    password = IntegerField(unique=True)
    vip = BlobField(unique=True)

    class Meta:
        database = db
# 格式，POSTS数据库的假数据
POSTS = [
	{},
    {'title': 'first post', 'content': 'I do not care', 'job': 'doc', 'username': 'a1', 'password': '123456', 'vip': 'True'},
    {'title': 'third post', 'content': 'I do not care', 'job': 'tea', 'username': 'a2', 'password': '123456', 'vip': 'False'}
]
# 格式：数据库链接
@app.before_request
def before_request():
    g.db = db
    g.db.connect()
# 格式：数据库断开
@app.after_request
def before_request(response):
    g.db.close()
    return response

# 方法：判断Post表类  的接口是否存在
def abort_if_post_doesnt_exist(username):
    # try:
    #     POSTS[post_id]
    # except IndexError:
    #     abort(404, message="POSTS doesn't exist")
    # if Post.select().where(id == int(post_id)).count() <= 0:
        # abort(404, message="POSTS doesn't exist")
    post_username = username
    try:
        Post.get(Post.username == post_username)
    except Post.DoesNotExist:
        abort(404, message="POSTS doesn't exist")


# 变量，添加数据库表“post”
parser = reqparse.RequestParser()
parser.add_argument('post', type=int)


# 类：Post表资源类。 访问URL为：默认url/数据库名/post_id
class PostResource(Resource):
    # get方法，通过/posts/id 到返回值
    # /posts/username GET
    def get(self,post_username):
        abort_if_post_doesnt_exist(post_username)
        # return POSTS[post_id]
        post = Post.get(Post.username == post_username)
        return {'title': post.title, 'content': post.content,'job':post.job,'vip':post.vip}

    # DELETE方法，通过/posts/id 删掉对应数据
    # /posts/username DELETE
    def delete(self, post_username):
        abort_if_post_doesnt_exist(post_username)
        rows = Post.get(Post.username == post_username).delete_instance()
        return rows, 204

    #  PUT方法，通过/posts/id 更换对应数据
    # /posts/username PUT
    def put(self, post_username):
        json_data = request.get_json(force=True)
        post = {'title': json_data['title'], 'content': json_data['content'],'job': json_data['job']}
        Post.update(title=json_data['title'], content=json_data['content'],job=json_data['job']).where(Post.username == post_username).execute()
        # POSTS[post_username] = post
        return post, 201

    # post方法，url：给定url/posts（数据库名）---data中写上对应数据名{"title":"000000000title","content":"000000000content"-------}



# 类：修改查询列表与创建post逻辑
class PostList(Resource):
    # /posts GET
    def get(self):
    	posts = []
        # 查询数据，需要做分页查询
        raw_posts = Post.select()
#=========== 方法：批量添加所有字节
    	for post in raw_posts:
    		if post:
    			new_post = {}
    			# new_post['url'] = '/posts/' + str(POSTS.index(post))
                new_post['url'] = '/posts/' + str(post.username)
    			# new_post['title'] = post['title']
                new_post['title'] = post.title
                new_post['content'] = post.content
                new_post['job'] = post.job
                posts.append(new_post)
        return posts


    # /posts POST
    def post(self):
        json_data = request.get_json(force=True)
        print json_data
        try:
#=========== 方法：表Post类 创建对应的数据
            post = Post.create(title=json_data['title'], content=json_data['content'],job=json_data['job'])
            # POSTS.append({'title': json_data['title'], 'content': json_data['content'],job=json_data['job']})
            return post.id, 201
        except IntegrityError:
            return {'message': 'the title is already token'}, 401

# 格式：api添加指定接口/posts
api.add_resource(PostList, '/posts')
# 格式：api添加指定URL/posts/<post_username>
api.add_resource(PostResource, '/posts/<post_username>')


if __name__ == '__main__':
    app.run(debug=True)