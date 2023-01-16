from flask import render_template, Blueprint, request
from pprint import pprint
from dao.dao import PostsDAO

'''В posts сразу передаются пути для posts.json и comments.json'''
'''Стили(папка css) читаются из папки static'''
'''Путь к стилям прописывается static_folder='/static' (папка), static_url_path='/static' (путь для Flask) '''
''' в index.html (head) и других шаблонах путь к css - /static/css/styles.min.css '''


main_blueprint = Blueprint('main_blueprint', __name__, template_folder='./templates', static_folder='/static', static_url_path='/static')
posts = PostsDAO('./data/posts.json', './data/comments.json')

'''Главная страница. Посты'''
'''def index_page() отвечает за список всех постов'''
'''pprint возвращает список постов'''
''' truncate(50) - ограничение поста в 50 символов'''
@main_blueprint.route('/')
def index_page():
    all_posts = posts.get_all_posts()
    #pprint(all_posts)
    return render_template('index.html', posts=all_posts)


'''Комментарии под постами'''
'''pprint возвращает список словарей конкретного комментария'''
''' {{ comments | count }} - счетчик комментариев'''
@main_blueprint.route('/posts/<int:postid>')
def post_page(postid):
    found_post = posts.get_post_by_pk(postid)
    comments = posts.get_comments_by_post_id(postid)
    #pprint(found_post)
    #pprint(comments)
    return render_template('post.html', post=found_post, comments=comments)


'''Поиск постов'''
'''При введении в окошко поиска на сайте, имеющейся где-либо фразы'''
'''pprint возвращает список, где указано имя пользователя номер поста '''
'''print(query) - возвращает слово введенное в поиск'''
'''В index и search в форме поиска обязательно указывается имя переменной, по которой передается значение name="s" '''
''' и form action="/search" '''
'''Если имеются пользователи без постов, можно использовать ValueError и вернуть [] (у нас таких юзеров нет)'''
''' {{ posts | count }} - счетчик найденных постов '''
@main_blueprint.route('/search', methods=['GET'])
def search_page():
    query = request.args.get('s')
    #print(query)
    found_posts = posts.search_posts(query)
    #pprint(found_posts)
    #found_posts = []
    #if len(found_posts) == 0:
    #    raise ValueError
    return render_template('search.html', posts=found_posts)


'''Посты конкретного пользователя'''
@main_blueprint.route('/users/<username>', methods=['GET'])
def user_page(username):
    user_posts = posts.get_posts_by_username(username)
    return render_template('user-feed.html', posts=user_posts, username=username)


