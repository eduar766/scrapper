from .models import UrlSearch, Backlinks, GoogleSearch, GoogleBD, Backlinks, ScrapperTest, SingleAhref

import threading
import time
import requests
from bs4 import BeautifulSoup
import urllib.request
import re

USER_AGENT = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}

def scrapper_0(array, links):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = links.get(pk=pk)

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


def scrapper_1(array, links):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = links.get(pk=pk)

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

def scrapper_2(array, links):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = links.get(pk=pk)

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

def scrapper_3(array, links):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = links.get(pk=pk)

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

def scrapper_4(array, links):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = links.get(pk=pk)

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

def scrapper_5(array, links):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = links.get(pk=pk)

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

def scrapper_6(array, links):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = links.get(pk=pk)

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


def scrapper_7(array, links):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = links.get(pk=pk)

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

def scrapper_8(array, links):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = links.get(pk=pk)

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

def scrapper_9(array, links):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = links.get(pk=pk)

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

def scrapper_10(array, links):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = links.get(pk=pk)

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


def scrapper_11(array, links):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = links.get(pk=pk)

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


def scrapper_12(array, links):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = links.get(pk=pk)

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

def scrapper_13(array, links):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = links.get(pk=pk)

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

def scrapper_14(array, links):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = links.get(pk=pk)

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

def scrapper_15(array, links):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = links.get(pk=pk)

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

def scrapper_16(array, links):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = links.get(pk=pk)

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

def scrapper_17(array, links):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = links.get(pk=pk)

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


def scrapper_18(array, links):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = links.get(pk=pk)

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

def scrapper_19(array, links):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = links.get(pk=pk)

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

def scrapper_20(array, links):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = links.get(pk=pk)

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


def scrapper_21(array, links):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = links.get(pk=pk)

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

def scrapper_22(array, links):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = links.get(pk=pk)

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

def scrapper_23(array, links):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = links.get(pk=pk)

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

def scrapper_24(array, links):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = links.get(pk=pk)

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

def scrapper_25(array, links):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = links.get(pk=pk)

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

def scrapper_26(array, links):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = links.get(pk=pk)

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


def scrapper_27(array, links):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = links.get(pk=pk)

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

def scrapper_28(array, links):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = links.get(pk=pk)

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

def scrapper_29(array, links):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = links.get(pk=pk)

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

def scrapper_30(array, links):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = links.get(pk=pk)

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


def scrapper_31(array, links):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = links.get(pk=pk)

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


def scrapper_32(array, links):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = links.get(pk=pk)

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

def scrapper_33(array, links):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = links.get(pk=pk)

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

def scrapper_34(array, links):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = links.get(pk=pk)

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

def scrapper_35(array, links):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = links.get(pk=pk)

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

def scrapper_36(array, links):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = links.get(pk=pk)

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

def scrapper_37(array, links):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = links.get(pk=pk)

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


def scrapper_38(array, links):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = links.get(pk=pk)

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

def scrapper_39(array, links):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = links.get(pk=pk)

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

def scrapper_40(array, links):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = links.get(pk=pk)

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


def scrapper_41(array, links):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = links.get(pk=pk)

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

def scrapper_42(array, links):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = links.get(pk=pk)

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

def scrapper_43(array, links):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = links.get(pk=pk)

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

def scrapper_44(array, links):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = links.get(pk=pk)

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

def scrapper_45(array, links):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = links.get(pk=pk)

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

def scrapper_46(array, links):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = links.get(pk=pk)

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


def scrapper_47(array, links):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = links.get(pk=pk)

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

def scrapper_48(array, links):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = links.get(pk=pk)

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

def scrapper_49(array, links):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = links.get(pk=pk)

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

def scrapper_50(array, links):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = links.get(pk=pk)

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


def scrapper_51(array, links):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = links.get(pk=pk)

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


def scrapper_52(array, links):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = links.get(pk=pk)

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

def scrapper_53(array, links):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = links.get(pk=pk)

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

def scrapper_54(array, links):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = links.get(pk=pk)

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

def scrapper_55(array, links):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = links.get(pk=pk)

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

def scrapper_56(array, links):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = links.get(pk=pk)

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

def scrapper_57(array, links):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = links.get(pk=pk)

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


def scrapper_58(array, links):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = links.get(pk=pk)

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

def scrapper_59(array, links):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = links.get(pk=pk)

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

def scrapper_60(array, links):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = links.get(pk=pk)

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


def scrapper_61(array, links):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = links.get(pk=pk)

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

def scrapper_62(array, links):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = links.get(pk=pk)

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

def scrapper_63(array, links):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = links.get(pk=pk)

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

def scrapper_64(array, links):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = links.get(pk=pk)

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

def scrapper_65(array, links):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = links.get(pk=pk)

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

def scrapper_66(array, links):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = links.get(pk=pk)

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


def scrapper_67(array, links):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = links.get(pk=pk)

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

def scrapper_68(array, links):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = links.get(pk=pk)

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

def scrapper_69(array, links):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = links.get(pk=pk)

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

def scrapper_70(array, links):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = links.get(pk=pk)

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


def scrapper_71(array, links):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = links.get(pk=pk)

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


def scrapper_72(array, links):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = links.get(pk=pk)

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

def scrapper_73(array, links):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = links.get(pk=pk)

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

def scrapper_74(array, links):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = links.get(pk=pk)

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

def scrapper_75(array, links):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = links.get(pk=pk)

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

def scrapper_76(array, links):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = links.get(pk=pk)

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

def scrapper_77(array, links):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = links.get(pk=pk)

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


def scrapper_78(array, links):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = links.get(pk=pk)

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

def scrapper_79(array, links):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = links.get(pk=pk)

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

def scrapper_80(array, links):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = links.get(pk=pk)

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


def scrapper_81(array, links):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = links.get(pk=pk)

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

def scrapper_82(array, links):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = links.get(pk=pk)

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

def scrapper_83(array, links):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = links.get(pk=pk)

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

def scrapper_84(array, links):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = links.get(pk=pk)

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

def scrapper_85(array, links):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = links.get(pk=pk)

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

def scrapper_86(array, links):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = links.get(pk=pk)

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


def scrapper_87(array, links):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = links.get(pk=pk)

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

def scrapper_88(array, links):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = links.get(pk=pk)

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

def scrapper_89(array, links):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = links.get(pk=pk)

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

def scrapper_90(array, links):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = links.get(pk=pk)

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


def scrapper_91(array, links):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = links.get(pk=pk)

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


def scrapper_92(array, links):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = links.get(pk=pk)

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

def scrapper_93(array, links):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = links.get(pk=pk)

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

def scrapper_94(array, links):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = links.get(pk=pk)

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

def scrapper_95(array, links):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = links.get(pk=pk)

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

def scrapper_96(array, links):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = links.get(pk=pk)

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

def scrapper_97(array, links):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = links.get(pk=pk)

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


def scrapper_98(array, links):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = links.get(pk=pk)

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

def scrapper_99(array, links):
    for l in array:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0
        f_ = 0

        csv = links.get(pk=pk)

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
