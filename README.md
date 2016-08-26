# djcelery_proj
django-celery study

版本：
django == 1.9
celery == 3.1.23
django-celery = 3.2.0a1


运行步骤
１.运行虚拟环境
2. 运行 django-celery:
$ python manage.py celery -A djcelery_proj worker -l info
3. 运行 django
$ python manage.py runserver 8111
4. 运行 celery beat
$  python manage.py  celery beat