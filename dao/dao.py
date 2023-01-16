import json
from dao.post import Post

'''PostsDAO отвечает за получение постов и их обработку'''


class PostsDAO:
    def __init__(self, posts_path, comments_path):
        self.posts_path = posts_path
        self.comments_path = comments_path

    '''Открываем json файл, список экземпляров класса Post'''
    '''Список словарей в json файле преобразуем в список объектов'''

    def load_posts(self):
        with open(self.posts_path, 'r', encoding='utf-8') as file:
            new_posts = []
            posts_data = json.load(file)

            for post in posts_data:
                new_posts.append(Post(
                    post['poster_name'],
                    post['poster_avatar'],
                    post['pic'],
                    post['content'],
                    post['views_count'],
                    post['likes_count'],
                    post['pk']))
        return new_posts

    ''' Возвращает список словарей'''

    def load_posts_json(self):
        with open(self.posts_path, 'r', encoding='utf-8') as file:
            posts_data = json.load(file)

        return posts_data


    '''Открывает комментарии из json файла'''

    def load_comments(self):
        with open(self.comments_path, 'r', encoding='utf-8') as file:
            comments = json.load(file)
        return comments


    '''Загрузка всех постов из файла'''

    def get_all_posts(self):
        return self.load_posts()

    '''Поиск постов по имени пользователя (username)'''

    def get_posts_by_username(self, username):
        posts = self.load_posts()
        user_posts = []

        for post in posts:
            if post.poster_name.lower() == username.lower():
                user_posts.append(post)

        return user_posts

    '''Получение комментариев определенного поста и загрузка в список'''

    def get_comments_by_post_id(self, post_id):
        comments = self.load_comments()
        post_comments = []

        for comment in comments:
            if comment['post_id'] == post_id:
                post_comments.append(comment)
        return post_comments

    '''Поиск постов'''
    '''Поиск подстроки в строке'''

    def search_posts(self, substr):
        posts = self.load_posts()
        new_posts = []

        for post in posts:
            if substr.lower() in post.content.lower():
                new_posts.append(post)
        return new_posts

    '''Получение поста по его номеру(pk)'''

    def get_post_by_pk(self, pk):
        posts = self.load_posts()
        for post in posts:
            if post.pk == pk:
                return post

        return

    '''Получение конкретного поста возвращает словарь'''

    def get_post_by_pk_json(self, pk):
        posts = self.load_posts_json()
        for post in posts:
            if post['pk'] == pk:
                return post

        return

