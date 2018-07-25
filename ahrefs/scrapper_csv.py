from .models import UrlSearch, Backlinks, GoogleSearch, GoogleBD, Backlinks, ScrapperTest, SingleAhref, CSV_import

import threading
import time
import requests
from bs4 import BeautifulSoup
import urllib.request
import re

USER_AGENT = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}

def scrapper_0(array, search):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.backlink
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = search.get(pk=pk)

        if 'forum' in url or 'foro' in url:
            csv.foro = True
            csv.save()
            f_ += 1
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = csv.delete()
        else:
            try:
                response = requests.get(url, headers=USER_AGENT)
                response.raise_for_status()
                c = response.content

                soup = BeautifulSoup(c, 'html.parser')
                x_class = re.compile('com[a-z]+')
                comment_class_id = soup.find_all(['div', 'section', 'footer', 'p', 'span', 'li'], attrs={'class':x_class})
                for comment in comment_class_id:
                    comment_link = comment.find_all('a', attrs = {'rel':'nofollow'}, href=True)
                    for comment_link_to in comment_link:
                        comment_link_to = comment_link_to['href']
                        if to_url == comment_link_to:
                            s_ += 1
                        else:
                            pass
            except:
                print('no se pudo acceder a: ' + url)
                eraseTwo = csv.delete()

        if s_ > 0:
            csv.site_link = 'Comentario'
            csv.save()
        else:
            pass

        if f_ > 0:
            csv.site_link = 'Foro'
            csv.save()
        else:
            pass


def scrapper_1(array, search):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.backlink
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = search.get(pk=pk)

        if 'forum' in url or 'foro' in url:
            csv.foro = True
            csv.save()
            f_ += 1
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = csv.delete()
        else:
            try:
                response = requests.get(url, headers=USER_AGENT)
                response.raise_for_status()
                c = response.content

                soup = BeautifulSoup(c, 'html.parser')
                x_class = re.compile('com[a-z]+')
                comment_class_id = soup.find_all(['div', 'section', 'footer', 'p', 'span', 'li'], attrs={'class':x_class})
                for comment in comment_class_id:
                    comment_link = comment.find_all('a', attrs = {'rel':'nofollow'}, href=True)
                    for comment_link_to in comment_link:
                        comment_link_to = comment_link_to['href']
                        if to_url == comment_link_to:
                            s_ += 1
                        else:
                            pass
            except:
                print('no se pudo acceder a: ' + url)
                eraseTwo = csv.delete()

        if s_ > 0:
            csv.site_link = 'Comentario'
            csv.save()
        else:
            pass

        if f_ > 0:
            csv.site_link = 'Foro'
            csv.save()
        else:
            pass

def scrapper_2(array, search):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.backlink
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = search.get(pk=pk)

        if 'forum' in url or 'foro' in url:
            csv.foro = True
            csv.save()
            f_ += 1
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = csv.delete()
        else:
            try:
                response = requests.get(url, headers=USER_AGENT)
                response.raise_for_status()
                c = response.content

                soup = BeautifulSoup(c, 'html.parser')
                x_class = re.compile('com[a-z]+')
                comment_class_id = soup.find_all(['div', 'section', 'footer', 'p', 'span', 'li'], attrs={'class':x_class})
                for comment in comment_class_id:
                    comment_link = comment.find_all('a', attrs = {'rel':'nofollow'}, href=True)
                    for comment_link_to in comment_link:
                        comment_link_to = comment_link_to['href']
                        if to_url == comment_link_to:
                            s_ += 1
                        else:
                            pass
            except:
                print('no se pudo acceder a: ' + url)
                eraseTwo = csv.delete()

        if s_ > 0:
            csv.site_link = 'Comentario'
            csv.save()
        else:
            pass

        if f_ > 0:
            csv.site_link = 'Foro'
            csv.save()
        else:
            pass

def scrapper_3(array, search):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.backlink
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = search.get(pk=pk)

        if 'forum' in url or 'foro' in url:
            csv.foro = True
            csv.save()
            f_ += 1
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = csv.delete()
        else:
            try:
                response = requests.get(url, headers=USER_AGENT)
                response.raise_for_status()
                c = response.content

                soup = BeautifulSoup(c, 'html.parser')
                x_class = re.compile('com[a-z]+')
                comment_class_id = soup.find_all(['div', 'section', 'footer', 'p', 'span', 'li'], attrs={'class':x_class})
                for comment in comment_class_id:
                    comment_link = comment.find_all('a', attrs = {'rel':'nofollow'}, href=True)
                    for comment_link_to in comment_link:
                        comment_link_to = comment_link_to['href']
                        if to_url == comment_link_to:
                            s_ += 1
                        else:
                            pass
            except:
                print('no se pudo acceder a: ' + url)
                eraseTwo = csv.delete()

        if s_ > 0:
            csv.site_link = 'Comentario'
            csv.save()
        else:
            pass

        if f_ > 0:
            csv.site_link = 'Foro'
            csv.save()
        else:
            pass

def scrapper_4(array, search):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.backlink
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = search.get(pk=pk)

        if 'forum' in url or 'foro' in url:
            csv.foro = True
            csv.save()
            f_ += 1
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = csv.delete()
        else:
            try:
                response = requests.get(url, headers=USER_AGENT)
                response.raise_for_status()
                c = response.content

                soup = BeautifulSoup(c, 'html.parser')
                x_class = re.compile('com[a-z]+')
                comment_class_id = soup.find_all(['div', 'section', 'footer', 'p', 'span', 'li'], attrs={'class':x_class})
                for comment in comment_class_id:
                    comment_link = comment.find_all('a', attrs = {'rel':'nofollow'}, href=True)
                    for comment_link_to in comment_link:
                        comment_link_to = comment_link_to['href']
                        if to_url == comment_link_to:
                            s_ += 1
                        else:
                            pass
            except:
                print('no se pudo acceder a: ' + url)
                eraseTwo = csv.delete()

        if s_ > 0:
            csv.site_link = 'Comentario'
            csv.save()
        else:
            pass

        if f_ > 0:
            csv.site_link = 'Foro'
            csv.save()
        else:
            pass

def scrapper_5(array, search):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.backlink
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = search.get(pk=pk)

        if 'forum' in url or 'foro' in url:
            csv.foro = True
            csv.save()
            f_ += 1
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = csv.delete()
        else:
            try:
                response = requests.get(url, headers=USER_AGENT)
                response.raise_for_status()
                c = response.content

                soup = BeautifulSoup(c, 'html.parser')
                x_class = re.compile('com[a-z]+')
                comment_class_id = soup.find_all(['div', 'section', 'footer', 'p', 'span', 'li'], attrs={'class':x_class})
                for comment in comment_class_id:
                    comment_link = comment.find_all('a', attrs = {'rel':'nofollow'}, href=True)
                    for comment_link_to in comment_link:
                        comment_link_to = comment_link_to['href']
                        if to_url == comment_link_to:
                            s_ += 1
                        else:
                            pass
            except:
                print('no se pudo acceder a: ' + url)
                eraseTwo = csv.delete()

        if s_ > 0:
            csv.site_link = 'Comentario'
            csv.save()
        else:
            pass

        if f_ > 0:
            csv.site_link = 'Foro'
            csv.save()
        else:
            pass

def scrapper_6(array, search):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.backlink
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = search.get(pk=pk)

        if 'forum' in url or 'foro' in url:
            csv.foro = True
            csv.save()
            f_ += 1
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = csv.delete()
        else:
            try:
                response = requests.get(url, headers=USER_AGENT)
                response.raise_for_status()
                c = response.content

                soup = BeautifulSoup(c, 'html.parser')
                x_class = re.compile('com[a-z]+')
                comment_class_id = soup.find_all(['div', 'section', 'footer', 'p', 'span', 'li'], attrs={'class':x_class})
                for comment in comment_class_id:
                    comment_link = comment.find_all('a', attrs = {'rel':'nofollow'}, href=True)
                    for comment_link_to in comment_link:
                        comment_link_to = comment_link_to['href']
                        if to_url == comment_link_to:
                            s_ += 1
                        else:
                            pass
            except:
                print('no se pudo acceder a: ' + url)
                eraseTwo = csv.delete()

        if s_ > 0:
            csv.site_link = 'Comentario'
            csv.save()
        else:
            pass

        if f_ > 0:
            csv.site_link = 'Foro'
            csv.save()
        else:
            pass


def scrapper_7(array, search):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.backlink
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = search.get(pk=pk)

        if 'forum' in url or 'foro' in url:
            csv.foro = True
            csv.save()
            f_ += 1
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = csv.delete()
        else:
            try:
                response = requests.get(url, headers=USER_AGENT)
                response.raise_for_status()
                c = response.content

                soup = BeautifulSoup(c, 'html.parser')
                x_class = re.compile('com[a-z]+')
                comment_class_id = soup.find_all(['div', 'section', 'footer', 'p', 'span', 'li'], attrs={'class':x_class})
                for comment in comment_class_id:
                    comment_link = comment.find_all('a', attrs = {'rel':'nofollow'}, href=True)
                    for comment_link_to in comment_link:
                        comment_link_to = comment_link_to['href']
                        if to_url == comment_link_to:
                            s_ += 1
                        else:
                            pass
            except:
                print('no se pudo acceder a: ' + url)
                eraseTwo = csv.delete()

        if s_ > 0:
            csv.site_link = 'Comentario'
            csv.save()
        else:
            pass

        if f_ > 0:
            csv.site_link = 'Foro'
            csv.save()
        else:
            pass

def scrapper_8(array, search):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.backlink
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = search.get(pk=pk)

        if 'forum' in url or 'foro' in url:
            csv.foro = True
            csv.save()
            f_ += 1
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = csv.delete()
        else:
            try:
                response = requests.get(url, headers=USER_AGENT)
                response.raise_for_status()
                c = response.content

                soup = BeautifulSoup(c, 'html.parser')
                x_class = re.compile('com[a-z]+')
                comment_class_id = soup.find_all(['div', 'section', 'footer', 'p', 'span', 'li'], attrs={'class':x_class})
                for comment in comment_class_id:
                    comment_link = comment.find_all('a', attrs = {'rel':'nofollow'}, href=True)
                    for comment_link_to in comment_link:
                        comment_link_to = comment_link_to['href']
                        if to_url == comment_link_to:
                            s_ += 1
                        else:
                            pass
            except:
                print('no se pudo acceder a: ' + url)
                eraseTwo = csv.delete()

        if s_ > 0:
            csv.site_link = 'Comentario'
            csv.save()
        else:
            pass

        if f_ > 0:
            csv.site_link = 'Foro'
            csv.save()
        else:
            pass

def scrapper_9(array, search):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.backlink
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = search.get(pk=pk)

        if 'forum' in url or 'foro' in url:
            csv.foro = True
            csv.save()
            f_ += 1
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = csv.delete()
        else:
            try:
                response = requests.get(url, headers=USER_AGENT)
                response.raise_for_status()
                c = response.content

                soup = BeautifulSoup(c, 'html.parser')
                x_class = re.compile('com[a-z]+')
                comment_class_id = soup.find_all(['div', 'section', 'footer', 'p', 'span', 'li'], attrs={'class':x_class})
                for comment in comment_class_id:
                    comment_link = comment.find_all('a', attrs = {'rel':'nofollow'}, href=True)
                    for comment_link_to in comment_link:
                        comment_link_to = comment_link_to['href']
                        if to_url == comment_link_to:
                            s_ += 1
                        else:
                            pass
            except:
                print('no se pudo acceder a: ' + url)
                eraseTwo = csv.delete()

        if s_ > 0:
            csv.site_link = 'Comentario'
            csv.save()
        else:
            pass

        if f_ > 0:
            csv.site_link = 'Foro'
            csv.save()
        else:
            pass

def scrapper_10(array, search):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.backlink
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = search.get(pk=pk)

        if 'forum' in url or 'foro' in url:
            csv.foro = True
            csv.save()
            f_ += 1
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = csv.delete()
        else:
            try:
                response = requests.get(url, headers=USER_AGENT)
                response.raise_for_status()
                c = response.content

                soup = BeautifulSoup(c, 'html.parser')
                x_class = re.compile('com[a-z]+')
                comment_class_id = soup.find_all(['div', 'section', 'footer', 'p', 'span', 'li'], attrs={'class':x_class})
                for comment in comment_class_id:
                    comment_link = comment.find_all('a', attrs = {'rel':'nofollow'}, href=True)
                    for comment_link_to in comment_link:
                        comment_link_to = comment_link_to['href']
                        if to_url == comment_link_to:
                            s_ += 1
                        else:
                            pass
            except:
                print('no se pudo acceder a: ' + url)
                eraseTwo = csv.delete()

        if s_ > 0:
            csv.site_link = 'Comentario'
            csv.save()
        else:
            pass

        if f_ > 0:
            csv.site_link = 'Foro'
            csv.save()
        else:
            pass


def scrapper_11(array, search):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.backlink
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = search.get(pk=pk)

        if 'forum' in url or 'foro' in url:
            csv.foro = True
            csv.save()
            f_ += 1
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = csv.delete()
        else:
            try:
                response = requests.get(url, headers=USER_AGENT)
                response.raise_for_status()
                c = response.content

                soup = BeautifulSoup(c, 'html.parser')
                x_class = re.compile('com[a-z]+')
                comment_class_id = soup.find_all(['div', 'section', 'footer', 'p', 'span', 'li'], attrs={'class':x_class})
                for comment in comment_class_id:
                    comment_link = comment.find_all('a', attrs = {'rel':'nofollow'}, href=True)
                    for comment_link_to in comment_link:
                        comment_link_to = comment_link_to['href']
                        if to_url == comment_link_to:
                            s_ += 1
                        else:
                            pass
            except:
                print('no se pudo acceder a: ' + url)
                eraseTwo = csv.delete()

        if s_ > 0:
            csv.site_link = 'Comentario'
            csv.save()
        else:
            pass

        if f_ > 0:
            csv.site_link = 'Foro'
            csv.save()
        else:
            pass


