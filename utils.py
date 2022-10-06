import json
from json import JSONDecodeError

# Для правильной склейки путей
import os

POST_PATH = os.path.join("data", "posts.json")
COM_PATH = os.path.join("data", "comments.json")


def get_posts_all() -> list[dict]:
    """
    Получаем все посты из файла,
    обработка ошибок при проблемах с открытием файлов
    """
    with open(POST_PATH, "r", encoding="utf-8") as file:
        try:
            return json.load(file)
        except FileNotFoundError:
            return "Файл не найден"
        except JSONDecodeError:
            return "Файл не удается преобразовать"


def get_post_by_pk(n):
    """
    Получаем пост по post id (pk)
    """
    result = get_posts_all()

    for el in result:
        if el["pk"] == n:
            return el


def search_for_posts(word):
    """
    Поиск по слову
    """
    result = get_posts_all()
    lst_result = []

    for posts in result:
        if word.lower() in posts["content"].lower():
            lst_result.append(posts)
    return lst_result


def get_posts_by_user(user_name):
    """
    Поиск по имени пользователя
    """
    result = get_posts_all()

    is_exists = False
    lst_names = []

    for posts in result:
        if user_name.lower() in posts["poster_name"].lower():
            lst_names.append(posts)
            is_exists = True

    if not is_exists:
        raise ValueError

    return lst_names


def get_comments_all() -> list[dict]:
    """
    Получаем все комментарии,
    обработка ошибок при проблеме открытия файлов json
    """
    with open(COM_PATH, "r", encoding="utf-8") as file:
        try:
            return json.load(file)
        except FileNotFoundError:
            return "Файл не найден"
        except JSONDecodeError:
            return "Файл не удается преобразовать"


def get_comments_by_post_id(needed_com):
    """
    Получает комментарии по id,
    обработка ошибок, если комментарий не существует
    """
    result = get_comments_all()
    lst = []

    is_exists = False
    for com in result:
        if com["post_id"] == needed_com:
            is_exists = True
            lst.append(com)

    if not is_exists:
        raise ValueError

    return lst
