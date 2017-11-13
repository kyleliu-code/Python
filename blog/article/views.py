from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from blog.article.models import Article , Comment 

# Create your views here.


def add (request):
    
    if request.method == 'POST':
        # 1. 接收前台提交的数据
        title = request.POST.get('title',None)
        content = request.POST.get('content',None)

        # 2. 数据写入数据库(首先要引入数据库文件)

        new = Article.objects.create(title = title,content = content)
        new.save()

        # 3. 跳转到 /list/页面
        # note: 跳转的时候，前面添加的 反斜杠，表示从端口径开始的url
        return HttpResponseRedirect('/list/')
    
    return render(request,'add.html',{'method_str':request.method})

def list(request):
    # 1. 从数据读取数据
    # 2. 将数据添加到模板文件中，并返回 模板文件
    
    articles = Article.objects.all().order_by('-id')
    # render 函数 是 拼接模板并返回对应字符串
    return render(request,'list.html', {'articles': articles})

# url 中传过来的 id 就是查询的入参
def view (request,id):
    # 1. 从数据库中取符合条件的数据

    article = Article.objects.get(id=id)
    # 1.1. 从 comment 表中取出 comment 对应的数据

    comments = Comment.objects.filter(Article = id).order_by('-id').all()

    # 2. 将数据添加到模板中，并返回模板文件对应字符串
    return render(request,'view.html',{'article':article,'comments': comments})

def comment_add (request):
    
    if request.method == 'POST':
        # 1. 获取前台传来的数据
        article_id = request.POST.get('article','')
        detail = request.POST.get('detail','')


    # 2. 将数据写入 Comment 表中
    if article_id and detail:
        comment = Comment()
        comment.Article = Article(id = article_id)
        comment.detail = detail
        comment.save()
    # 3. 重定向 到 /list/ url 下
    return HttpResponseRedirect('/view/' + article_id)