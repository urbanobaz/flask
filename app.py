from flask import Flask, render_template, redirect, request

app = Flask(__name__)
app.config['DEBUG'] = True

allBlogs = {
    1: {
        'title': "My first blog entry",
        'body': "this is my first blog entry, Hello there"
    },
    2: {
        'title': "My second blog entry",
        'body': "this is my 2nd blog entry, Hello there"
    }
}

@app.route('/')
def home():
    return render_template("index.html", name="Urbano Baz", online=True)

@app.route('/blogs')
def blogsList():
    return render_template("blogs.html", blogs=allBlogs)

@app.route('/add_blog')
def addBlog():
    return render_template("add_blog.html")

@app.route('/submit_blog', methods=["POST"])
def submitBlog():
    blogTitle = request.form["blog_title"]
    blogBody = request.form["blog_body"]
    next_id = list(allBlogs.keys())[-1] + 1
    allBlogs[next_id] = {
        'title': blogTitle,
        'body': blogBody
    }
    return redirect('/blogs')

@app.route('/blog/<id>')
def singleBlog(id):
    singleBlog = allBlogs[int(id)]
    return render_template("blog.html", blog=singleBlog)


if __name__ == "__main__":
    app.run()