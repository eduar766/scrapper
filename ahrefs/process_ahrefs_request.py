from .models import UrlSearch, Backlinks, GoogleSearch, GoogleBD, CSV_import, ScrapperTest, SingleAhref

from urllib.parse import urlparse
import time
import urllib.request

def ahref_0(array, session_id):
    lenght = len(array)
    i = 0

    while i < lenght:
        backlink_info = {
            'url_from': array[i]['url_from'],
            'title': array[i]['title'],
            'url_to': array[i]['url_to'],
            'language': array[i]['language'],
            'anchor': array[i]['anchor'],
            'nofollow': array[i]['nofollow']
        }
        bk = Backlinks.objects.create(
            url_from = backlink_info['url_from'],
            title = backlink_info['title'],
            url_to = backlink_info['url_to'],
            language = backlink_info['language'],
            anchor = backlink_info['anchor'],
            nofollow = backlink_info['nofollow'],
            site_link = 'Articulo',
            session_id = session_id,
        )
        bk.save()
        print(bk)
        i += 1

def ahref_1(array, session_id):
    lenght = len(array)
    i = 0

    while i < lenght:
        backlink_info = {
            'url_from': array[i]['url_from'],
            'title': array[i]['title'],
            'url_to': array[i]['url_to'],
            'language': array[i]['language'],
            'anchor': array[i]['anchor'],
            'nofollow': array[i]['nofollow']
        }
        bk = Backlinks.objects.create(
            url_from = backlink_info['url_from'],
            title = backlink_info['title'],
            url_to = backlink_info['url_to'],
            language = backlink_info['language'],
            anchor = backlink_info['anchor'],
            nofollow = backlink_info['nofollow'],
            site_link = 'Articulo',
            session_id = session_id,
        )
        bk.save()
        i += 1

def ahref_2(array, session_id):
    lenght = len(array)
    i = 0

    while i < lenght:
        backlink_info = {
            'url_from': array[i]['url_from'],
            'title': array[i]['title'],
            'url_to': array[i]['url_to'],
            'language': array[i]['language'],
            'anchor': array[i]['anchor'],
            'nofollow': array[i]['nofollow']
        }
        bk = Backlinks.objects.create(
            url_from = backlink_info['url_from'],
            title = backlink_info['title'],
            url_to = backlink_info['url_to'],
            language = backlink_info['language'],
            anchor = backlink_info['anchor'],
            nofollow = backlink_info['nofollow'],
            site_link = 'Articulo',
            session_id = session_id,
        )
        bk.save()
        i += 1

def ahref_3(array, session_id):
    lenght = len(array)
    i = 0

    while i < lenght:
        backlink_info = {
            'url_from': array[i]['url_from'],
            'title': array[i]['title'],
            'url_to': array[i]['url_to'],
            'language': array[i]['language'],
            'anchor': array[i]['anchor'],
            'nofollow': array[i]['nofollow']
        }
        bk = Backlinks.objects.create(
            url_from = backlink_info['url_from'],
            title = backlink_info['title'],
            url_to = backlink_info['url_to'],
            language = backlink_info['language'],
            anchor = backlink_info['anchor'],
            nofollow = backlink_info['nofollow'],
            site_link = 'Articulo',
            session_id = session_id,
        )
        bk.save()
        i += 1

def ahref_4(array, session_id):
    lenght = len(array)
    i = 0

    while i < lenght:
        backlink_info = {
            'url_from': array[i]['url_from'],
            'title': array[i]['title'],
            'url_to': array[i]['url_to'],
            'language': array[i]['language'],
            'anchor': array[i]['anchor'],
            'nofollow': array[i]['nofollow']
        }
        bk = Backlinks.objects.create(
            url_from = backlink_info['url_from'],
            title = backlink_info['title'],
            url_to = backlink_info['url_to'],
            language = backlink_info['language'],
            anchor = backlink_info['anchor'],
            nofollow = backlink_info['nofollow'],
            site_link = 'Articulo',
            session_id = session_id,
        )
        bk.save()
        i += 1

def ahref_5(array, session_id):
    lenght = len(array)
    i = 0

    while i < lenght:
        backlink_info = {
            'url_from': array[i]['url_from'],
            'title': array[i]['title'],
            'url_to': array[i]['url_to'],
            'language': array[i]['language'],
            'anchor': array[i]['anchor'],
            'nofollow': array[i]['nofollow']
        }
        bk = Backlinks.objects.create(
            url_from = backlink_info['url_from'],
            title = backlink_info['title'],
            url_to = backlink_info['url_to'],
            language = backlink_info['language'],
            anchor = backlink_info['anchor'],
            nofollow = backlink_info['nofollow'],
            site_link = 'Articulo',
            session_id = session_id,
        )
        bk.save()
        i += 1

