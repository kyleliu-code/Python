from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length = 30)
    content = models.TextField()

    class Meta:
        db_table = 'Article'

# def Article(models.Model):
#     title = models.CharField(max_length = 30)
#     content = models.TextField()
    
#     class Meta:
#         db_table = 'Article'


# 在 article 数据库文件中创建 comment 文件夹

class Comment(models.Model):
    # 这个Article 是块级作用域中的变量
    Article = models.ForeignKey(Article,related_name = 'article_comment')
    detail = models.TextField()

    class Meta:
        db_table = 'Comment'