def scrapper_12(array, search):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.backlink
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = search.get(pk=pk)

        if 'forum' in url or 'foro' in url:
            csv.foro = True
            csv.save()
            f_ += 1
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = csv.delete()
        else:
            try:
                response = requests.get(url, headers=USER_AGENT)
                response.raise_for_status()
                c = response.content

                soup = BeautifulSoup(c, 'html.parser')
                x_class = re.compile('com[a-z]+')
                comment_class_id = soup.find_all(['div', 'section', 'footer', 'p', 'span', 'li'], attrs={'class':x_class})
                for comment in comment_class_id:
                    comment_link = comment.find_all('a', attrs = {'rel':'nofollow'}, href=True)
                    for comment_link_to in comment_link:
                        comment_link_to = comment_link_to['href']
                        if to_url == comment_link_to:
                            s_ += 1
                        else:
                            pass
            except:
                print('no se pudo acceder a: ' + url)
                eraseTwo = csv.delete()

        if s_ > 0:
            csv.site_link = 'Comentario'
            csv.save()
        else:
            pass

        if f_ > 0:
            csv.site_link = 'Foro'
            csv.save()
        else:
            pass

def scrapper_13(array, search):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.backlink
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = search.get(pk=pk)

        if 'forum' in url or 'foro' in url:
            csv.foro = True
            csv.save()
            f_ += 1
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = csv.delete()
        else:
            try:
                response = requests.get(url, headers=USER_AGENT)
                response.raise_for_status()
                c = response.content

                soup = BeautifulSoup(c, 'html.parser')
                x_class = re.compile('com[a-z]+')
                comment_class_id = soup.find_all(['div', 'section', 'footer', 'p', 'span', 'li'], attrs={'class':x_class})
                for comment in comment_class_id:
                    comment_link = comment.find_all('a', attrs = {'rel':'nofollow'}, href=True)
                    for comment_link_to in comment_link:
                        comment_link_to = comment_link_to['href']
                        if to_url == comment_link_to:
                            s_ += 1
                        else:
                            pass
            except:
                print('no se pudo acceder a: ' + url)
                eraseTwo = csv.delete()

        if s_ > 0:
            csv.site_link = 'Comentario'
            csv.save()
        else:
            pass

        if f_ > 0:
            csv.site_link = 'Foro'
            csv.save()
        else:
            pass

def scrapper_14(array, search):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.backlink
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = search.get(pk=pk)

        if 'forum' in url or 'foro' in url:
            csv.foro = True
            csv.save()
            f_ += 1
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = csv.delete()
        else:
            try:
                response = requests.get(url, headers=USER_AGENT)
                response.raise_for_status()
                c = response.content

                soup = BeautifulSoup(c, 'html.parser')
                x_class = re.compile('com[a-z]+')
                comment_class_id = soup.find_all(['div', 'section', 'footer', 'p', 'span', 'li'], attrs={'class':x_class})
                for comment in comment_class_id:
                    comment_link = comment.find_all('a', attrs = {'rel':'nofollow'}, href=True)
                    for comment_link_to in comment_link:
                        comment_link_to = comment_link_to['href']
                        if to_url == comment_link_to:
                            s_ += 1
                        else:
                            pass
            except:
                print('no se pudo acceder a: ' + url)
                eraseTwo = csv.delete()

        if s_ > 0:
            csv.site_link = 'Comentario'
            csv.save()
        else:
            pass

        if f_ > 0:
            csv.site_link = 'Foro'
            csv.save()
        else:
            pass

def scrapper_15(array, search):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.backlink
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = search.get(pk=pk)

        if 'forum' in url or 'foro' in url:
            csv.foro = True
            csv.save()
            f_ += 1
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = csv.delete()
        else:
            try:
                response = requests.get(url, headers=USER_AGENT)
                response.raise_for_status()
                c = response.content

                soup = BeautifulSoup(c, 'html.parser')
                x_class = re.compile('com[a-z]+')
                comment_class_id = soup.find_all(['div', 'section', 'footer', 'p', 'span', 'li'], attrs={'class':x_class})
                for comment in comment_class_id:
                    comment_link = comment.find_all('a', attrs = {'rel':'nofollow'}, href=True)
                    for comment_link_to in comment_link:
                        comment_link_to = comment_link_to['href']
                        if to_url == comment_link_to:
                            s_ += 1
                        else:
                            pass
            except:
                print('no se pudo acceder a: ' + url)
                eraseTwo = csv.delete()

        if s_ > 0:
            csv.site_link = 'Comentario'
            csv.save()
        else:
            pass

        if f_ > 0:
            csv.site_link = 'Foro'
            csv.save()
        else:
            pass

def scrapper_16(array, search):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.backlink
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = search.get(pk=pk)

        if 'forum' in url or 'foro' in url:
            csv.foro = True
            csv.save()
            f_ += 1
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = csv.delete()
        else:
            try:
                response = requests.get(url, headers=USER_AGENT)
                response.raise_for_status()
                c = response.content

                soup = BeautifulSoup(c, 'html.parser')
                x_class = re.compile('com[a-z]+')
                comment_class_id = soup.find_all(['div', 'section', 'footer', 'p', 'span', 'li'], attrs={'class':x_class})
                for comment in comment_class_id:
                    comment_link = comment.find_all('a', attrs = {'rel':'nofollow'}, href=True)
                    for comment_link_to in comment_link:
                        comment_link_to = comment_link_to['href']
                        if to_url == comment_link_to:
                            s_ += 1
                        else:
                            pass
            except:
                print('no se pudo acceder a: ' + url)
                eraseTwo = csv.delete()

        if s_ > 0:
            csv.site_link = 'Comentario'
            csv.save()
        else:
            pass

        if f_ > 0:
            csv.site_link = 'Foro'
            csv.save()
        else:
            pass

def scrapper_17(array, search):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.backlink
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = search.get(pk=pk)

        if 'forum' in url or 'foro' in url:
            csv.foro = True
            csv.save()
            f_ += 1
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = csv.delete()
        else:
            try:
                response = requests.get(url, headers=USER_AGENT)
                response.raise_for_status()
                c = response.content

                soup = BeautifulSoup(c, 'html.parser')
                x_class = re.compile('com[a-z]+')
                comment_class_id = soup.find_all(['div', 'section', 'footer', 'p', 'span', 'li'], attrs={'class':x_class})
                for comment in comment_class_id:
                    comment_link = comment.find_all('a', attrs = {'rel':'nofollow'}, href=True)
                    for comment_link_to in comment_link:
                        comment_link_to = comment_link_to['href']
                        if to_url == comment_link_to:
                            s_ += 1
                        else:
                            pass
            except:
                print('no se pudo acceder a: ' + url)
                eraseTwo = csv.delete()

        if s_ > 0:
            csv.site_link = 'Comentario'
            csv.save()
        else:
            pass

        if f_ > 0:
            csv.site_link = 'Foro'
            csv.save()
        else:
            pass


def scrapper_18(array, search):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.backlink
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = search.get(pk=pk)

        if 'forum' in url or 'foro' in url:
            csv.foro = True
            csv.save()
            f_ += 1
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = csv.delete()
        else:
            try:
                response = requests.get(url, headers=USER_AGENT)
                response.raise_for_status()
                c = response.content

                soup = BeautifulSoup(c, 'html.parser')
                x_class = re.compile('com[a-z]+')
                comment_class_id = soup.find_all(['div', 'section', 'footer', 'p', 'span', 'li'], attrs={'class':x_class})
                for comment in comment_class_id:
                    comment_link = comment.find_all('a', attrs = {'rel':'nofollow'}, href=True)
                    for comment_link_to in comment_link:
                        comment_link_to = comment_link_to['href']
                        if to_url == comment_link_to:
                            s_ += 1
                        else:
                            pass
            except:
                print('no se pudo acceder a: ' + url)
                eraseTwo = csv.delete()

        if s_ > 0:
            csv.site_link = 'Comentario'
            csv.save()
        else:
            pass

        if f_ > 0:
            csv.site_link = 'Foro'
            csv.save()
        else:
            pass

def scrapper_19(array, search):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.backlink
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = search.get(pk=pk)

        if 'forum' in url or 'foro' in url:
            csv.foro = True
            csv.save()
            f_ += 1
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = csv.delete()
        else:
            try:
                response = requests.get(url, headers=USER_AGENT)
                response.raise_for_status()
                c = response.content

                soup = BeautifulSoup(c, 'html.parser')
                x_class = re.compile('com[a-z]+')
                comment_class_id = soup.find_all(['div', 'section', 'footer', 'p', 'span', 'li'], attrs={'class':x_class})
                for comment in comment_class_id:
                    comment_link = comment.find_all('a', attrs = {'rel':'nofollow'}, href=True)
                    for comment_link_to in comment_link:
                        comment_link_to = comment_link_to['href']
                        if to_url == comment_link_to:
                            s_ += 1
                        else:
                            pass
            except:
                print('no se pudo acceder a: ' + url)
                eraseTwo = csv.delete()

        if s_ > 0:
            csv.site_link = 'Comentario'
            csv.save()
        else:
            pass

        if f_ > 0:
            csv.site_link = 'Foro'
            csv.save()
        else:
            pass

def scrapper_20(array, search):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.backlink
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = search.get(pk=pk)

        if 'forum' in url or 'foro' in url:
            csv.foro = True
            csv.save()
            f_ += 1
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = csv.delete()
        else:
            try:
                response = requests.get(url, headers=USER_AGENT)
                response.raise_for_status()
                c = response.content

                soup = BeautifulSoup(c, 'html.parser')
                x_class = re.compile('com[a-z]+')
                comment_class_id = soup.find_all(['div', 'section', 'footer', 'p', 'span', 'li'], attrs={'class':x_class})
                for comment in comment_class_id:
                    comment_link = comment.find_all('a', attrs = {'rel':'nofollow'}, href=True)
                    for comment_link_to in comment_link:
                        comment_link_to = comment_link_to['href']
                        if to_url == comment_link_to:
                            s_ += 1
                        else:
                            pass
            except:
                print('no se pudo acceder a: ' + url)
                eraseTwo = csv.delete()

        if s_ > 0:
            csv.site_link = 'Comentario'
            csv.save()
        else:
            pass

        if f_ > 0:
            csv.site_link = 'Foro'
            csv.save()
        else:
            pass


def scrapper_21(array, search):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.backlink
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = search.get(pk=pk)

        if 'forum' in url or 'foro' in url:
            csv.foro = True
            csv.save()
            f_ += 1
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = csv.delete()
        else:
            try:
                response = requests.get(url, headers=USER_AGENT)
                response.raise_for_status()
                c = response.content

                soup = BeautifulSoup(c, 'html.parser')
                x_class = re.compile('com[a-z]+')
                comment_class_id = soup.find_all(['div', 'section', 'footer', 'p', 'span', 'li'], attrs={'class':x_class})
                for comment in comment_class_id:
                    comment_link = comment.find_all('a', attrs = {'rel':'nofollow'}, href=True)
                    for comment_link_to in comment_link:
                        comment_link_to = comment_link_to['href']
                        if to_url == comment_link_to:
                            s_ += 1
                        else:
                            pass
            except:
                print('no se pudo acceder a: ' + url)
                eraseTwo = csv.delete()

        if s_ > 0:
            csv.site_link = 'Comentario'
            csv.save()
        else:
            pass

        if f_ > 0:
            csv.site_link = 'Foro'
            csv.save()
        else:
            pass

def scrapper_22(array, search):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.backlink
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = search.get(pk=pk)

        if 'forum' in url or 'foro' in url:
            csv.foro = True
            csv.save()
            f_ += 1
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = csv.delete()
        else:
            try:
                response = requests.get(url, headers=USER_AGENT)
                response.raise_for_status()
                c = response.content

                soup = BeautifulSoup(c, 'html.parser')
                x_class = re.compile('com[a-z]+')
                comment_class_id = soup.find_all(['div', 'section', 'footer', 'p', 'span', 'li'], attrs={'class':x_class})
                for comment in comment_class_id:
                    comment_link = comment.find_all('a', attrs = {'rel':'nofollow'}, href=True)
                    for comment_link_to in comment_link:
                        comment_link_to = comment_link_to['href']
                        if to_url == comment_link_to:
                            s_ += 1
                        else:
                            pass
            except:
                print('no se pudo acceder a: ' + url)
                eraseTwo = csv.delete()

        if s_ > 0:
            csv.site_link = 'Comentario'
            csv.save()
        else:
            pass

        if f_ > 0:
            csv.site_link = 'Foro'
            csv.save()
        else:
            pass

def scrapper_23(array, search):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.backlink
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = search.get(pk=pk)

        if 'forum' in url or 'foro' in url:
            csv.foro = True
            csv.save()
            f_ += 1
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = csv.delete()
        else:
            try:
                response = requests.get(url, headers=USER_AGENT)
                response.raise_for_status()
                c = response.content

                soup = BeautifulSoup(c, 'html.parser')
                x_class = re.compile('com[a-z]+')
                comment_class_id = soup.find_all(['div', 'section', 'footer', 'p', 'span', 'li'], attrs={'class':x_class})
                for comment in comment_class_id:
                    comment_link = comment.find_all('a', attrs = {'rel':'nofollow'}, href=True)
                    for comment_link_to in comment_link:
                        comment_link_to = comment_link_to['href']
                        if to_url == comment_link_to:
                            s_ += 1
                        else:
                            pass
            except:
                print('no se pudo acceder a: ' + url)
                eraseTwo = csv.delete()

        if s_ > 0:
            csv.site_link = 'Comentario'
            csv.save()
        else:
            pass

        if f_ > 0:
            csv.site_link = 'Foro'
            csv.save()
        else:
            pass

def scrapper_24(array, search):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.backlink
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = search.get(pk=pk)

        if 'forum' in url or 'foro' in url:
            csv.foro = True
            csv.save()
            f_ += 1
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = csv.delete()
        else:
            try:
                response = requests.get(url, headers=USER_AGENT)
                response.raise_for_status()
                c = response.content

                soup = BeautifulSoup(c, 'html.parser')
                x_class = re.compile('com[a-z]+')
                comment_class_id = soup.find_all(['div', 'section', 'footer', 'p', 'span', 'li'], attrs={'class':x_class})
                for comment in comment_class_id:
                    comment_link = comment.find_all('a', attrs = {'rel':'nofollow'}, href=True)
                    for comment_link_to in comment_link:
                        comment_link_to = comment_link_to['href']
                        if to_url == comment_link_to:
                            s_ += 1
                        else:
                            pass
            except:
                print('no se pudo acceder a: ' + url)
                eraseTwo = csv.delete()

        if s_ > 0:
            csv.site_link = 'Comentario'
            csv.save()
        else:
            pass

        if f_ > 0:
            csv.site_link = 'Foro'
            csv.save()
        else:
            pass

