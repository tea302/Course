from flask import Flask, request, render_template, send_from_directory
from utils import *

# Для правильной склейки путей
import os

POST_PATH = os.path.join("data", "posts.json")
UPLOAD_FOLDER = os.path.join("uploads", "images")
IMG_FOLDER = os.path.join("static", "img")



app = Flask(__name__)


@app.route("/")
def page_index():
    """
    Собирает все посты в ленту
    """

    results = get_posts_all()

    context = {
        "title": "Все посты",
        "posts_all": results
    }

    return render_template("index.html", **context)


@app.route("/list")
def page_tag():
    """
    Поиск по тэгам
    """

    pass


@app.route("/post/<path:path>")
def page_post(path):
    """
    реализует просмотр поста
    :return:
    """

    result = get_post_by_pk(path)

    com = get_comments_by_post_id(path)
    com_len = len(com)

    context = {
        "title": "Один пост",
        "post_one": result,
        "comments": com,
        "len": com_len
    }

    return render_template("post.html", **context)

@app.route('/users/<path:path>')
def user_name(path):
    """"
    Реализует вывод по пользователю
    """

    posts = get_posts_by_user(path.lower())

    context = {
            "quantity": len(posts),
            "word": path,
            "posts_all": posts,
            "title": "Все посты пользователя"
                  }

    return render_template("user-feed.html", **context)




@app.route('/user-feed', methods=['POST'])
def search_by_user():

    if request.method == 'POST':
        search_word = request.form['key_word']

        posts = get_posts_by_user(search_word.lower())


        context = {
            "quantity": len(posts),
            "word": search_word,
            "posts_all": posts,
            "title": "Все посты пользователя"
                  }

    return render_template("user-feed.html", **context)


@app.route('/search', methods=['POST'])
def search_by_word():

    if request.method == 'POST':
        search_word = request.form['key_word']

        posts = search_for_posts(search_word.lower())

        if len(posts) > 10:
            posts = posts[0:10]

        context = {
            "quantity": len(posts),
            "word": search_word,
            "posts_all": posts,
            "title": "Результат поиска"
                  }

    return render_template('search.html', **context)




@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


if __name__ == '__main__':
    app.run(debug=True)


