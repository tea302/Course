import json

# Для правильной склейки путей
import os

POST_PATH = os.path.join("data", "posts.json")
COM_PATH = os.path.join("data", "comments.json")

def get_posts_all() -> list[dict]:
    with open(POST_PATH, 'r', encoding='utf-8') as file:
        return json.load(file)


def get_post_by_pk(n):
    result = get_posts_all()

    for el in result:
        if el["pk"] == n:
            return el



def search_for_posts(word):
    result = get_posts_all()
    lst_result = []

    for posts in result:
        if word.lower() in posts['content'].lower():
            lst_result.append(posts)
    return lst_result


def get_posts_by_user(user_name):
    result = get_posts_all()
    lst_names = []

    for posts in result:
        if user_name.lower() in posts['poster_name'].lower():
            lst_names.append(posts)
    return lst_names


# Получает все комментарии
def get_comments_all() -> list[dict]:
    with open(COM_PATH, 'r', encoding='utf-8') as file:
        return json.load(file)


# Получает комментарии по id
def get_comments_by_post_id(needed_com):
    result = get_comments_all()
    lst = []

    for com in result:
        if com["post_id"] == needed_com:
            lst.append(com)

    return lst