def scrapper_25(array, search):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.backlink
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = search.get(pk=pk)

        if 'forum' in url or 'foro' in url:
            csv.foro = True
            csv.save()
            f_ += 1
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = csv.delete()
        else:
            try:
                response = requests.get(url, headers=USER_AGENT)
                response.raise_for_status()
                c = response.content

                soup = BeautifulSoup(c, 'html.parser')
                x_class = re.compile('com[a-z]+')
                comment_class_id = soup.find_all(['div', 'section', 'footer', 'p', 'span', 'li'], attrs={'class':x_class})
                for comment in comment_class_id:
                    comment_link = comment.find_all('a', attrs = {'rel':'nofollow'}, href=True)
                    for comment_link_to in comment_link:
                        comment_link_to = comment_link_to['href']
                        if to_url == comment_link_to:
                            s_ += 1
                        else:
                            pass
            except:
                print('no se pudo acceder a: ' + url)
                eraseTwo = csv.delete()

        if s_ > 0:
            csv.site_link = 'Comentario'
            csv.save()
        else:
            pass

        if f_ > 0:
            csv.site_link = 'Foro'
            csv.save()
        else:
            pass

def scrapper_26(array, search):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.backlink
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = search.get(pk=pk)

        if 'forum' in url or 'foro' in url:
            csv.foro = True
            csv.save()
            f_ += 1
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = csv.delete()
        else:
            try:
                response = requests.get(url, headers=USER_AGENT)
                response.raise_for_status()
                c = response.content

                soup = BeautifulSoup(c, 'html.parser')
                x_class = re.compile('com[a-z]+')
                comment_class_id = soup.find_all(['div', 'section', 'footer', 'p', 'span', 'li'], attrs={'class':x_class})
                for comment in comment_class_id:
                    comment_link = comment.find_all('a', attrs = {'rel':'nofollow'}, href=True)
                    for comment_link_to in comment_link:
                        comment_link_to = comment_link_to['href']
                        if to_url == comment_link_to:
                            s_ += 1
                        else:
                            pass
            except:
                print('no se pudo acceder a: ' + url)
                eraseTwo = csv.delete()

        if s_ > 0:
            csv.site_link = 'Comentario'
            csv.save()
        else:
            pass

        if f_ > 0:
            csv.site_link = 'Foro'
            csv.save()
        else:
            pass


def scrapper_27(array, search):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.backlink
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = search.get(pk=pk)

        if 'forum' in url or 'foro' in url:
            csv.foro = True
            csv.save()
            f_ += 1
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = csv.delete()
        else:
            try:
                response = requests.get(url, headers=USER_AGENT)
                response.raise_for_status()
                c = response.content

                soup = BeautifulSoup(c, 'html.parser')
                x_class = re.compile('com[a-z]+')
                comment_class_id = soup.find_all(['div', 'section', 'footer', 'p', 'span', 'li'], attrs={'class':x_class})
                for comment in comment_class_id:
                    comment_link = comment.find_all('a', attrs = {'rel':'nofollow'}, href=True)
                    for comment_link_to in comment_link:
                        comment_link_to = comment_link_to['href']
                        if to_url == comment_link_to:
                            s_ += 1
                        else:
                            pass
            except:
                print('no se pudo acceder a: ' + url)
                eraseTwo = csv.delete()

        if s_ > 0:
            csv.site_link = 'Comentario'
            csv.save()
        else:
            pass

        if f_ > 0:
            csv.site_link = 'Foro'
            csv.save()
        else:
            pass

def scrapper_28(array, search):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.backlink
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = search.get(pk=pk)

        if 'forum' in url or 'foro' in url:
            csv.foro = True
            csv.save()
            f_ += 1
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = csv.delete()
        else:
            try:
                response = requests.get(url, headers=USER_AGENT)
                response.raise_for_status()
                c = response.content

                soup = BeautifulSoup(c, 'html.parser')
                x_class = re.compile('com[a-z]+')
                comment_class_id = soup.find_all(['div', 'section', 'footer', 'p', 'span', 'li'], attrs={'class':x_class})
                for comment in comment_class_id:
                    comment_link = comment.find_all('a', attrs = {'rel':'nofollow'}, href=True)
                    for comment_link_to in comment_link:
                        comment_link_to = comment_link_to['href']
                        if to_url == comment_link_to:
                            s_ += 1
                        else:
                            pass
            except:
                print('no se pudo acceder a: ' + url)
                eraseTwo = csv.delete()

        if s_ > 0:
            csv.site_link = 'Comentario'
            csv.save()
        else:
            pass

        if f_ > 0:
            csv.site_link = 'Foro'
            csv.save()
        else:
            pass

def scrapper_29(array, search):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.backlink
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = search.get(pk=pk)

        if 'forum' in url or 'foro' in url:
            csv.foro = True
            csv.save()
            f_ += 1
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = csv.delete()
        else:
            try:
                response = requests.get(url, headers=USER_AGENT)
                response.raise_for_status()
                c = response.content

                soup = BeautifulSoup(c, 'html.parser')
                x_class = re.compile('com[a-z]+')
                comment_class_id = soup.find_all(['div', 'section', 'footer', 'p', 'span', 'li'], attrs={'class':x_class})
                for comment in comment_class_id:
                    comment_link = comment.find_all('a', attrs = {'rel':'nofollow'}, href=True)
                    for comment_link_to in comment_link:
                        comment_link_to = comment_link_to['href']
                        if to_url == comment_link_to:
                            s_ += 1
                        else:
                            pass
            except:
                print('no se pudo acceder a: ' + url)
                eraseTwo = csv.delete()

        if s_ > 0:
            csv.site_link = 'Comentario'
            csv.save()
        else:
            pass

        if f_ > 0:
            csv.site_link = 'Foro'
            csv.save()
        else:
            pass

def scrapper_30(array, search):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.backlink
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = search.get(pk=pk)

        if 'forum' in url or 'foro' in url:
            csv.foro = True
            csv.save()
            f_ += 1
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = csv.delete()
        else:
            try:
                response = requests.get(url, headers=USER_AGENT)
                response.raise_for_status()
                c = response.content

                soup = BeautifulSoup(c, 'html.parser')
                x_class = re.compile('com[a-z]+')
                comment_class_id = soup.find_all(['div', 'section', 'footer', 'p', 'span', 'li'], attrs={'class':x_class})
                for comment in comment_class_id:
                    comment_link = comment.find_all('a', attrs = {'rel':'nofollow'}, href=True)
                    for comment_link_to in comment_link:
                        comment_link_to = comment_link_to['href']
                        if to_url == comment_link_to:
                            s_ += 1
                        else:
                            pass
            except:
                print('no se pudo acceder a: ' + url)
                eraseTwo = csv.delete()

        if s_ > 0:
            csv.site_link = 'Comentario'
            csv.save()
        else:
            pass

        if f_ > 0:
            csv.site_link = 'Foro'
            csv.save()
        else:
            pass


def scrapper_31(array, search):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.backlink
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = search.get(pk=pk)

        if 'forum' in url or 'foro' in url:
            csv.foro = True
            csv.save()
            f_ += 1
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = csv.delete()
        else:
            try:
                response = requests.get(url, headers=USER_AGENT)
                response.raise_for_status()
                c = response.content

                soup = BeautifulSoup(c, 'html.parser')
                x_class = re.compile('com[a-z]+')
                comment_class_id = soup.find_all(['div', 'section', 'footer', 'p', 'span', 'li'], attrs={'class':x_class})
                for comment in comment_class_id:
                    comment_link = comment.find_all('a', attrs = {'rel':'nofollow'}, href=True)
                    for comment_link_to in comment_link:
                        comment_link_to = comment_link_to['href']
                        if to_url == comment_link_to:
                            s_ += 1
                        else:
                            pass
            except:
                print('no se pudo acceder a: ' + url)
                eraseTwo = csv.delete()

        if s_ > 0:
            csv.site_link = 'Comentario'
            csv.save()
        else:
            pass

        if f_ > 0:
            csv.site_link = 'Foro'
            csv.save()
        else:
            pass


def scrapper_32(array, search):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.backlink
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = search.get(pk=pk)

        if 'forum' in url or 'foro' in url:
            csv.foro = True
            csv.save()
            f_ += 1
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = csv.delete()
        else:
            try:
                response = requests.get(url, headers=USER_AGENT)
                response.raise_for_status()
                c = response.content

                soup = BeautifulSoup(c, 'html.parser')
                x_class = re.compile('com[a-z]+')
                comment_class_id = soup.find_all(['div', 'section', 'footer', 'p', 'span', 'li'], attrs={'class':x_class})
                for comment in comment_class_id:
                    comment_link = comment.find_all('a', attrs = {'rel':'nofollow'}, href=True)
                    for comment_link_to in comment_link:
                        comment_link_to = comment_link_to['href']
                        if to_url == comment_link_to:
                            s_ += 1
                        else:
                            pass
            except:
                print('no se pudo acceder a: ' + url)
                eraseTwo = csv.delete()

        if s_ > 0:
            csv.site_link = 'Comentario'
            csv.save()
        else:
            pass

        if f_ > 0:
            csv.site_link = 'Foro'
            csv.save()
        else:
            pass

def scrapper_33(array, search):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.backlink
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = search.get(pk=pk)

        if 'forum' in url or 'foro' in url:
            csv.foro = True
            csv.save()
            f_ += 1
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = csv.delete()
        else:
            try:
                response = requests.get(url, headers=USER_AGENT)
                response.raise_for_status()
                c = response.content

                soup = BeautifulSoup(c, 'html.parser')
                x_class = re.compile('com[a-z]+')
                comment_class_id = soup.find_all(['div', 'section', 'footer', 'p', 'span', 'li'], attrs={'class':x_class})
                for comment in comment_class_id:
                    comment_link = comment.find_all('a', attrs = {'rel':'nofollow'}, href=True)
                    for comment_link_to in comment_link:
                        comment_link_to = comment_link_to['href']
                        if to_url == comment_link_to:
                            s_ += 1
                        else:
                            pass
            except:
                print('no se pudo acceder a: ' + url)
                eraseTwo = csv.delete()

        if s_ > 0:
            csv.site_link = 'Comentario'
            csv.save()
        else:
            pass

        if f_ > 0:
            csv.site_link = 'Foro'
            csv.save()
        else:
            pass

def scrapper_34(array, search):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.backlink
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = search.get(pk=pk)

        if 'forum' in url or 'foro' in url:
            csv.foro = True
            csv.save()
            f_ += 1
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = csv.delete()
        else:
            try:
                response = requests.get(url, headers=USER_AGENT)
                response.raise_for_status()
                c = response.content

                soup = BeautifulSoup(c, 'html.parser')
                x_class = re.compile('com[a-z]+')
                comment_class_id = soup.find_all(['div', 'section', 'footer', 'p', 'span', 'li'], attrs={'class':x_class})
                for comment in comment_class_id:
                    comment_link = comment.find_all('a', attrs = {'rel':'nofollow'}, href=True)
                    for comment_link_to in comment_link:
                        comment_link_to = comment_link_to['href']
                        if to_url == comment_link_to:
                            s_ += 1
                        else:
                            pass
            except:
                print('no se pudo acceder a: ' + url)
                eraseTwo = csv.delete()

        if s_ > 0:
            csv.site_link = 'Comentario'
            csv.save()
        else:
            pass

        if f_ > 0:
            csv.site_link = 'Foro'
            csv.save()
        else:
            pass

def scrapper_35(array, search):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.backlink
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = search.get(pk=pk)

        if 'forum' in url or 'foro' in url:
            csv.foro = True
            csv.save()
            f_ += 1
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = csv.delete()
        else:
            try:
                response = requests.get(url, headers=USER_AGENT)
                response.raise_for_status()
                c = response.content

                soup = BeautifulSoup(c, 'html.parser')
                x_class = re.compile('com[a-z]+')
                comment_class_id = soup.find_all(['div', 'section', 'footer', 'p', 'span', 'li'], attrs={'class':x_class})
                for comment in comment_class_id:
                    comment_link = comment.find_all('a', attrs = {'rel':'nofollow'}, href=True)
                    for comment_link_to in comment_link:
                        comment_link_to = comment_link_to['href']
                        if to_url == comment_link_to:
                            s_ += 1
                        else:
                            pass
            except:
                print('no se pudo acceder a: ' + url)
                eraseTwo = csv.delete()

        if s_ > 0:
            csv.site_link = 'Comentario'
            csv.save()
        else:
            pass

        if f_ > 0:
            csv.site_link = 'Foro'
            csv.save()
        else:
            pass

def scrapper_36(array, search):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.backlink
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = search.get(pk=pk)

        if 'forum' in url or 'foro' in url:
            csv.foro = True
            csv.save()
            f_ += 1
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = csv.delete()
        else:
            try:
                response = requests.get(url, headers=USER_AGENT)
                response.raise_for_status()
                c = response.content

                soup = BeautifulSoup(c, 'html.parser')
                x_class = re.compile('com[a-z]+')
                comment_class_id = soup.find_all(['div', 'section', 'footer', 'p', 'span', 'li'], attrs={'class':x_class})
                for comment in comment_class_id:
                    comment_link = comment.find_all('a', attrs = {'rel':'nofollow'}, href=True)
                    for comment_link_to in comment_link:
                        comment_link_to = comment_link_to['href']
                        if to_url == comment_link_to:
                            s_ += 1
                        else:
                            pass
            except:
                print('no se pudo acceder a: ' + url)
                eraseTwo = csv.delete()

        if s_ > 0:
            csv.site_link = 'Comentario'
            csv.save()
        else:
            pass

        if f_ > 0:
            csv.site_link = 'Foro'
            csv.save()
        else:
            pass

