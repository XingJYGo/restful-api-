# restful api -
后台微博“增删改查”接口简易创建：
RESTful API实现增删改查的接口小案例.. 
python+flask+sqlite3数据库...



使用操作:

模拟数据库内容:

1 模拟数据库内容(也可以操作sqlite3存储数据)

POSTS = [
	{},
    {'title': 'first post', 'content': 'first post','word': 'first word'},
    {'title': 'last post', 'content': 'last post','word': 'last word'},
    {'title': 'how to learn interface test', 'content': 'how to learn interface test','word': 'how to learn interface test word'}
]

2 运行flaskStart.py文件:

调用请求方法,返回对应键的值.

```
# posts 请求的具体资源
class PostResource(Resource):
    # /posts/1 GET
    def get(self, post_id):
        post_id = int(post_id)
        abort_if_post_doesnt_exist(post_id)
        # return POSTS[post_id]
        post = Post.get(Post.id == post_id)
        return {'title': post.title, 'content': post.content}

    # /posts/1 DELETE
    def delete(self, post_id):
        post_id = int(post_id)
        abort_if_post_doesnt_exist(post_id)
        rows = Post.get(Post.id == post_id).delete_instance()
        return rows, 204

    # /posts/1 PUT
    def put(self, post_id):
        json_data = request.get_json(force=True)
        post_id = int(post_id)
        post = {'title': json_data['title'], 'content': json_data['content']}
        Post.update(title=json_data['title'], content=json_data['content']).where(Post.id == post_id).execute()
        # POSTS[post_id] = post
        return post, 201


```