def ahref_6(array, session_id):
    lenght = len(array)
    i = 0

    while i < lenght:
        backlink_info = {
            'url_from': array[i]['url_from'],
            'title': array[i]['title'],
            'url_to': array[i]['url_to'],
            'language': array[i]['language'],
            'anchor': array[i]['anchor'],
            'nofollow': array[i]['nofollow']
        }
        bk = Backlinks.objects.create(
            url_from = backlink_info['url_from'],
            title = backlink_info['title'],
            url_to = backlink_info['url_to'],
            language = backlink_info['language'],
            anchor = backlink_info['anchor'],
            nofollow = backlink_info['nofollow'],
            site_link = 'Articulo',
            session_id = session_id,
        )
        bk.save()
        i += 1

def ahref_7(array, session_id):
    lenght = len(array)
    i = 0

    while i < lenght:
        backlink_info = {
            'url_from': array[i]['url_from'],
            'title': array[i]['title'],
            'url_to': array[i]['url_to'],
            'language': array[i]['language'],
            'anchor': array[i]['anchor'],
            'nofollow': array[i]['nofollow']
        }
        bk = Backlinks.objects.create(
            url_from = backlink_info['url_from'],
            title = backlink_info['title'],
            url_to = backlink_info['url_to'],
            language = backlink_info['language'],
            anchor = backlink_info['anchor'],
            nofollow = backlink_info['nofollow'],
            site_link = 'Articulo',
            session_id = session_id,
        )
        bk.save()
        i += 1

def ahref_8(array, session_id):
    lenght = len(array)
    i = 0

    while i < lenght:
        backlink_info = {
            'url_from': array[i]['url_from'],
            'title': array[i]['title'],
            'url_to': array[i]['url_to'],
            'language': array[i]['language'],
            'anchor': array[i]['anchor'],
            'nofollow': array[i]['nofollow']
        }
        bk = Backlinks.objects.create(
            url_from = backlink_info['url_from'],
            title = backlink_info['title'],
            url_to = backlink_info['url_to'],
            language = backlink_info['language'],
            anchor = backlink_info['anchor'],
            nofollow = backlink_info['nofollow'],
            site_link = 'Articulo',
            session_id = session_id,
        )
        bk.save()
        i += 1

def ahref_9(array, session_id):
    lenght = len(array)
    i = 0

    while i < lenght:
        backlink_info = {
            'url_from': array[i]['url_from'],
            'title': array[i]['title'],
            'url_to': array[i]['url_to'],
            'language': array[i]['language'],
            'anchor': array[i]['anchor'],
            'nofollow': array[i]['nofollow']
        }
        bk = Backlinks.objects.create(
            url_from = backlink_info['url_from'],
            title = backlink_info['title'],
            url_to = backlink_info['url_to'],
            language = backlink_info['language'],
            anchor = backlink_info['anchor'],
            nofollow = backlink_info['nofollow'],
            site_link = 'Articulo',
            session_id = session_id,
        )
        bk.save()
        i += 1

def ahref_10(array, session_id):
    lenght = len(array)
    i = 0

    while i < lenght:
        backlink_info = {
            'url_from': array[i]['url_from'],
            'title': array[i]['title'],
            'url_to': array[i]['url_to'],
            'language': array[i]['language'],
            'anchor': array[i]['anchor'],
            'nofollow': array[i]['nofollow']
        }
        bk = Backlinks.objects.create(
            url_from = backlink_info['url_from'],
            title = backlink_info['title'],
            url_to = backlink_info['url_to'],
            language = backlink_info['language'],
            anchor = backlink_info['anchor'],
            nofollow = backlink_info['nofollow'],
            site_link = 'Articulo',
            session_id = session_id,
        )
        bk.save()
        i += 1

def ahref_11(array, session_id):
    lenght = len(array)
    i = 0

    while i < lenght:
        backlink_info = {
            'url_from': array[i]['url_from'],
            'title': array[i]['title'],
            'url_to': array[i]['url_to'],
            'language': array[i]['language'],
            'anchor': array[i]['anchor'],
            'nofollow': array[i]['nofollow']
        }
        bk = Backlinks.objects.create(
            url_from = backlink_info['url_from'],
            title = backlink_info['title'],
            url_to = backlink_info['url_to'],
            language = backlink_info['language'],
            anchor = backlink_info['anchor'],
            nofollow = backlink_info['nofollow'],
            site_link = 'Articulo',
            session_id = session_id,
        )
        bk.save()
        i += 1

def ahref_12(array, session_id):
    lenght = len(array)
    i = 0

    while i < lenght:
        backlink_info = {
            'url_from': array[i]['url_from'],
            'title': array[i]['title'],
            'url_to': array[i]['url_to'],
            'language': array[i]['language'],
            'anchor': array[i]['anchor'],
            'nofollow': array[i]['nofollow']
        }
        bk = Backlinks.objects.create(
            url_from = backlink_info['url_from'],
            title = backlink_info['title'],
            url_to = backlink_info['url_to'],
            language = backlink_info['language'],
            anchor = backlink_info['anchor'],
            nofollow = backlink_info['nofollow'],
            site_link = 'Articulo',
            session_id = session_id,
        )
        bk.save()
        i += 1