def scrapper_37(array, search):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.backlink
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = search.get(pk=pk)

        if 'forum' in url or 'foro' in url:
            csv.foro = True
            csv.save()
            f_ += 1
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = csv.delete()
        else:
            try:
                response = requests.get(url, headers=USER_AGENT)
                response.raise_for_status()
                c = response.content

                soup = BeautifulSoup(c, 'html.parser')
                x_class = re.compile('com[a-z]+')
                comment_class_id = soup.find_all(['div', 'section', 'footer', 'p', 'span', 'li'], attrs={'class':x_class})
                for comment in comment_class_id:
                    comment_link = comment.find_all('a', attrs = {'rel':'nofollow'}, href=True)
                    for comment_link_to in comment_link:
                        comment_link_to = comment_link_to['href']
                        if to_url == comment_link_to:
                            s_ += 1
                        else:
                            pass
            except:
                print('no se pudo acceder a: ' + url)
                eraseTwo = csv.delete()

        if s_ > 0:
            csv.site_link = 'Comentario'
            csv.save()
        else:
            pass

        if f_ > 0:
            csv.site_link = 'Foro'
            csv.save()
        else:
            pass


def scrapper_38(array, search):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.backlink
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = search.get(pk=pk)

        if 'forum' in url or 'foro' in url:
            csv.foro = True
            csv.save()
            f_ += 1
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = csv.delete()
        else:
            try:
                response = requests.get(url, headers=USER_AGENT)
                response.raise_for_status()
                c = response.content

                soup = BeautifulSoup(c, 'html.parser')
                x_class = re.compile('com[a-z]+')
                comment_class_id = soup.find_all(['div', 'section', 'footer', 'p', 'span', 'li'], attrs={'class':x_class})
                for comment in comment_class_id:
                    comment_link = comment.find_all('a', attrs = {'rel':'nofollow'}, href=True)
                    for comment_link_to in comment_link:
                        comment_link_to = comment_link_to['href']
                        if to_url == comment_link_to:
                            s_ += 1
                        else:
                            pass
            except:
                print('no se pudo acceder a: ' + url)
                eraseTwo = csv.delete()

        if s_ > 0:
            csv.site_link = 'Comentario'
            csv.save()
        else:
            pass

        if f_ > 0:
            csv.site_link = 'Foro'
            csv.save()
        else:
            pass

def scrapper_39(array, search):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.backlink
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = search.get(pk=pk)

        if 'forum' in url or 'foro' in url:
            csv.foro = True
            csv.save()
            f_ += 1
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = csv.delete()
        else:
            try:
                response = requests.get(url, headers=USER_AGENT)
                response.raise_for_status()
                c = response.content

                soup = BeautifulSoup(c, 'html.parser')
                x_class = re.compile('com[a-z]+')
                comment_class_id = soup.find_all(['div', 'section', 'footer', 'p', 'span', 'li'], attrs={'class':x_class})
                for comment in comment_class_id:
                    comment_link = comment.find_all('a', attrs = {'rel':'nofollow'}, href=True)
                    for comment_link_to in comment_link:
                        comment_link_to = comment_link_to['href']
                        if to_url == comment_link_to:
                            s_ += 1
                        else:
                            pass
            except:
                print('no se pudo acceder a: ' + url)
                eraseTwo = csv.delete()

        if s_ > 0:
            csv.site_link = 'Comentario'
            csv.save()
        else:
            pass

        if f_ > 0:
            csv.site_link = 'Foro'
            csv.save()
        else:
            pass

def scrapper_40(array, search):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.backlink
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = search.get(pk=pk)

        if 'forum' in url or 'foro' in url:
            csv.foro = True
            csv.save()
            f_ += 1
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = csv.delete()
        else:
            try:
                response = requests.get(url, headers=USER_AGENT)
                response.raise_for_status()
                c = response.content

                soup = BeautifulSoup(c, 'html.parser')
                x_class = re.compile('com[a-z]+')
                comment_class_id = soup.find_all(['div', 'section', 'footer', 'p', 'span', 'li'], attrs={'class':x_class})
                for comment in comment_class_id:
                    comment_link = comment.find_all('a', attrs = {'rel':'nofollow'}, href=True)
                    for comment_link_to in comment_link:
                        comment_link_to = comment_link_to['href']
                        if to_url == comment_link_to:
                            s_ += 1
                        else:
                            pass
            except:
                print('no se pudo acceder a: ' + url)
                eraseTwo = csv.delete()

        if s_ > 0:
            csv.site_link = 'Comentario'
            csv.save()
        else:
            pass

        if f_ > 0:
            csv.site_link = 'Foro'
            csv.save()
        else:
            pass


def scrapper_41(array, search):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.backlink
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = search.get(pk=pk)

        if 'forum' in url or 'foro' in url:
            csv.foro = True
            csv.save()
            f_ += 1
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = csv.delete()
        else:
            try:
                response = requests.get(url, headers=USER_AGENT)
                response.raise_for_status()
                c = response.content

                soup = BeautifulSoup(c, 'html.parser')
                x_class = re.compile('com[a-z]+')
                comment_class_id = soup.find_all(['div', 'section', 'footer', 'p', 'span', 'li'], attrs={'class':x_class})
                for comment in comment_class_id:
                    comment_link = comment.find_all('a', attrs = {'rel':'nofollow'}, href=True)
                    for comment_link_to in comment_link:
                        comment_link_to = comment_link_to['href']
                        if to_url == comment_link_to:
                            s_ += 1
                        else:
                            pass
            except:
                print('no se pudo acceder a: ' + url)
                eraseTwo = csv.delete()

        if s_ > 0:
            csv.site_link = 'Comentario'
            csv.save()
        else:
            pass

        if f_ > 0:
            csv.site_link = 'Foro'
            csv.save()
        else:
            pass

def scrapper_42(array, search):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.backlink
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = search.get(pk=pk)

        if 'forum' in url or 'foro' in url:
            csv.foro = True
            csv.save()
            f_ += 1
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = csv.delete()
        else:
            try:
                response = requests.get(url, headers=USER_AGENT)
                response.raise_for_status()
                c = response.content

                soup = BeautifulSoup(c, 'html.parser')
                x_class = re.compile('com[a-z]+')
                comment_class_id = soup.find_all(['div', 'section', 'footer', 'p', 'span', 'li'], attrs={'class':x_class})
                for comment in comment_class_id:
                    comment_link = comment.find_all('a', attrs = {'rel':'nofollow'}, href=True)
                    for comment_link_to in comment_link:
                        comment_link_to = comment_link_to['href']
                        if to_url == comment_link_to:
                            s_ += 1
                        else:
                            pass
            except:
                print('no se pudo acceder a: ' + url)
                eraseTwo = csv.delete()

        if s_ > 0:
            csv.site_link = 'Comentario'
            csv.save()
        else:
            pass

        if f_ > 0:
            csv.site_link = 'Foro'
            csv.save()
        else:
            pass

def scrapper_43(array, search):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.backlink
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = search.get(pk=pk)

        if 'forum' in url or 'foro' in url:
            csv.foro = True
            csv.save()
            f_ += 1
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = csv.delete()
        else:
            try:
                response = requests.get(url, headers=USER_AGENT)
                response.raise_for_status()
                c = response.content

                soup = BeautifulSoup(c, 'html.parser')
                x_class = re.compile('com[a-z]+')
                comment_class_id = soup.find_all(['div', 'section', 'footer', 'p', 'span', 'li'], attrs={'class':x_class})
                for comment in comment_class_id:
                    comment_link = comment.find_all('a', attrs = {'rel':'nofollow'}, href=True)
                    for comment_link_to in comment_link:
                        comment_link_to = comment_link_to['href']
                        if to_url == comment_link_to:
                            s_ += 1
                        else:
                            pass
            except:
                print('no se pudo acceder a: ' + url)
                eraseTwo = csv.delete()

        if s_ > 0:
            csv.site_link = 'Comentario'
            csv.save()
        else:
            pass

        if f_ > 0:
            csv.site_link = 'Foro'
            csv.save()
        else:
            pass

def scrapper_44(array, search):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.backlink
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = search.get(pk=pk)

        if 'forum' in url or 'foro' in url:
            csv.foro = True
            csv.save()
            f_ += 1
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = csv.delete()
        else:
            try:
                response = requests.get(url, headers=USER_AGENT)
                response.raise_for_status()
                c = response.content

                soup = BeautifulSoup(c, 'html.parser')
                x_class = re.compile('com[a-z]+')
                comment_class_id = soup.find_all(['div', 'section', 'footer', 'p', 'span', 'li'], attrs={'class':x_class})
                for comment in comment_class_id:
                    comment_link = comment.find_all('a', attrs = {'rel':'nofollow'}, href=True)
                    for comment_link_to in comment_link:
                        comment_link_to = comment_link_to['href']
                        if to_url == comment_link_to:
                            s_ += 1
                        else:
                            pass
            except:
                print('no se pudo acceder a: ' + url)
                eraseTwo = csv.delete()

        if s_ > 0:
            csv.site_link = 'Comentario'
            csv.save()
        else:
            pass

        if f_ > 0:
            csv.site_link = 'Foro'
            csv.save()
        else:
            pass

def scrapper_45(array, search):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.backlink
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = search.get(pk=pk)

        if 'forum' in url or 'foro' in url:
            csv.foro = True
            csv.save()
            f_ += 1
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = csv.delete()
        else:
            try:
                response = requests.get(url, headers=USER_AGENT)
                response.raise_for_status()
                c = response.content

                soup = BeautifulSoup(c, 'html.parser')
                x_class = re.compile('com[a-z]+')
                comment_class_id = soup.find_all(['div', 'section', 'footer', 'p', 'span', 'li'], attrs={'class':x_class})
                for comment in comment_class_id:
                    comment_link = comment.find_all('a', attrs = {'rel':'nofollow'}, href=True)
                    for comment_link_to in comment_link:
                        comment_link_to = comment_link_to['href']
                        if to_url == comment_link_to:
                            s_ += 1
                        else:
                            pass
            except:
                print('no se pudo acceder a: ' + url)
                eraseTwo = csv.delete()

        if s_ > 0:
            csv.site_link = 'Comentario'
            csv.save()
        else:
            pass

        if f_ > 0:
            csv.site_link = 'Foro'
            csv.save()
        else:
            pass

def scrapper_46(array, search):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.backlink
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = search.get(pk=pk)

        if 'forum' in url or 'foro' in url:
            csv.foro = True
            csv.save()
            f_ += 1
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = csv.delete()
        else:
            try:
                response = requests.get(url, headers=USER_AGENT)
                response.raise_for_status()
                c = response.content

                soup = BeautifulSoup(c, 'html.parser')
                x_class = re.compile('com[a-z]+')
                comment_class_id = soup.find_all(['div', 'section', 'footer', 'p', 'span', 'li'], attrs={'class':x_class})
                for comment in comment_class_id:
                    comment_link = comment.find_all('a', attrs = {'rel':'nofollow'}, href=True)
                    for comment_link_to in comment_link:
                        comment_link_to = comment_link_to['href']
                        if to_url == comment_link_to:
                            s_ += 1
                        else:
                            pass
            except:
                print('no se pudo acceder a: ' + url)
                eraseTwo = csv.delete()

        if s_ > 0:
            csv.site_link = 'Comentario'
            csv.save()
        else:
            pass

        if f_ > 0:
            csv.site_link = 'Foro'
            csv.save()
        else:
            pass


def scrapper_47(array, search):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.backlink
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = search.get(pk=pk)

        if 'forum' in url or 'foro' in url:
            csv.foro = True
            csv.save()
            f_ += 1
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = csv.delete()
        else:
            try:
                response = requests.get(url, headers=USER_AGENT)
                response.raise_for_status()
                c = response.content

                soup = BeautifulSoup(c, 'html.parser')
                x_class = re.compile('com[a-z]+')
                comment_class_id = soup.find_all(['div', 'section', 'footer', 'p', 'span', 'li'], attrs={'class':x_class})
                for comment in comment_class_id:
                    comment_link = comment.find_all('a', attrs = {'rel':'nofollow'}, href=True)
                    for comment_link_to in comment_link:
                        comment_link_to = comment_link_to['href']
                        if to_url == comment_link_to:
                            s_ += 1
                        else:
                            pass
            except:
                print('no se pudo acceder a: ' + url)
                eraseTwo = csv.delete()

        if s_ > 0:
            csv.site_link = 'Comentario'
            csv.save()
        else:
            pass

        if f_ > 0:
            csv.site_link = 'Foro'
            csv.save()
        else:
            pass

def scrapper_48(array, search):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.backlink
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = search.get(pk=pk)

        if 'forum' in url or 'foro' in url:
            csv.foro = True
            csv.save()
            f_ += 1
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = csv.delete()
        else:
            try:
                response = requests.get(url, headers=USER_AGENT)
                response.raise_for_status()
                c = response.content

                soup = BeautifulSoup(c, 'html.parser')
                x_class = re.compile('com[a-z]+')
                comment_class_id = soup.find_all(['div', 'section', 'footer', 'p', 'span', 'li'], attrs={'class':x_class})
                for comment in comment_class_id:
                    comment_link = comment.find_all('a', attrs = {'rel':'nofollow'}, href=True)
                    for comment_link_to in comment_link:
                        comment_link_to = comment_link_to['href']
                        if to_url == comment_link_to:
                            s_ += 1
                        else:
                            pass
            except:
                print('no se pudo acceder a: ' + url)
                eraseTwo = csv.delete()

        if s_ > 0:
            csv.site_link = 'Comentario'
            csv.save()
        else:
            pass

        if f_ > 0:
            csv.site_link = 'Foro'
            csv.save()
        else:
            pass

def scrapper_49(array, search):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.backlink
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = search.get(pk=pk)

        if 'forum' in url or 'foro' in url:
            csv.foro = True
            csv.save()
            f_ += 1
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = csv.delete()
        else:
            try:
                response = requests.get(url, headers=USER_AGENT)
                response.raise_for_status()
                c = response.content

                soup = BeautifulSoup(c, 'html.parser')
                x_class = re.compile('com[a-z]+')
                comment_class_id = soup.find_all(['div', 'section', 'footer', 'p', 'span', 'li'], attrs={'class':x_class})
                for comment in comment_class_id:
                    comment_link = comment.find_all('a', attrs = {'rel':'nofollow'}, href=True)
                    for comment_link_to in comment_link:
                        comment_link_to = comment_link_to['href']
                        if to_url == comment_link_to:
                            s_ += 1
                        else:
                            pass
            except:
                print('no se pudo acceder a: ' + url)
                eraseTwo = csv.delete()

        if s_ > 0:
            csv.site_link = 'Comentario'
            csv.save()
        else:
            pass

        if f_ > 0:
            csv.site_link = 'Foro'
            csv.save()
        else:
            pass

