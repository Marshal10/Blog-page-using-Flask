from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)

response=requests.get("https://api.npoint.io/c790b4d5cab58020d391")
data=response.json()  
post_objs=[Post(post['id'],post['title'],post['subtitle'],post['body']) for post in data]

@app.route('/')
def home():  
    return render_template("index.html",posts=post_objs)

@app.route('/post/<int:id>')
def get_post(id):
    requested_post=None
    for post_obj in post_objs:
        if post_obj.id==id:
            requested_post=post_obj
    return render_template("post.html",post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)
