import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'food.settings')
import django
django.setup()
from area.models import Category, Page
import random

def populate():
        # 早午餐
        category = addCategory('早午餐')
        addPage(category, 'hecho做咖啡', 'http://kevinkaishek.wix.com/isitcoffee')
        # 午餐
        category = addCategory('午餐')
        addPage(category, '品田牧場', 'http://www.pinnada.com.tw/index.html')
        # 晚餐
        category = addCategory('晚餐')
        addPage(category, '凱恩斯岩燒餐廳cairns-stonegrill', 'http://www.cairns-stonegrill.com.tw/')
        # Print everything
        for category in Category.objects.all():
            for page in Page.objects.filter(category=category):
                print(category.name, '--', page.title)
def addCategory(name):
    category = Category.objects.get_or_create(name=name)[0]
    category.views = random.randint(0, 20)
    category.likes = random.randint(0, 20)
    category.save()
    return category
def addPage(category, title, url):
    page = Page.objects.get_or_create(category=category, title=title, url=url)[0]
    page.views = random.randint(0, 20)
    page.save()
if __name__ == '__main__':
    print('開始填入資料...')
    populate()
    print('完成。') 