def scrapper_50(array, search):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.backlink
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = search.get(pk=pk)

        if 'forum' in url or 'foro' in url:
            csv.foro = True
            csv.save()
            f_ += 1
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = csv.delete()
        else:
            try:
                response = requests.get(url, headers=USER_AGENT)
                response.raise_for_status()
                c = response.content

                soup = BeautifulSoup(c, 'html.parser')
                x_class = re.compile('com[a-z]+')
                comment_class_id = soup.find_all(['div', 'section', 'footer', 'p', 'span', 'li'], attrs={'class':x_class})
                for comment in comment_class_id:
                    comment_link = comment.find_all('a', attrs = {'rel':'nofollow'}, href=True)
                    for comment_link_to in comment_link:
                        comment_link_to = comment_link_to['href']
                        if to_url == comment_link_to:
                            s_ += 1
                        else:
                            pass
            except:
                print('no se pudo acceder a: ' + url)
                eraseTwo = csv.delete()

        if s_ > 0:
            csv.site_link = 'Comentario'
            csv.save()
        else:
            pass

        if f_ > 0:
            csv.site_link = 'Foro'
            csv.save()
        else:
            pass


def scrapper_51(array, search):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.backlink
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = search.get(pk=pk)

        if 'forum' in url or 'foro' in url:
            csv.foro = True
            csv.save()
            f_ += 1
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = csv.delete()
        else:
            try:
                response = requests.get(url, headers=USER_AGENT)
                response.raise_for_status()
                c = response.content

                soup = BeautifulSoup(c, 'html.parser')
                x_class = re.compile('com[a-z]+')
                comment_class_id = soup.find_all(['div', 'section', 'footer', 'p', 'span', 'li'], attrs={'class':x_class})
                for comment in comment_class_id:
                    comment_link = comment.find_all('a', attrs = {'rel':'nofollow'}, href=True)
                    for comment_link_to in comment_link:
                        comment_link_to = comment_link_to['href']
                        if to_url == comment_link_to:
                            s_ += 1
                        else:
                            pass
            except:
                print('no se pudo acceder a: ' + url)
                eraseTwo = csv.delete()

        if s_ > 0:
            csv.site_link = 'Comentario'
            csv.save()
        else:
            pass

        if f_ > 0:
            csv.site_link = 'Foro'
            csv.save()
        else:
            pass


def scrapper_52(array, search):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.backlink
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = search.get(pk=pk)

        if 'forum' in url or 'foro' in url:
            csv.foro = True
            csv.save()
            f_ += 1
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = csv.delete()
        else:
            try:
                response = requests.get(url, headers=USER_AGENT)
                response.raise_for_status()
                c = response.content

                soup = BeautifulSoup(c, 'html.parser')
                x_class = re.compile('com[a-z]+')
                comment_class_id = soup.find_all(['div', 'section', 'footer', 'p', 'span', 'li'], attrs={'class':x_class})
                for comment in comment_class_id:
                    comment_link = comment.find_all('a', attrs = {'rel':'nofollow'}, href=True)
                    for comment_link_to in comment_link:
                        comment_link_to = comment_link_to['href']
                        if to_url == comment_link_to:
                            s_ += 1
                        else:
                            pass
            except:
                print('no se pudo acceder a: ' + url)
                eraseTwo = csv.delete()

        if s_ > 0:
            csv.site_link = 'Comentario'
            csv.save()
        else:
            pass

        if f_ > 0:
            csv.site_link = 'Foro'
            csv.save()
        else:
            pass

def scrapper_53(array, search):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.backlink
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = search.get(pk=pk)

        if 'forum' in url or 'foro' in url:
            csv.foro = True
            csv.save()
            f_ += 1
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = csv.delete()
        else:
            try:
                response = requests.get(url, headers=USER_AGENT)
                response.raise_for_status()
                c = response.content

                soup = BeautifulSoup(c, 'html.parser')
                x_class = re.compile('com[a-z]+')
                comment_class_id = soup.find_all(['div', 'section', 'footer', 'p', 'span', 'li'], attrs={'class':x_class})
                for comment in comment_class_id:
                    comment_link = comment.find_all('a', attrs = {'rel':'nofollow'}, href=True)
                    for comment_link_to in comment_link:
                        comment_link_to = comment_link_to['href']
                        if to_url == comment_link_to:
                            s_ += 1
                        else:
                            pass
            except:
                print('no se pudo acceder a: ' + url)
                eraseTwo = csv.delete()

        if s_ > 0:
            csv.site_link = 'Comentario'
            csv.save()
        else:
            pass

        if f_ > 0:
            csv.site_link = 'Foro'
            csv.save()
        else:
            pass

def scrapper_54(array, search):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.backlink
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = search.get(pk=pk)

        if 'forum' in url or 'foro' in url:
            csv.foro = True
            csv.save()
            f_ += 1
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = csv.delete()
        else:
            try:
                response = requests.get(url, headers=USER_AGENT)
                response.raise_for_status()
                c = response.content

                soup = BeautifulSoup(c, 'html.parser')
                x_class = re.compile('com[a-z]+')
                comment_class_id = soup.find_all(['div', 'section', 'footer', 'p', 'span', 'li'], attrs={'class':x_class})
                for comment in comment_class_id:
                    comment_link = comment.find_all('a', attrs = {'rel':'nofollow'}, href=True)
                    for comment_link_to in comment_link:
                        comment_link_to = comment_link_to['href']
                        if to_url == comment_link_to:
                            s_ += 1
                        else:
                            pass
            except:
                print('no se pudo acceder a: ' + url)
                eraseTwo = csv.delete()

        if s_ > 0:
            csv.site_link = 'Comentario'
            csv.save()
        else:
            pass

        if f_ > 0:
            csv.site_link = 'Foro'
            csv.save()
        else:
            pass

def scrapper_55(array, search):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.backlink
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = search.get(pk=pk)

        if 'forum' in url or 'foro' in url:
            csv.foro = True
            csv.save()
            f_ += 1
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = csv.delete()
        else:
            try:
                response = requests.get(url, headers=USER_AGENT)
                response.raise_for_status()
                c = response.content

                soup = BeautifulSoup(c, 'html.parser')
                x_class = re.compile('com[a-z]+')
                comment_class_id = soup.find_all(['div', 'section', 'footer', 'p', 'span', 'li'], attrs={'class':x_class})
                for comment in comment_class_id:
                    comment_link = comment.find_all('a', attrs = {'rel':'nofollow'}, href=True)
                    for comment_link_to in comment_link:
                        comment_link_to = comment_link_to['href']
                        if to_url == comment_link_to:
                            s_ += 1
                        else:
                            pass
            except:
                print('no se pudo acceder a: ' + url)
                eraseTwo = csv.delete()

        if s_ > 0:
            csv.site_link = 'Comentario'
            csv.save()
        else:
            pass

        if f_ > 0:
            csv.site_link = 'Foro'
            csv.save()
        else:
            pass

def scrapper_56(array, search):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.backlink
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = search.get(pk=pk)

        if 'forum' in url or 'foro' in url:
            csv.foro = True
            csv.save()
            f_ += 1
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = csv.delete()
        else:
            try:
                response = requests.get(url, headers=USER_AGENT)
                response.raise_for_status()
                c = response.content

                soup = BeautifulSoup(c, 'html.parser')
                x_class = re.compile('com[a-z]+')
                comment_class_id = soup.find_all(['div', 'section', 'footer', 'p', 'span', 'li'], attrs={'class':x_class})
                for comment in comment_class_id:
                    comment_link = comment.find_all('a', attrs = {'rel':'nofollow'}, href=True)
                    for comment_link_to in comment_link:
                        comment_link_to = comment_link_to['href']
                        if to_url == comment_link_to:
                            s_ += 1
                        else:
                            pass
            except:
                print('no se pudo acceder a: ' + url)
                eraseTwo = csv.delete()

        if s_ > 0:
            csv.site_link = 'Comentario'
            csv.save()
        else:
            pass

        if f_ > 0:
            csv.site_link = 'Foro'
            csv.save()
        else:
            pass

def scrapper_57(array, search):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.backlink
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = search.get(pk=pk)

        if 'forum' in url or 'foro' in url:
            csv.foro = True
            csv.save()
            f_ += 1
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = csv.delete()
        else:
            try:
                response = requests.get(url, headers=USER_AGENT)
                response.raise_for_status()
                c = response.content

                soup = BeautifulSoup(c, 'html.parser')
                x_class = re.compile('com[a-z]+')
                comment_class_id = soup.find_all(['div', 'section', 'footer', 'p', 'span', 'li'], attrs={'class':x_class})
                for comment in comment_class_id:
                    comment_link = comment.find_all('a', attrs = {'rel':'nofollow'}, href=True)
                    for comment_link_to in comment_link:
                        comment_link_to = comment_link_to['href']
                        if to_url == comment_link_to:
                            s_ += 1
                        else:
                            pass
            except:
                print('no se pudo acceder a: ' + url)
                eraseTwo = csv.delete()

        if s_ > 0:
            csv.site_link = 'Comentario'
            csv.save()
        else:
            pass

        if f_ > 0:
            csv.site_link = 'Foro'
            csv.save()
        else:
            pass


def scrapper_58(array, search):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.backlink
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = search.get(pk=pk)

        if 'forum' in url or 'foro' in url:
            csv.foro = True
            csv.save()
            f_ += 1
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = csv.delete()
        else:
            try:
                response = requests.get(url, headers=USER_AGENT)
                response.raise_for_status()
                c = response.content

                soup = BeautifulSoup(c, 'html.parser')
                x_class = re.compile('com[a-z]+')
                comment_class_id = soup.find_all(['div', 'section', 'footer', 'p', 'span', 'li'], attrs={'class':x_class})
                for comment in comment_class_id:
                    comment_link = comment.find_all('a', attrs = {'rel':'nofollow'}, href=True)
                    for comment_link_to in comment_link:
                        comment_link_to = comment_link_to['href']
                        if to_url == comment_link_to:
                            s_ += 1
                        else:
                            pass
            except:
                print('no se pudo acceder a: ' + url)
                eraseTwo = csv.delete()

        if s_ > 0:
            csv.site_link = 'Comentario'
            csv.save()
        else:
            pass

        if f_ > 0:
            csv.site_link = 'Foro'
            csv.save()
        else:
            pass

def scrapper_59(array, search):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.backlink
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = search.get(pk=pk)

        if 'forum' in url or 'foro' in url:
            csv.foro = True
            csv.save()
            f_ += 1
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = csv.delete()
        else:
            try:
                response = requests.get(url, headers=USER_AGENT)
                response.raise_for_status()
                c = response.content

                soup = BeautifulSoup(c, 'html.parser')
                x_class = re.compile('com[a-z]+')
                comment_class_id = soup.find_all(['div', 'section', 'footer', 'p', 'span', 'li'], attrs={'class':x_class})
                for comment in comment_class_id:
                    comment_link = comment.find_all('a', attrs = {'rel':'nofollow'}, href=True)
                    for comment_link_to in comment_link:
                        comment_link_to = comment_link_to['href']
                        if to_url == comment_link_to:
                            s_ += 1
                        else:
                            pass
            except:
                print('no se pudo acceder a: ' + url)
                eraseTwo = csv.delete()

        if s_ > 0:
            csv.site_link = 'Comentario'
            csv.save()
        else:
            pass

        if f_ > 0:
            csv.site_link = 'Foro'
            csv.save()
        else:
            pass

def scrapper_60(array, search):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.backlink
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = search.get(pk=pk)

        if 'forum' in url or 'foro' in url:
            csv.foro = True
            csv.save()
            f_ += 1
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = csv.delete()
        else:
            try:
                response = requests.get(url, headers=USER_AGENT)
                response.raise_for_status()
                c = response.content

                soup = BeautifulSoup(c, 'html.parser')
                x_class = re.compile('com[a-z]+')
                comment_class_id = soup.find_all(['div', 'section', 'footer', 'p', 'span', 'li'], attrs={'class':x_class})
                for comment in comment_class_id:
                    comment_link = comment.find_all('a', attrs = {'rel':'nofollow'}, href=True)
                    for comment_link_to in comment_link:
                        comment_link_to = comment_link_to['href']
                        if to_url == comment_link_to:
                            s_ += 1
                        else:
                            pass
            except:
                print('no se pudo acceder a: ' + url)
                eraseTwo = csv.delete()

        if s_ > 0:
            csv.site_link = 'Comentario'
            csv.save()
        else:
            pass

        if f_ > 0:
            csv.site_link = 'Foro'
            csv.save()
        else:
            pass


def scrapper_61(array, search):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.backlink
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = search.get(pk=pk)

        if 'forum' in url or 'foro' in url:
            csv.foro = True
            csv.save()
            f_ += 1
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = csv.delete()
        else:
            try:
                response = requests.get(url, headers=USER_AGENT)
                response.raise_for_status()
                c = response.content

                soup = BeautifulSoup(c, 'html.parser')
                x_class = re.compile('com[a-z]+')
                comment_class_id = soup.find_all(['div', 'section', 'footer', 'p', 'span', 'li'], attrs={'class':x_class})
                for comment in comment_class_id:
                    comment_link = comment.find_all('a', attrs = {'rel':'nofollow'}, href=True)
                    for comment_link_to in comment_link:
                        comment_link_to = comment_link_to['href']
                        if to_url == comment_link_to:
                            s_ += 1
                        else:
                            pass
            except:
                print('no se pudo acceder a: ' + url)
                eraseTwo = csv.delete()

        if s_ > 0:
            csv.site_link = 'Comentario'
            csv.save()
        else:
            pass

        if f_ > 0:
            csv.site_link = 'Foro'
            csv.save()
        else:
            pass

