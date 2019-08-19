# db_fake_data_generator.py
import os
from random import *
from bs4 import BeautifulSoup
import urllib.request

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dongnebug24.settings')

import django
django.setup()

## FAKE POP SCRIPT
from dongnebug.models import *
from django.contrib.auth.models import User
from api.models import Locations
from faker import Faker

fake = Faker('ko_KR')

def add_User(N=20):
    for entry in range(N):
        t = User.objects.get_or_create(
            id=entry+1,
            username=fake.user_name(),
            password='password',
            email=fake.email(),
            first_name=fake.first_name(),
            last_name=fake.last_name()
        )[0]
        t.save()

def add_Complain(N=20):
    for entry in range(N):
        file = fake.file_name(category='imagefile', extension='jpg')
        ### crawling code ####
        base_url = "http://10000img.com/"
        url = "http://10000img.com/ran.php"
        html = urllib.request.urlopen(url)
        source = html.read()
        soup = BeautifulSoup(source, "html.parser")
        img = soup.find("img")
        img_src = img.get("src")
        img_url = base_url + img_src
        img_name = img_src.replace("/", "")
        urllib.request.urlretrieve(img_url, "./media/" + img_name)
        os.rename("./media/" + img_name, "./media/" + file)
        Complain.objects.filter(id=entry+1).update_or_create(
            author_id=User.objects.all()[randint(0, 19)].id,
            title=fake.text(max_nb_chars=20, ext_word_list=None),
            content=fake.text(max_nb_chars=200, ext_word_list=None),
            latitude=fake.latitude(),
            longitude=fake.longitude(),
            file=file
         )


def update_Complain(N=20):
    for entry in range(N):
        fake.seed(randint(1, 1000))
        Complain.objects.filter(id=entry+1).update_or_create(
            author_id=User.objects.all()[randint(0, 19)].id,
            title=fake.text(max_nb_chars=20, ext_word_list=None),
            content=fake.text(max_nb_chars=200, ext_word_list=None),
            latitude=fake.latitude(),
            longitude=fake.longitude(),
            file=fake.file_name(),
         )
        # t.save()

def add_Favorite(N=20):
    for entry in range(N):
        t = Favorite.objects.get_or_create(
            user_id=User.objects.all()[randint(0, 19)].id,
            complain_id=Complain.objects.all()[randint(0, 19)].id
        )[0]
        t.save()

def add_Comment(N=20):
    for entry in range(N):
        t = Comment.objects.get_or_create(
            user_id=User.objects.all()[randint(0, 19)].id,
            complain_id=Complain.objects.all()[randint(0, 19)].id,
            content=fake.text(max_nb_chars=200, ext_word_list=None),
        )[0]
        t.save()

def update_Comment(N=20):
    for entry in range(N):
        Comment.objects.filter(id=entry+1).update(
            user_id=User.objects.all()[randint(0, 19)].id,
            complain_id=Complain.objects.all()[randint(0, 19)].id,
            content=fake.text(max_nb_chars=200, ext_word_list=None),)
        # t.save()

def add_Sympathy(N=20):
    for entry in range(N):
        t = Sympathy.objects.get_or_create(
            user_id=User.objects.all()[randint(0, 19)].id,
            complain_id=Complain.objects.all()[randint(0, 19)].id,
        )[0]
        t.save()

def add_Location(N=20):
    for entry in range(N):
        t = Locations.objects.get_or_create(
            latitude=fake.latitude(),
            longitude=fake.longitude(),
            author_id=User.objects.all()[entry].id,
        )

def update_Location(N=20):
    for entry in range(N):
        Locations.objects.filter(user_id=entry+1).update(
            complain_id=Complain.objects.all()[randint(0, 19)].id,
            content=fake.text(max_nb_chars=200, ext_word_list=None),)


if __name__ == "__main__":
    print("db_fake_data_generator.py를 열고, 함수를 하나하나씩 실행하세요. 주석을 제거해야 할겁니다.")
    print("populating script!")
    # add_User()
    add_Complain()
    # update_Complain()
    # add_Complain_Image()
    # update_Complain_Image()
    # add_Comment()
    # update_Comment()
    # add_Favorite()
    # add_Sympathy()
    # add_Location()
    print("populating complete!")

#TODO : 커밋해서 현 상황 푸시하기.
#TODO : 나머지 Image부분이나, Video부분, 그리고, Comment나 Sympathy값이 증가할 때마다, Complain의 num_of_sympathy 등의
# 값이 변할 수 있게 끔 만들기 즉, DB 내용 추가