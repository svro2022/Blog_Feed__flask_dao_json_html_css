'''Поля класса из posts.json'''
'''repr позволит увидеть запись вида - имя создателя поста, номер поста (pk)'''
'''Поля класса в ссылках index.html - section class="items" '''
'''truncate(50) - ограничение в 50 символов'''


class Post:
     def __init__(self, poster_name, poster_avatar, pic, content, views_count, likes_count, pk):
         self.poster_name = poster_name
         self.poster_avatar = poster_avatar
         self.pic = pic
         self.content = content
         self.views_count = views_count
         self.likes_count = likes_count
         self.pk = pk

     def __repr__(self):
         return f'{self.poster_name}, номер поста {self.pk}'