def scrapper_62(array, search):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.backlink
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = search.get(pk=pk)

        if 'forum' in url or 'foro' in url:
            csv.foro = True
            csv.save()
            f_ += 1
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = csv.delete()
        else:
            try:
                response = requests.get(url, headers=USER_AGENT)
                response.raise_for_status()
                c = response.content

                soup = BeautifulSoup(c, 'html.parser')
                x_class = re.compile('com[a-z]+')
                comment_class_id = soup.find_all(['div', 'section', 'footer', 'p', 'span', 'li'], attrs={'class':x_class})
                for comment in comment_class_id:
                    comment_link = comment.find_all('a', attrs = {'rel':'nofollow'}, href=True)
                    for comment_link_to in comment_link:
                        comment_link_to = comment_link_to['href']
                        if to_url == comment_link_to:
                            s_ += 1
                        else:
                            pass
            except:
                print('no se pudo acceder a: ' + url)
                eraseTwo = csv.delete()

        if s_ > 0:
            csv.site_link = 'Comentario'
            csv.save()
        else:
            pass

        if f_ > 0:
            csv.site_link = 'Foro'
            csv.save()
        else:
            pass

def scrapper_63(array, search):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.backlink
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = search.get(pk=pk)

        if 'forum' in url or 'foro' in url:
            csv.foro = True
            csv.save()
            f_ += 1
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = csv.delete()
        else:
            try:
                response = requests.get(url, headers=USER_AGENT)
                response.raise_for_status()
                c = response.content

                soup = BeautifulSoup(c, 'html.parser')
                x_class = re.compile('com[a-z]+')
                comment_class_id = soup.find_all(['div', 'section', 'footer', 'p', 'span', 'li'], attrs={'class':x_class})
                for comment in comment_class_id:
                    comment_link = comment.find_all('a', attrs = {'rel':'nofollow'}, href=True)
                    for comment_link_to in comment_link:
                        comment_link_to = comment_link_to['href']
                        if to_url == comment_link_to:
                            s_ += 1
                        else:
                            pass
            except:
                print('no se pudo acceder a: ' + url)
                eraseTwo = csv.delete()

        if s_ > 0:
            csv.site_link = 'Comentario'
            csv.save()
        else:
            pass

        if f_ > 0:
            csv.site_link = 'Foro'
            csv.save()
        else:
            pass

def scrapper_64(array, search):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.backlink
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = search.get(pk=pk)

        if 'forum' in url or 'foro' in url:
            csv.foro = True
            csv.save()
            f_ += 1
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = csv.delete()
        else:
            try:
                response = requests.get(url, headers=USER_AGENT)
                response.raise_for_status()
                c = response.content

                soup = BeautifulSoup(c, 'html.parser')
                x_class = re.compile('com[a-z]+')
                comment_class_id = soup.find_all(['div', 'section', 'footer', 'p', 'span', 'li'], attrs={'class':x_class})
                for comment in comment_class_id:
                    comment_link = comment.find_all('a', attrs = {'rel':'nofollow'}, href=True)
                    for comment_link_to in comment_link:
                        comment_link_to = comment_link_to['href']
                        if to_url == comment_link_to:
                            s_ += 1
                        else:
                            pass
            except:
                print('no se pudo acceder a: ' + url)
                eraseTwo = csv.delete()

        if s_ > 0:
            csv.site_link = 'Comentario'
            csv.save()
        else:
            pass

        if f_ > 0:
            csv.site_link = 'Foro'
            csv.save()
        else:
            pass

def scrapper_65(array, search):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.backlink
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = search.get(pk=pk)

        if 'forum' in url or 'foro' in url:
            csv.foro = True
            csv.save()
            f_ += 1
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = csv.delete()
        else:
            try:
                response = requests.get(url, headers=USER_AGENT)
                response.raise_for_status()
                c = response.content

                soup = BeautifulSoup(c, 'html.parser')
                x_class = re.compile('com[a-z]+')
                comment_class_id = soup.find_all(['div', 'section', 'footer', 'p', 'span', 'li'], attrs={'class':x_class})
                for comment in comment_class_id:
                    comment_link = comment.find_all('a', attrs = {'rel':'nofollow'}, href=True)
                    for comment_link_to in comment_link:
                        comment_link_to = comment_link_to['href']
                        if to_url == comment_link_to:
                            s_ += 1
                        else:
                            pass
            except:
                print('no se pudo acceder a: ' + url)
                eraseTwo = csv.delete()

        if s_ > 0:
            csv.site_link = 'Comentario'
            csv.save()
        else:
            pass

        if f_ > 0:
            csv.site_link = 'Foro'
            csv.save()
        else:
            pass

def scrapper_66(array, search):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.backlink
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = search.get(pk=pk)

        if 'forum' in url or 'foro' in url:
            csv.foro = True
            csv.save()
            f_ += 1
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = csv.delete()
        else:
            try:
                response = requests.get(url, headers=USER_AGENT)
                response.raise_for_status()
                c = response.content

                soup = BeautifulSoup(c, 'html.parser')
                x_class = re.compile('com[a-z]+')
                comment_class_id = soup.find_all(['div', 'section', 'footer', 'p', 'span', 'li'], attrs={'class':x_class})
                for comment in comment_class_id:
                    comment_link = comment.find_all('a', attrs = {'rel':'nofollow'}, href=True)
                    for comment_link_to in comment_link:
                        comment_link_to = comment_link_to['href']
                        if to_url == comment_link_to:
                            s_ += 1
                        else:
                            pass
            except:
                print('no se pudo acceder a: ' + url)
                eraseTwo = csv.delete()

        if s_ > 0:
            csv.site_link = 'Comentario'
            csv.save()
        else:
            pass

        if f_ > 0:
            csv.site_link = 'Foro'
            csv.save()
        else:
            pass


def scrapper_67(array, search):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.backlink
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = search.get(pk=pk)

        if 'forum' in url or 'foro' in url:
            csv.foro = True
            csv.save()
            f_ += 1
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = csv.delete()
        else:
            try:
                response = requests.get(url, headers=USER_AGENT)
                response.raise_for_status()
                c = response.content

                soup = BeautifulSoup(c, 'html.parser')
                x_class = re.compile('com[a-z]+')
                comment_class_id = soup.find_all(['div', 'section', 'footer', 'p', 'span', 'li'], attrs={'class':x_class})
                for comment in comment_class_id:
                    comment_link = comment.find_all('a', attrs = {'rel':'nofollow'}, href=True)
                    for comment_link_to in comment_link:
                        comment_link_to = comment_link_to['href']
                        if to_url == comment_link_to:
                            s_ += 1
                        else:
                            pass
            except:
                print('no se pudo acceder a: ' + url)
                eraseTwo = csv.delete()

        if s_ > 0:
            csv.site_link = 'Comentario'
            csv.save()
        else:
            pass

        if f_ > 0:
            csv.site_link = 'Foro'
            csv.save()
        else:
            pass

def scrapper_68(array, search):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.backlink
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = search.get(pk=pk)

        if 'forum' in url or 'foro' in url:
            csv.foro = True
            csv.save()
            f_ += 1
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = csv.delete()
        else:
            try:
                response = requests.get(url, headers=USER_AGENT)
                response.raise_for_status()
                c = response.content

                soup = BeautifulSoup(c, 'html.parser')
                x_class = re.compile('com[a-z]+')
                comment_class_id = soup.find_all(['div', 'section', 'footer', 'p', 'span', 'li'], attrs={'class':x_class})
                for comment in comment_class_id:
                    comment_link = comment.find_all('a', attrs = {'rel':'nofollow'}, href=True)
                    for comment_link_to in comment_link:
                        comment_link_to = comment_link_to['href']
                        if to_url == comment_link_to:
                            s_ += 1
                        else:
                            pass
            except:
                print('no se pudo acceder a: ' + url)
                eraseTwo = csv.delete()

        if s_ > 0:
            csv.site_link = 'Comentario'
            csv.save()
        else:
            pass

        if f_ > 0:
            csv.site_link = 'Foro'
            csv.save()
        else:
            pass

def scrapper_69(array, search):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.backlink
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = search.get(pk=pk)

        if 'forum' in url or 'foro' in url:
            csv.foro = True
            csv.save()
            f_ += 1
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = csv.delete()
        else:
            try:
                response = requests.get(url, headers=USER_AGENT)
                response.raise_for_status()
                c = response.content

                soup = BeautifulSoup(c, 'html.parser')
                x_class = re.compile('com[a-z]+')
                comment_class_id = soup.find_all(['div', 'section', 'footer', 'p', 'span', 'li'], attrs={'class':x_class})
                for comment in comment_class_id:
                    comment_link = comment.find_all('a', attrs = {'rel':'nofollow'}, href=True)
                    for comment_link_to in comment_link:
                        comment_link_to = comment_link_to['href']
                        if to_url == comment_link_to:
                            s_ += 1
                        else:
                            pass
            except:
                print('no se pudo acceder a: ' + url)
                eraseTwo = csv.delete()

        if s_ > 0:
            csv.site_link = 'Comentario'
            csv.save()
        else:
            pass

        if f_ > 0:
            csv.site_link = 'Foro'
            csv.save()
        else:
            pass

def scrapper_70(array, search):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.backlink
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = search.get(pk=pk)

        if 'forum' in url or 'foro' in url:
            csv.foro = True
            csv.save()
            f_ += 1
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = csv.delete()
        else:
            try:
                response = requests.get(url, headers=USER_AGENT)
                response.raise_for_status()
                c = response.content

                soup = BeautifulSoup(c, 'html.parser')
                x_class = re.compile('com[a-z]+')
                comment_class_id = soup.find_all(['div', 'section', 'footer', 'p', 'span', 'li'], attrs={'class':x_class})
                for comment in comment_class_id:
                    comment_link = comment.find_all('a', attrs = {'rel':'nofollow'}, href=True)
                    for comment_link_to in comment_link:
                        comment_link_to = comment_link_to['href']
                        if to_url == comment_link_to:
                            s_ += 1
                        else:
                            pass
            except:
                print('no se pudo acceder a: ' + url)
                eraseTwo = csv.delete()

        if s_ > 0:
            csv.site_link = 'Comentario'
            csv.save()
        else:
            pass

        if f_ > 0:
            csv.site_link = 'Foro'
            csv.save()
        else:
            pass


def scrapper_71(array, search):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.backlink
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = search.get(pk=pk)

        if 'forum' in url or 'foro' in url:
            csv.foro = True
            csv.save()
            f_ += 1
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = csv.delete()
        else:
            try:
                response = requests.get(url, headers=USER_AGENT)
                response.raise_for_status()
                c = response.content

                soup = BeautifulSoup(c, 'html.parser')
                x_class = re.compile('com[a-z]+')
                comment_class_id = soup.find_all(['div', 'section', 'footer', 'p', 'span', 'li'], attrs={'class':x_class})
                for comment in comment_class_id:
                    comment_link = comment.find_all('a', attrs = {'rel':'nofollow'}, href=True)
                    for comment_link_to in comment_link:
                        comment_link_to = comment_link_to['href']
                        if to_url == comment_link_to:
                            s_ += 1
                        else:
                            pass
            except:
                print('no se pudo acceder a: ' + url)
                eraseTwo = csv.delete()

        if s_ > 0:
            csv.site_link = 'Comentario'
            csv.save()
        else:
            pass

        if f_ > 0:
            csv.site_link = 'Foro'
            csv.save()
        else:
            pass


def scrapper_72(array, search):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.backlink
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = search.get(pk=pk)

        if 'forum' in url or 'foro' in url:
            csv.foro = True
            csv.save()
            f_ += 1
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = csv.delete()
        else:
            try:
                response = requests.get(url, headers=USER_AGENT)
                response.raise_for_status()
                c = response.content

                soup = BeautifulSoup(c, 'html.parser')
                x_class = re.compile('com[a-z]+')
                comment_class_id = soup.find_all(['div', 'section', 'footer', 'p', 'span', 'li'], attrs={'class':x_class})
                for comment in comment_class_id:
                    comment_link = comment.find_all('a', attrs = {'rel':'nofollow'}, href=True)
                    for comment_link_to in comment_link:
                        comment_link_to = comment_link_to['href']
                        if to_url == comment_link_to:
                            s_ += 1
                        else:
                            pass
            except:
                print('no se pudo acceder a: ' + url)
                eraseTwo = csv.delete()

        if s_ > 0:
            csv.site_link = 'Comentario'
            csv.save()
        else:
            pass

        if f_ > 0:
            csv.site_link = 'Foro'
            csv.save()
        else:
            pass

def scrapper_73(array, search):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.backlink
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = search.get(pk=pk)

        if 'forum' in url or 'foro' in url:
            csv.foro = True
            csv.save()
            f_ += 1
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = csv.delete()
        else:
            try:
                response = requests.get(url, headers=USER_AGENT)
                response.raise_for_status()
                c = response.content

                soup = BeautifulSoup(c, 'html.parser')
                x_class = re.compile('com[a-z]+')
                comment_class_id = soup.find_all(['div', 'section', 'footer', 'p', 'span', 'li'], attrs={'class':x_class})
                for comment in comment_class_id:
                    comment_link = comment.find_all('a', attrs = {'rel':'nofollow'}, href=True)
                    for comment_link_to in comment_link:
                        comment_link_to = comment_link_to['href']
                        if to_url == comment_link_to:
                            s_ += 1
                        else:
                            pass
            except:
                print('no se pudo acceder a: ' + url)
                eraseTwo = csv.delete()

        if s_ > 0:
            csv.site_link = 'Comentario'
            csv.save()
        else:
            pass

        if f_ > 0:
            csv.site_link = 'Foro'
            csv.save()
        else:
            pass

def scrapper_74(array, search):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.backlink
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = search.get(pk=pk)

        if 'forum' in url or 'foro' in url:
            csv.foro = True
            csv.save()
            f_ += 1
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = csv.delete()
        else:
            try:
                response = requests.get(url, headers=USER_AGENT)
                response.raise_for_status()
                c = response.content

                soup = BeautifulSoup(c, 'html.parser')
                x_class = re.compile('com[a-z]+')
                comment_class_id = soup.find_all(['div', 'section', 'footer', 'p', 'span', 'li'], attrs={'class':x_class})
                for comment in comment_class_id:
                    comment_link = comment.find_all('a', attrs = {'rel':'nofollow'}, href=True)
                    for comment_link_to in comment_link:
                        comment_link_to = comment_link_to['href']
                        if to_url == comment_link_to:
                            s_ += 1
                        else:
                            pass
            except:
                print('no se pudo acceder a: ' + url)
                eraseTwo = csv.delete()

        if s_ > 0:
            csv.site_link = 'Comentario'
            csv.save()
        else:
            pass

        if f_ > 0:
            csv.site_link = 'Foro'
            csv.save()
        else:
            pass