def ahref_13(array, session_id):
    lenght = len(array)
    i = 0

    while i < lenght:
        backlink_info = {
            'url_from': array[i]['url_from'],
            'title': array[i]['title'],
            'url_to': array[i]['url_to'],
            'language': array[i]['language'],
            'anchor': array[i]['anchor'],
            'nofollow': array[i]['nofollow']
        }
        bk = Backlinks.objects.create(
            url_from = backlink_info['url_from'],
            title = backlink_info['title'],
            url_to = backlink_info['url_to'],
            language = backlink_info['language'],
            anchor = backlink_info['anchor'],
            nofollow = backlink_info['nofollow'],
            site_link = 'Articulo',
            session_id = session_id,
        )
        bk.save()
        i += 1

def ahref_14(array, session_id):
    lenght = len(array)
    i = 0

    while i < lenght:
        backlink_info = {
            'url_from': array[i]['url_from'],
            'title': array[i]['title'],
            'url_to': array[i]['url_to'],
            'language': array[i]['language'],
            'anchor': array[i]['anchor'],
            'nofollow': array[i]['nofollow']
        }
        bk = Backlinks.objects.create(
            url_from = backlink_info['url_from'],
            title = backlink_info['title'],
            url_to = backlink_info['url_to'],
            language = backlink_info['language'],
            anchor = backlink_info['anchor'],
            nofollow = backlink_info['nofollow'],
            site_link = 'Articulo',
            session_id = session_id,
        )
        bk.save()
        i += 1

def ahref_15(array, session_id):
    lenght = len(array)
    i = 0

    while i < lenght:
        backlink_info = {
            'url_from': array[i]['url_from'],
            'title': array[i]['title'],
            'url_to': array[i]['url_to'],
            'language': array[i]['language'],
            'anchor': array[i]['anchor'],
            'nofollow': array[i]['nofollow']
        }
        bk = Backlinks.objects.create(
            url_from = backlink_info['url_from'],
            title = backlink_info['title'],
            url_to = backlink_info['url_to'],
            language = backlink_info['language'],
            anchor = backlink_info['anchor'],
            nofollow = backlink_info['nofollow'],
            site_link = 'Articulo',
            session_id = session_id,
        )
        bk.save()
        i += 1

def ahref_16(array, session_id):
    lenght = len(array)
    i = 0

    while i < lenght:
        backlink_info = {
            'url_from': array[i]['url_from'],
            'title': array[i]['title'],
            'url_to': array[i]['url_to'],
            'language': array[i]['language'],
            'anchor': array[i]['anchor'],
            'nofollow': array[i]['nofollow']
        }
        bk = Backlinks.objects.create(
            url_from = backlink_info['url_from'],
            title = backlink_info['title'],
            url_to = backlink_info['url_to'],
            language = backlink_info['language'],
            anchor = backlink_info['anchor'],
            nofollow = backlink_info['nofollow'],
            site_link = 'Articulo',
            session_id = session_id,
        )
        bk.save()
        i += 1

def ahref_17(array, session_id):
    lenght = len(array)
    i = 0

    while i < lenght:
        backlink_info = {
            'url_from': array[i]['url_from'],
            'title': array[i]['title'],
            'url_to': array[i]['url_to'],
            'language': array[i]['language'],
            'anchor': array[i]['anchor'],
            'nofollow': array[i]['nofollow']
        }
        bk = Backlinks.objects.create(
            url_from = backlink_info['url_from'],
            title = backlink_info['title'],
            url_to = backlink_info['url_to'],
            language = backlink_info['language'],
            anchor = backlink_info['anchor'],
            nofollow = backlink_info['nofollow'],
            site_link = 'Articulo',
            session_id = session_id,
        )
        bk.save()
        i += 1

def ahref_18(array, session_id):
    lenght = len(array)
    i = 0

    while i < lenght:
        backlink_info = {
            'url_from': array[i]['url_from'],
            'title': array[i]['title'],
            'url_to': array[i]['url_to'],
            'language': array[i]['language'],
            'anchor': array[i]['anchor'],
            'nofollow': array[i]['nofollow']
        }
        bk = Backlinks.objects.create(
            url_from = backlink_info['url_from'],
            title = backlink_info['title'],
            url_to = backlink_info['url_to'],
            language = backlink_info['language'],
            anchor = backlink_info['anchor'],
            nofollow = backlink_info['nofollow'],
            site_link = 'Articulo',
            session_id = session_id,
        )
        bk.save()
        i += 1

def ahref_19(array, session_id):
    lenght = len(array)
    i = 0

    while i < lenght:
        backlink_info = {
            'url_from': array[i]['url_from'],
            'title': array[i]['title'],
            'url_to': array[i]['url_to'],
            'language': array[i]['language'],
            'anchor': array[i]['anchor'],
            'nofollow': array[i]['nofollow']
        }
        bk = Backlinks.objects.create(
            url_from = backlink_info['url_from'],
            title = backlink_info['title'],
            url_to = backlink_info['url_to'],
            language = backlink_info['language'],
            anchor = backlink_info['anchor'],
            nofollow = backlink_info['nofollow'],
            site_link = 'Articulo',
            session_id = session_id,
        )
        bk.save()
        i += 1
