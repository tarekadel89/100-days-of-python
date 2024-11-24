from flask import Flask, render_template
import requests

app = Flask(__name__)

all_blogs = []

@app.route('/')
def home():
    global all_blogs
    blogs_data = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    all_blogs = blogs_data.json()
    return render_template("index.html", blogs = all_blogs)

@app.route('/blog/<int:blog_id>')
def blog_detail(blog_id):
    global all_blogs
    blog_info = next((blog for blog in all_blogs if blog['id'] == blog_id), None)
    if blog_info:
        return render_template("post.html", blog=blog_info)
    else:
        return "Blog not found", 404
    

if __name__ == "__main__":
    app.run(debug=True)