def scrapper_75(array, search):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.backlink
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = search.get(pk=pk)

        if 'forum' in url or 'foro' in url:
            csv.foro = True
            csv.save()
            f_ += 1
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = csv.delete()
        else:
            try:
                response = requests.get(url, headers=USER_AGENT)
                response.raise_for_status()
                c = response.content

                soup = BeautifulSoup(c, 'html.parser')
                x_class = re.compile('com[a-z]+')
                comment_class_id = soup.find_all(['div', 'section', 'footer', 'p', 'span', 'li'], attrs={'class':x_class})
                for comment in comment_class_id:
                    comment_link = comment.find_all('a', attrs = {'rel':'nofollow'}, href=True)
                    for comment_link_to in comment_link:
                        comment_link_to = comment_link_to['href']
                        if to_url == comment_link_to:
                            s_ += 1
                        else:
                            pass
            except:
                print('no se pudo acceder a: ' + url)
                eraseTwo = csv.delete()

        if s_ > 0:
            csv.site_link = 'Comentario'
            csv.save()
        else:
            pass

        if f_ > 0:
            csv.site_link = 'Foro'
            csv.save()
        else:
            pass

def scrapper_76(array, search):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.backlink
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = search.get(pk=pk)

        if 'forum' in url or 'foro' in url:
            csv.foro = True
            csv.save()
            f_ += 1
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = csv.delete()
        else:
            try:
                response = requests.get(url, headers=USER_AGENT)
                response.raise_for_status()
                c = response.content

                soup = BeautifulSoup(c, 'html.parser')
                x_class = re.compile('com[a-z]+')
                comment_class_id = soup.find_all(['div', 'section', 'footer', 'p', 'span', 'li'], attrs={'class':x_class})
                for comment in comment_class_id:
                    comment_link = comment.find_all('a', attrs = {'rel':'nofollow'}, href=True)
                    for comment_link_to in comment_link:
                        comment_link_to = comment_link_to['href']
                        if to_url == comment_link_to:
                            s_ += 1
                        else:
                            pass
            except:
                print('no se pudo acceder a: ' + url)
                eraseTwo = csv.delete()

        if s_ > 0:
            csv.site_link = 'Comentario'
            csv.save()
        else:
            pass

        if f_ > 0:
            csv.site_link = 'Foro'
            csv.save()
        else:
            pass

def scrapper_77(array, search):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.backlink
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = search.get(pk=pk)

        if 'forum' in url or 'foro' in url:
            csv.foro = True
            csv.save()
            f_ += 1
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = csv.delete()
        else:
            try:
                response = requests.get(url, headers=USER_AGENT)
                response.raise_for_status()
                c = response.content

                soup = BeautifulSoup(c, 'html.parser')
                x_class = re.compile('com[a-z]+')
                comment_class_id = soup.find_all(['div', 'section', 'footer', 'p', 'span', 'li'], attrs={'class':x_class})
                for comment in comment_class_id:
                    comment_link = comment.find_all('a', attrs = {'rel':'nofollow'}, href=True)
                    for comment_link_to in comment_link:
                        comment_link_to = comment_link_to['href']
                        if to_url == comment_link_to:
                            s_ += 1
                        else:
                            pass
            except:
                print('no se pudo acceder a: ' + url)
                eraseTwo = csv.delete()

        if s_ > 0:
            csv.site_link = 'Comentario'
            csv.save()
        else:
            pass

        if f_ > 0:
            csv.site_link = 'Foro'
            csv.save()
        else:
            pass


def scrapper_78(array, search):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.backlink
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = search.get(pk=pk)

        if 'forum' in url or 'foro' in url:
            csv.foro = True
            csv.save()
            f_ += 1
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = csv.delete()
        else:
            try:
                response = requests.get(url, headers=USER_AGENT)
                response.raise_for_status()
                c = response.content

                soup = BeautifulSoup(c, 'html.parser')
                x_class = re.compile('com[a-z]+')
                comment_class_id = soup.find_all(['div', 'section', 'footer', 'p', 'span', 'li'], attrs={'class':x_class})
                for comment in comment_class_id:
                    comment_link = comment.find_all('a', attrs = {'rel':'nofollow'}, href=True)
                    for comment_link_to in comment_link:
                        comment_link_to = comment_link_to['href']
                        if to_url == comment_link_to:
                            s_ += 1
                        else:
                            pass
            except:
                print('no se pudo acceder a: ' + url)
                eraseTwo = csv.delete()

        if s_ > 0:
            csv.site_link = 'Comentario'
            csv.save()
        else:
            pass

        if f_ > 0:
            csv.site_link = 'Foro'
            csv.save()
        else:
            pass

def scrapper_79(array, search):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.backlink
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = search.get(pk=pk)

        if 'forum' in url or 'foro' in url:
            csv.foro = True
            csv.save()
            f_ += 1
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = csv.delete()
        else:
            try:
                response = requests.get(url, headers=USER_AGENT)
                response.raise_for_status()
                c = response.content

                soup = BeautifulSoup(c, 'html.parser')
                x_class = re.compile('com[a-z]+')
                comment_class_id = soup.find_all(['div', 'section', 'footer', 'p', 'span', 'li'], attrs={'class':x_class})
                for comment in comment_class_id:
                    comment_link = comment.find_all('a', attrs = {'rel':'nofollow'}, href=True)
                    for comment_link_to in comment_link:
                        comment_link_to = comment_link_to['href']
                        if to_url == comment_link_to:
                            s_ += 1
                        else:
                            pass
            except:
                print('no se pudo acceder a: ' + url)
                eraseTwo = csv.delete()

        if s_ > 0:
            csv.site_link = 'Comentario'
            csv.save()
        else:
            pass

        if f_ > 0:
            csv.site_link = 'Foro'
            csv.save()
        else:
            pass

def scrapper_80(array, search):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.backlink
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = search.get(pk=pk)

        if 'forum' in url or 'foro' in url:
            csv.foro = True
            csv.save()
            f_ += 1
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = csv.delete()
        else:
            try:
                response = requests.get(url, headers=USER_AGENT)
                response.raise_for_status()
                c = response.content

                soup = BeautifulSoup(c, 'html.parser')
                x_class = re.compile('com[a-z]+')
                comment_class_id = soup.find_all(['div', 'section', 'footer', 'p', 'span', 'li'], attrs={'class':x_class})
                for comment in comment_class_id:
                    comment_link = comment.find_all('a', attrs = {'rel':'nofollow'}, href=True)
                    for comment_link_to in comment_link:
                        comment_link_to = comment_link_to['href']
                        if to_url == comment_link_to:
                            s_ += 1
                        else:
                            pass
            except:
                print('no se pudo acceder a: ' + url)
                eraseTwo = csv.delete()

        if s_ > 0:
            csv.site_link = 'Comentario'
            csv.save()
        else:
            pass

        if f_ > 0:
            csv.site_link = 'Foro'
            csv.save()
        else:
            pass


def scrapper_81(array, search):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.backlink
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = search.get(pk=pk)

        if 'forum' in url or 'foro' in url:
            csv.foro = True
            csv.save()
            f_ += 1
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = csv.delete()
        else:
            try:
                response = requests.get(url, headers=USER_AGENT)
                response.raise_for_status()
                c = response.content

                soup = BeautifulSoup(c, 'html.parser')
                x_class = re.compile('com[a-z]+')
                comment_class_id = soup.find_all(['div', 'section', 'footer', 'p', 'span', 'li'], attrs={'class':x_class})
                for comment in comment_class_id:
                    comment_link = comment.find_all('a', attrs = {'rel':'nofollow'}, href=True)
                    for comment_link_to in comment_link:
                        comment_link_to = comment_link_to['href']
                        if to_url == comment_link_to:
                            s_ += 1
                        else:
                            pass
            except:
                print('no se pudo acceder a: ' + url)
                eraseTwo = csv.delete()

        if s_ > 0:
            csv.site_link = 'Comentario'
            csv.save()
        else:
            pass

        if f_ > 0:
            csv.site_link = 'Foro'
            csv.save()
        else:
            pass

def scrapper_82(array, search):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.backlink
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = search.get(pk=pk)

        if 'forum' in url or 'foro' in url:
            csv.foro = True
            csv.save()
            f_ += 1
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = csv.delete()
        else:
            try:
                response = requests.get(url, headers=USER_AGENT)
                response.raise_for_status()
                c = response.content

                soup = BeautifulSoup(c, 'html.parser')
                x_class = re.compile('com[a-z]+')
                comment_class_id = soup.find_all(['div', 'section', 'footer', 'p', 'span', 'li'], attrs={'class':x_class})
                for comment in comment_class_id:
                    comment_link = comment.find_all('a', attrs = {'rel':'nofollow'}, href=True)
                    for comment_link_to in comment_link:
                        comment_link_to = comment_link_to['href']
                        if to_url == comment_link_to:
                            s_ += 1
                        else:
                            pass
            except:
                print('no se pudo acceder a: ' + url)
                eraseTwo = csv.delete()

        if s_ > 0:
            csv.site_link = 'Comentario'
            csv.save()
        else:
            pass

        if f_ > 0:
            csv.site_link = 'Foro'
            csv.save()
        else:
            pass

def scrapper_83(array, search):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.backlink
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = search.get(pk=pk)

        if 'forum' in url or 'foro' in url:
            csv.foro = True
            csv.save()
            f_ += 1
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = csv.delete()
        else:
            try:
                response = requests.get(url, headers=USER_AGENT)
                response.raise_for_status()
                c = response.content

                soup = BeautifulSoup(c, 'html.parser')
                x_class = re.compile('com[a-z]+')
                comment_class_id = soup.find_all(['div', 'section', 'footer', 'p', 'span', 'li'], attrs={'class':x_class})
                for comment in comment_class_id:
                    comment_link = comment.find_all('a', attrs = {'rel':'nofollow'}, href=True)
                    for comment_link_to in comment_link:
                        comment_link_to = comment_link_to['href']
                        if to_url == comment_link_to:
                            s_ += 1
                        else:
                            pass
            except:
                print('no se pudo acceder a: ' + url)
                eraseTwo = csv.delete()

        if s_ > 0:
            csv.site_link = 'Comentario'
            csv.save()
        else:
            pass

        if f_ > 0:
            csv.site_link = 'Foro'
            csv.save()
        else:
            pass

def scrapper_84(array, search):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.backlink
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = search.get(pk=pk)

        if 'forum' in url or 'foro' in url:
            csv.foro = True
            csv.save()
            f_ += 1
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = csv.delete()
        else:
            try:
                response = requests.get(url, headers=USER_AGENT)
                response.raise_for_status()
                c = response.content

                soup = BeautifulSoup(c, 'html.parser')
                x_class = re.compile('com[a-z]+')
                comment_class_id = soup.find_all(['div', 'section', 'footer', 'p', 'span', 'li'], attrs={'class':x_class})
                for comment in comment_class_id:
                    comment_link = comment.find_all('a', attrs = {'rel':'nofollow'}, href=True)
                    for comment_link_to in comment_link:
                        comment_link_to = comment_link_to['href']
                        if to_url == comment_link_to:
                            s_ += 1
                        else:
                            pass
            except:
                print('no se pudo acceder a: ' + url)
                eraseTwo = csv.delete()

        if s_ > 0:
            csv.site_link = 'Comentario'
            csv.save()
        else:
            pass

        if f_ > 0:
            csv.site_link = 'Foro'
            csv.save()
        else:
            pass

def scrapper_85(array, search):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.backlink
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = search.get(pk=pk)

        if 'forum' in url or 'foro' in url:
            csv.foro = True
            csv.save()
            f_ += 1
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = csv.delete()
        else:
            try:
                response = requests.get(url, headers=USER_AGENT)
                response.raise_for_status()
                c = response.content

                soup = BeautifulSoup(c, 'html.parser')
                x_class = re.compile('com[a-z]+')
                comment_class_id = soup.find_all(['div', 'section', 'footer', 'p', 'span', 'li'], attrs={'class':x_class})
                for comment in comment_class_id:
                    comment_link = comment.find_all('a', attrs = {'rel':'nofollow'}, href=True)
                    for comment_link_to in comment_link:
                        comment_link_to = comment_link_to['href']
                        if to_url == comment_link_to:
                            s_ += 1
                        else:
                            pass
            except:
                print('no se pudo acceder a: ' + url)
                eraseTwo = csv.delete()

        if s_ > 0:
            csv.site_link = 'Comentario'
            csv.save()
        else:
            pass

        if f_ > 0:
            csv.site_link = 'Foro'
            csv.save()
        else:
            pass

def scrapper_86(array, search):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.backlink
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = search.get(pk=pk)

        if 'forum' in url or 'foro' in url:
            csv.foro = True
            csv.save()
            f_ += 1
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = csv.delete()
        else:
            try:
                response = requests.get(url, headers=USER_AGENT)
                response.raise_for_status()
                c = response.content

                soup = BeautifulSoup(c, 'html.parser')
                x_class = re.compile('com[a-z]+')
                comment_class_id = soup.find_all(['div', 'section', 'footer', 'p', 'span', 'li'], attrs={'class':x_class})
                for comment in comment_class_id:
                    comment_link = comment.find_all('a', attrs = {'rel':'nofollow'}, href=True)
                    for comment_link_to in comment_link:
                        comment_link_to = comment_link_to['href']
                        if to_url == comment_link_to:
                            s_ += 1
                        else:
                            pass
            except:
                print('no se pudo acceder a: ' + url)
                eraseTwo = csv.delete()

        if s_ > 0:
            csv.site_link = 'Comentario'
            csv.save()
        else:
            pass

        if f_ > 0:
            csv.site_link = 'Foro'
            csv.save()
        else:
            pass


def scrapper_87(array, search):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.backlink
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = search.get(pk=pk)

        if 'forum' in url or 'foro' in url:
            csv.foro = True
            csv.save()
            f_ += 1
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = csv.delete()
        else:
            try:
                response = requests.get(url, headers=USER_AGENT)
                response.raise_for_status()
                c = response.content

                soup = BeautifulSoup(c, 'html.parser')
                x_class = re.compile('com[a-z]+')
                comment_class_id = soup.find_all(['div', 'section', 'footer', 'p', 'span', 'li'], attrs={'class':x_class})
                for comment in comment_class_id:
                    comment_link = comment.find_all('a', attrs = {'rel':'nofollow'}, href=True)
                    for comment_link_to in comment_link:
                        comment_link_to = comment_link_to['href']
                        if to_url == comment_link_to:
                            s_ += 1
                        else:
                            pass
            except:
                print('no se pudo acceder a: ' + url)
                eraseTwo = csv.delete()

        if s_ > 0:
            csv.site_link = 'Comentario'
            csv.save()
        else:
            pass

        if f_ > 0:
            csv.site_link = 'Foro'
            csv.save()
        else:
            pass

def scrapper_88(array, search):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.backlink
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = search.get(pk=pk)

        if 'forum' in url or 'foro' in url:
            csv.foro = True
            csv.save()
            f_ += 1
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = csv.delete()
        else:
            try:
                response = requests.get(url, headers=USER_AGENT)
                response.raise_for_status()
                c = response.content

                soup = BeautifulSoup(c, 'html.parser')
                x_class = re.compile('com[a-z]+')
                comment_class_id = soup.find_all(['div', 'section', 'footer', 'p', 'span', 'li'], attrs={'class':x_class})
                for comment in comment_class_id:
                    comment_link = comment.find_all('a', attrs = {'rel':'nofollow'}, href=True)
                    for comment_link_to in comment_link:
                        comment_link_to = comment_link_to['href']
                        if to_url == comment_link_to:
                            s_ += 1
                        else:
                            pass
            except:
                print('no se pudo acceder a: ' + url)
                eraseTwo = csv.delete()

        if s_ > 0:
            csv.site_link = 'Comentario'
            csv.save()
        else:
            pass

        if f_ > 0:
            csv.site_link = 'Foro'
            csv.save()
        else:
            pass

def scrapper_89(array, search):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.backlink
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = search.get(pk=pk)

        if 'forum' in url or 'foro' in url:
            csv.foro = True
            csv.save()
            f_ += 1
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = csv.delete()
        else:
            try:
                response = requests.get(url, headers=USER_AGENT)
                response.raise_for_status()
                c = response.content

                soup = BeautifulSoup(c, 'html.parser')
                x_class = re.compile('com[a-z]+')
                comment_class_id = soup.find_all(['div', 'section', 'footer', 'p', 'span', 'li'], attrs={'class':x_class})
                for comment in comment_class_id:
                    comment_link = comment.find_all('a', attrs = {'rel':'nofollow'}, href=True)
                    for comment_link_to in comment_link:
                        comment_link_to = comment_link_to['href']
                        if to_url == comment_link_to:
                            s_ += 1
                        else:
                            pass
            except:
                print('no se pudo acceder a: ' + url)
                eraseTwo = csv.delete()

        if s_ > 0:
            csv.site_link = 'Comentario'
            csv.save()
        else:
            pass

        if f_ > 0:
            csv.site_link = 'Foro'
            csv.save()
        else:
            pass

def scrapper_90(array, search):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.backlink
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = search.get(pk=pk)

        if 'forum' in url or 'foro' in url:
            csv.foro = True
            csv.save()
            f_ += 1
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = csv.delete()
        else:
            try:
                response = requests.get(url, headers=USER_AGENT)
                response.raise_for_status()
                c = response.content

                soup = BeautifulSoup(c, 'html.parser')
                x_class = re.compile('com[a-z]+')
                comment_class_id = soup.find_all(['div', 'section', 'footer', 'p', 'span', 'li'], attrs={'class':x_class})
                for comment in comment_class_id:
                    comment_link = comment.find_all('a', attrs = {'rel':'nofollow'}, href=True)
                    for comment_link_to in comment_link:
                        comment_link_to = comment_link_to['href']
                        if to_url == comment_link_to:
                            s_ += 1
                        else:
                            pass
            except:
                print('no se pudo acceder a: ' + url)
                eraseTwo = csv.delete()

        if s_ > 0:
            csv.site_link = 'Comentario'
            csv.save()
        else:
            pass

        if f_ > 0:
            csv.site_link = 'Foro'
            csv.save()
        else:
            pass


def scrapper_91(array, search):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.backlink
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = search.get(pk=pk)

        if 'forum' in url or 'foro' in url:
            csv.foro = True
            csv.save()
            f_ += 1
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = csv.delete()
        else:
            try:
                response = requests.get(url, headers=USER_AGENT)
                response.raise_for_status()
                c = response.content

                soup = BeautifulSoup(c, 'html.parser')
                x_class = re.compile('com[a-z]+')
                comment_class_id = soup.find_all(['div', 'section', 'footer', 'p', 'span', 'li'], attrs={'class':x_class})
                for comment in comment_class_id:
                    comment_link = comment.find_all('a', attrs = {'rel':'nofollow'}, href=True)
                    for comment_link_to in comment_link:
                        comment_link_to = comment_link_to['href']
                        if to_url == comment_link_to:
                            s_ += 1
                        else:
                            pass
            except:
                print('no se pudo acceder a: ' + url)
                eraseTwo = csv.delete()

        if s_ > 0:
            csv.site_link = 'Comentario'
            csv.save()
        else:
            pass

        if f_ > 0:
            csv.site_link = 'Foro'
            csv.save()
        else:
            pass


def scrapper_92(array, search):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.backlink
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = search.get(pk=pk)

        if 'forum' in url or 'foro' in url:
            csv.foro = True
            csv.save()
            f_ += 1
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = csv.delete()
        else:
            try:
                response = requests.get(url, headers=USER_AGENT)
                response.raise_for_status()
                c = response.content

                soup = BeautifulSoup(c, 'html.parser')
                x_class = re.compile('com[a-z]+')
                comment_class_id = soup.find_all(['div', 'section', 'footer', 'p', 'span', 'li'], attrs={'class':x_class})
                for comment in comment_class_id:
                    comment_link = comment.find_all('a', attrs = {'rel':'nofollow'}, href=True)
                    for comment_link_to in comment_link:
                        comment_link_to = comment_link_to['href']
                        if to_url == comment_link_to:
                            s_ += 1
                        else:
                            pass
            except:
                print('no se pudo acceder a: ' + url)
                eraseTwo = csv.delete()

        if s_ > 0:
            csv.site_link = 'Comentario'
            csv.save()
        else:
            pass

        if f_ > 0:
            csv.site_link = 'Foro'
            csv.save()
        else:
            pass

def scrapper_93(array, search):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.backlink
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = search.get(pk=pk)

        if 'forum' in url or 'foro' in url:
            csv.foro = True
            csv.save()
            f_ += 1
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = csv.delete()
        else:
            try:
                response = requests.get(url, headers=USER_AGENT)
                response.raise_for_status()
                c = response.content

                soup = BeautifulSoup(c, 'html.parser')
                x_class = re.compile('com[a-z]+')
                comment_class_id = soup.find_all(['div', 'section', 'footer', 'p', 'span', 'li'], attrs={'class':x_class})
                for comment in comment_class_id:
                    comment_link = comment.find_all('a', attrs = {'rel':'nofollow'}, href=True)
                    for comment_link_to in comment_link:
                        comment_link_to = comment_link_to['href']
                        if to_url == comment_link_to:
                            s_ += 1
                        else:
                            pass
            except:
                print('no se pudo acceder a: ' + url)
                eraseTwo = csv.delete()

        if s_ > 0:
            csv.site_link = 'Comentario'
            csv.save()
        else:
            pass

        if f_ > 0:
            csv.site_link = 'Foro'
            csv.save()
        else:
            pass

def scrapper_94(array, search):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.backlink
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = search.get(pk=pk)

        if 'forum' in url or 'foro' in url:
            csv.foro = True
            csv.save()
            f_ += 1
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = csv.delete()
        else:
            try:
                response = requests.get(url, headers=USER_AGENT)
                response.raise_for_status()
                c = response.content

                soup = BeautifulSoup(c, 'html.parser')
                x_class = re.compile('com[a-z]+')
                comment_class_id = soup.find_all(['div', 'section', 'footer', 'p', 'span', 'li'], attrs={'class':x_class})
                for comment in comment_class_id:
                    comment_link = comment.find_all('a', attrs = {'rel':'nofollow'}, href=True)
                    for comment_link_to in comment_link:
                        comment_link_to = comment_link_to['href']
                        if to_url == comment_link_to:
                            s_ += 1
                        else:
                            pass
            except:
                print('no se pudo acceder a: ' + url)
                eraseTwo = csv.delete()

        if s_ > 0:
            csv.site_link = 'Comentario'
            csv.save()
        else:
            pass

        if f_ > 0:
            csv.site_link = 'Foro'
            csv.save()
        else:
            pass

def scrapper_95(array, search):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.backlink
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = search.get(pk=pk)

        if 'forum' in url or 'foro' in url:
            csv.foro = True
            csv.save()
            f_ += 1
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = csv.delete()
        else:
            try:
                response = requests.get(url, headers=USER_AGENT)
                response.raise_for_status()
                c = response.content

                soup = BeautifulSoup(c, 'html.parser')
                x_class = re.compile('com[a-z]+')
                comment_class_id = soup.find_all(['div', 'section', 'footer', 'p', 'span', 'li'], attrs={'class':x_class})
                for comment in comment_class_id:
                    comment_link = comment.find_all('a', attrs = {'rel':'nofollow'}, href=True)
                    for comment_link_to in comment_link:
                        comment_link_to = comment_link_to['href']
                        if to_url == comment_link_to:
                            s_ += 1
                        else:
                            pass
            except:
                print('no se pudo acceder a: ' + url)
                eraseTwo = csv.delete()

        if s_ > 0:
            csv.site_link = 'Comentario'
            csv.save()
        else:
            pass

        if f_ > 0:
            csv.site_link = 'Foro'
            csv.save()
        else:
            pass

def scrapper_96(array, search):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.backlink
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = search.get(pk=pk)

        if 'forum' in url or 'foro' in url:
            csv.foro = True
            csv.save()
            f_ += 1
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = csv.delete()
        else:
            try:
                response = requests.get(url, headers=USER_AGENT)
                response.raise_for_status()
                c = response.content

                soup = BeautifulSoup(c, 'html.parser')
                x_class = re.compile('com[a-z]+')
                comment_class_id = soup.find_all(['div', 'section', 'footer', 'p', 'span', 'li'], attrs={'class':x_class})
                for comment in comment_class_id:
                    comment_link = comment.find_all('a', attrs = {'rel':'nofollow'}, href=True)
                    for comment_link_to in comment_link:
                        comment_link_to = comment_link_to['href']
                        if to_url == comment_link_to:
                            s_ += 1
                        else:
                            pass
            except:
                print('no se pudo acceder a: ' + url)
                eraseTwo = csv.delete()

        if s_ > 0:
            csv.site_link = 'Comentario'
            csv.save()
        else:
            pass

        if f_ > 0:
            csv.site_link = 'Foro'
            csv.save()
        else:
            pass

def scrapper_97(array, search):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.backlink
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = search.get(pk=pk)

        if 'forum' in url or 'foro' in url:
            csv.foro = True
            csv.save()
            f_ += 1
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = csv.delete()
        else:
            try:
                response = requests.get(url, headers=USER_AGENT)
                response.raise_for_status()
                c = response.content

                soup = BeautifulSoup(c, 'html.parser')
                x_class = re.compile('com[a-z]+')
                comment_class_id = soup.find_all(['div', 'section', 'footer', 'p', 'span', 'li'], attrs={'class':x_class})
                for comment in comment_class_id:
                    comment_link = comment.find_all('a', attrs = {'rel':'nofollow'}, href=True)
                    for comment_link_to in comment_link:
                        comment_link_to = comment_link_to['href']
                        if to_url == comment_link_to:
                            s_ += 1
                        else:
                            pass
            except:
                print('no se pudo acceder a: ' + url)
                eraseTwo = csv.delete()

        if s_ > 0:
            csv.site_link = 'Comentario'
            csv.save()
        else:
            pass

        if f_ > 0:
            csv.site_link = 'Foro'
            csv.save()
        else:
            pass


def scrapper_98(array, search):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.backlink
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = search.get(pk=pk)

        if 'forum' in url or 'foro' in url:
            csv.foro = True
            csv.save()
            f_ += 1
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = csv.delete()
        else:
            try:
                response = requests.get(url, headers=USER_AGENT)
                response.raise_for_status()
                c = response.content

                soup = BeautifulSoup(c, 'html.parser')
                x_class = re.compile('com[a-z]+')
                comment_class_id = soup.find_all(['div', 'section', 'footer', 'p', 'span', 'li'], attrs={'class':x_class})
                for comment in comment_class_id:
                    comment_link = comment.find_all('a', attrs = {'rel':'nofollow'}, href=True)
                    for comment_link_to in comment_link:
                        comment_link_to = comment_link_to['href']
                        if to_url == comment_link_to:
                            s_ += 1
                        else:
                            pass
            except:
                print('no se pudo acceder a: ' + url)
                eraseTwo = csv.delete()

        if s_ > 0:
            csv.site_link = 'Comentario'
            csv.save()
        else:
            pass

        if f_ > 0:
            csv.site_link = 'Foro'
            csv.save()
        else:
            pass

def scrapper_99(array, search):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.backlink
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = search.get(pk=pk)

        if 'forum' in url or 'foro' in url:
            csv.foro = True
            csv.save()
            f_ += 1
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = csv.delete()
        else:
            try:
                response = requests.get(url, headers=USER_AGENT)
                response.raise_for_status()
                c = response.content

                soup = BeautifulSoup(c, 'html.parser')
                x_class = re.compile('com[a-z]+')
                comment_class_id = soup.find_all(['div', 'section', 'footer', 'p', 'span', 'li'], attrs={'class':x_class})
                for comment in comment_class_id:
                    comment_link = comment.find_all('a', attrs = {'rel':'nofollow'}, href=True)
                    for comment_link_to in comment_link:
                        comment_link_to = comment_link_to['href']
                        if to_url == comment_link_to:
                            s_ += 1
                        else:
                            pass
            except:
                print('no se pudo acceder a: ' + url)
                eraseTwo = csv.delete()

        if s_ > 0:
            csv.site_link = 'Comentario'
            csv.save()
        else:
            pass

        if f_ > 0:
            csv.site_link = 'Foro'
            csv.save()
        else:
            pass
