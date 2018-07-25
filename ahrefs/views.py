from django.shortcuts import render, redirect, get_object_or_404
import requests
from .models import UrlSearch, Backlinks, GoogleSearch, GoogleBD, CSV_import, ScrapperTest, SingleAhref, TokenAhref
from .filters import BacklinksFilter, CSVFilter
from .forms import GoogleForm, ScrapperForm, SingleAhrefsForm
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

import requests
from bs4 import BeautifulSoup
import urllib.request
import time
import re
import xlsxwriter
from urllib.parse import urljoin, urlparse



USER_AGENT = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}

import random

def get_token():
    my_token = random.randint(1,99999)
    return my_token

# Create your views here.
@login_required
def pre_index(request):
    request.session['session_token'] = 0
    return redirect('index')

@login_required
def index(request):
    if request.session['session_token'] == 0:
        request.session['session_token'] = get_token()
    else:
        request.session['session_token'] = request.session['session_token']

    session = request.session['session_token']
    print(session)

    csv = CSV_import.objects.filter(session_id__exact = session ).delete()
    google = GoogleBD.objects.filter(session_id__exact = session ).delete()
    googleKey = GoogleSearch.objects.filter(session_id__exact = session ).delete()
    googleSingle = SingleAhref.objects.filter(session_id__exact = session ).delete()
    url = UrlSearch.objects.filter(session_id__exact = session ).delete()
    bk = Backlinks.objects.filter(session_id__exact = session ).delete()

    return redirect('search_bk')

import ahrefs.process_ahrefs_request as handle

@login_required
def backlinks(request):
    t = time.time()
    search_token = TokenAhref.objects.get(pk=1)
    #token = 'ef2fdefde20c70af3ad0ccd6352d1bedda36a5e1'
    token = search_token.token
    url_ahref = 'http://apiv2.ahrefs.com?from=backlinks&target=ahrefs.com&limit=100&mode=domain&order_by=ahrefs_rank%3Adesc&output=json&token={}'

    response = requests.get(url_ahref.format(token)).json()
    response = response['refpages']
    lenght = len(response)
    div = int(lenght / 20 )
    p = 0

    session_id = request.session['session_token']

    collect = []
    while p < lenght:
        if p == 0:
            a = response[:div]
            collect.append(a)
        else:
            h = div + p
            a = response[p:h]
            collect.append(a)
        p += div

    print(collect)

    t1= threading.Thread(target=handle.ahref_0, args=(collect[0], session_id))
    t2= threading.Thread(target=handle.ahref_1, args=(collect[1], session_id))
    t3= threading.Thread(target=handle.ahref_2, args=(collect[2], session_id))
    t4= threading.Thread(target=handle.ahref_3, args=(collect[3], session_id))
    t5= threading.Thread(target=handle.ahref_4, args=(collect[4], session_id))
    t6= threading.Thread(target=handle.ahref_5, args=(collect[5], session_id))
    t7= threading.Thread(target=handle.ahref_6, args=(collect[6], session_id))
    t8= threading.Thread(target=handle.ahref_7, args=(collect[7], session_id))
    t9= threading.Thread(target=handle.ahref_8, args=(collect[8], session_id))
    t10= threading.Thread(target=handle.ahref_9, args=(collect[9], session_id))
    t11= threading.Thread(target=handle.ahref_10, args=(collect[10], session_id))
    t12= threading.Thread(target=handle.ahref_11, args=(collect[11], session_id))
    t13= threading.Thread(target=handle.ahref_12, args=(collect[12], session_id))
    t14= threading.Thread(target=handle.ahref_13, args=(collect[13], session_id))
    t15= threading.Thread(target=handle.ahref_14, args=(collect[14], session_id))
    t16= threading.Thread(target=handle.ahref_15, args=(collect[15], session_id))
    t17= threading.Thread(target=handle.ahref_16, args=(collect[16], session_id))
    t18= threading.Thread(target=handle.ahref_17, args=(collect[17], session_id))
    t19= threading.Thread(target=handle.ahref_18, args=(collect[18], session_id))
    t20= threading.Thread(target=handle.ahref_19, args=(collect[19], session_id))


    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()
    t8.start()
    t9.start()
    t10.start()
    t11.start()
    t12.start()
    t13.start()
    t14.start()
    t15.start()
    t16.start()
    t17.start()
    t18.start()
    t19.start()
    t20.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()
    t7.join()
    t8.join()
    t9.join()
    t10.join()
    t11.join()
    t12.join()
    t13.join()
    t14.join()
    t15.join()
    t16.join()
    t17.join()
    t18.join()
    t19.join()
    t20.join()

    print("Ahref done in : ",time.time()-t)

    return redirect('backlinks_scrapper')


import ahrefs.scrapper_ahrefs as ah
@login_required
def backlinks_scrapper(request):
    t = time.time()
    links = Backlinks.objects.all()
    lenght = len(links)
    div = int(lenght / 100)

    p = 0

    collect = []
    while p < lenght:
        if p == 0:
            a = links[:div]
            collect.append(a)
        else:
            h = div + p
            a = links[p:h]
            collect.append(a)
        p += div

    print(links)

    t1= threading.Thread(target=ah.scrapper_0, args=(collect[0], links))
    t2= threading.Thread(target=ah.scrapper_1, args=(collect[1], links))
    t3= threading.Thread(target=ah.scrapper_2, args=(collect[2], links))
    t4= threading.Thread(target=ah.scrapper_3, args=(collect[3], links))
    t5= threading.Thread(target=ah.scrapper_4, args=(collect[4], links))
    t6= threading.Thread(target=ah.scrapper_5, args=(collect[5], links))
    t7= threading.Thread(target=ah.scrapper_6, args=(collect[6], links))
    t8= threading.Thread(target=ah.scrapper_7, args=(collect[7], links))
    t9= threading.Thread(target=ah.scrapper_8, args=(collect[8], links))
    t10= threading.Thread(target=ah.scrapper_9, args=(collect[9], links))
    t11= threading.Thread(target=ah.scrapper_10, args=(collect[10], links))
    t12= threading.Thread(target=ah.scrapper_11, args=(collect[11], links))
    t13= threading.Thread(target=ah.scrapper_12, args=(collect[12], links))
    t14= threading.Thread(target=ah.scrapper_13, args=(collect[13], links))
    t15= threading.Thread(target=ah.scrapper_14, args=(collect[14], links))
    t16= threading.Thread(target=ah.scrapper_15, args=(collect[15], links))
    t17= threading.Thread(target=ah.scrapper_16, args=(collect[16], links))
    t18= threading.Thread(target=ah.scrapper_17, args=(collect[17], links))
    t19= threading.Thread(target=ah.scrapper_18, args=(collect[18], links))
    t20= threading.Thread(target=ah.scrapper_19, args=(collect[19], links))
    t21= threading.Thread(target=ah.scrapper_20, args=(collect[20], links))
    t22= threading.Thread(target=ah.scrapper_21, args=(collect[21], links))
    t23= threading.Thread(target=ah.scrapper_22, args=(collect[22], links))
    t24= threading.Thread(target=ah.scrapper_23, args=(collect[23], links))
    t25= threading.Thread(target=ah.scrapper_24, args=(collect[24], links))
    t26= threading.Thread(target=ah.scrapper_25, args=(collect[25], links))
    t27= threading.Thread(target=ah.scrapper_26, args=(collect[26], links))
    t28= threading.Thread(target=ah.scrapper_27, args=(collect[27], links))
    t29= threading.Thread(target=ah.scrapper_28, args=(collect[28], links))
    t30= threading.Thread(target=ah.scrapper_29, args=(collect[29], links))
    t31= threading.Thread(target=ah.scrapper_30, args=(collect[30], links))
    t32= threading.Thread(target=ah.scrapper_31, args=(collect[31], links))
    t33= threading.Thread(target=ah.scrapper_32, args=(collect[32], links))
    t34= threading.Thread(target=ah.scrapper_33, args=(collect[33], links))
    t35= threading.Thread(target=ah.scrapper_34, args=(collect[34], links))
    t36= threading.Thread(target=ah.scrapper_35, args=(collect[35], links))
    t37= threading.Thread(target=ah.scrapper_36, args=(collect[36], links))
    t38= threading.Thread(target=ah.scrapper_37, args=(collect[37], links))
    t39= threading.Thread(target=ah.scrapper_38, args=(collect[38], links))
    t40= threading.Thread(target=ah.scrapper_39, args=(collect[39], links))
    t41= threading.Thread(target=ah.scrapper_40, args=(collect[40], links))
    t42= threading.Thread(target=ah.scrapper_41, args=(collect[41], links))
    t43= threading.Thread(target=ah.scrapper_42, args=(collect[42], links))
    t44= threading.Thread(target=ah.scrapper_43, args=(collect[43], links))
    t45= threading.Thread(target=ah.scrapper_44, args=(collect[44], links))
    t46= threading.Thread(target=ah.scrapper_45, args=(collect[45], links))
    t47= threading.Thread(target=ah.scrapper_46, args=(collect[46], links))
    t48= threading.Thread(target=ah.scrapper_47, args=(collect[47], links))
    t49= threading.Thread(target=ah.scrapper_48, args=(collect[48], links))
    t50= threading.Thread(target=ah.scrapper_49, args=(collect[49], links))
    t51= threading.Thread(target=ah.scrapper_50, args=(collect[50], links))
    t52= threading.Thread(target=ah.scrapper_51, args=(collect[51], links))
    t53= threading.Thread(target=ah.scrapper_52, args=(collect[52], links))
    t54= threading.Thread(target=ah.scrapper_53, args=(collect[53], links))
    t55= threading.Thread(target=ah.scrapper_54, args=(collect[54], links))
    t56= threading.Thread(target=ah.scrapper_55, args=(collect[55], links))
    t57= threading.Thread(target=ah.scrapper_56, args=(collect[56], links))
    t58= threading.Thread(target=ah.scrapper_57, args=(collect[57], links))
    t59= threading.Thread(target=ah.scrapper_58, args=(collect[58], links))
    t60= threading.Thread(target=ah.scrapper_59, args=(collect[59], links))
    t61= threading.Thread(target=ah.scrapper_60, args=(collect[60], links))
    t62= threading.Thread(target=ah.scrapper_61, args=(collect[61], links))
    t63= threading.Thread(target=ah.scrapper_62, args=(collect[62], links))
    t64= threading.Thread(target=ah.scrapper_63, args=(collect[63], links))
    t65= threading.Thread(target=ah.scrapper_64, args=(collect[64], links))
    t66= threading.Thread(target=ah.scrapper_65, args=(collect[65], links))
    t67= threading.Thread(target=ah.scrapper_66, args=(collect[66], links))
    t68= threading.Thread(target=ah.scrapper_67, args=(collect[67], links))
    t69= threading.Thread(target=ah.scrapper_68, args=(collect[68], links))
    t70= threading.Thread(target=ah.scrapper_69, args=(collect[69], links))
    t71= threading.Thread(target=ah.scrapper_70, args=(collect[70], links))
    t72= threading.Thread(target=ah.scrapper_71, args=(collect[71], links))
    t73= threading.Thread(target=ah.scrapper_72, args=(collect[72], links))
    t74= threading.Thread(target=ah.scrapper_73, args=(collect[73], links))
    t75= threading.Thread(target=ah.scrapper_74, args=(collect[74], links))
    t76= threading.Thread(target=ah.scrapper_75, args=(collect[75], links))
    t77= threading.Thread(target=ah.scrapper_76, args=(collect[76], links))
    t78= threading.Thread(target=ah.scrapper_77, args=(collect[77], links))
    t79= threading.Thread(target=ah.scrapper_78, args=(collect[78], links))
    t80= threading.Thread(target=ah.scrapper_79, args=(collect[79], links))
    t81= threading.Thread(target=ah.scrapper_80, args=(collect[80], links))
    t82= threading.Thread(target=ah.scrapper_81, args=(collect[81], links))
    t83= threading.Thread(target=ah.scrapper_82, args=(collect[82], links))
    t84= threading.Thread(target=ah.scrapper_83, args=(collect[83], links))
    t85= threading.Thread(target=ah.scrapper_84, args=(collect[84], links))
    t86= threading.Thread(target=ah.scrapper_85, args=(collect[85], links))
    t87= threading.Thread(target=ah.scrapper_86, args=(collect[86], links))
    t88= threading.Thread(target=ah.scrapper_87, args=(collect[87], links))
    t89= threading.Thread(target=ah.scrapper_88, args=(collect[88], links))
    t90= threading.Thread(target=ah.scrapper_89, args=(collect[89], links))
    t91= threading.Thread(target=ah.scrapper_90, args=(collect[90], links))
    t92= threading.Thread(target=ah.scrapper_91, args=(collect[91], links))
    t93= threading.Thread(target=ah.scrapper_92, args=(collect[92], links))
    t94= threading.Thread(target=ah.scrapper_93, args=(collect[93], links))
    t95= threading.Thread(target=ah.scrapper_94, args=(collect[94], links))
    t96= threading.Thread(target=ah.scrapper_95, args=(collect[95], links))
    t97= threading.Thread(target=ah.scrapper_96, args=(collect[96], links))
    t98= threading.Thread(target=ah.scrapper_97, args=(collect[97], links))
    t99= threading.Thread(target=ah.scrapper_98, args=(collect[98], links))
    t100= threading.Thread(target=ah.scrapper_99, args=(collect[99], links))


    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()
    t8.start()
    t9.start()
    t10.start()
    t11.start()
    t12.start()
    t13.start()
    t14.start()
    t15.start()
    t16.start()
    t17.start()
    t18.start()
    t19.start()
    t20.start()
    t21.start()
    t22.start()
    t23.start()
    t24.start()
    t25.start()
    t26.start()
    t27.start()
    t28.start()
    t29.start()
    t30.start()
    t31.start()
    t32.start()
    t33.start()
    t34.start()
    t35.start()
    t36.start()
    t37.start()
    t38.start()
    t39.start()
    t40.start()
    t41.start()
    t42.start()
    t43.start()
    t44.start()
    t45.start()
    t46.start()
    t47.start()
    t48.start()
    t49.start()
    t50.start()
    t51.start()
    t52.start()
    t53.start()
    t54.start()
    t55.start()
    t56.start()
    t57.start()
    t58.start()
    t59.start()
    t60.start()
    t61.start()
    t62.start()
    t63.start()
    t64.start()
    t65.start()
    t66.start()
    t67.start()
    t68.start()
    t69.start()
    t70.start()
    t71.start()
    t72.start()
    t73.start()
    t74.start()
    t75.start()
    t76.start()
    t77.start()
    t78.start()
    t79.start()
    t80.start()
    t81.start()
    t82.start()
    t83.start()
    t84.start()
    t85.start()
    t86.start()
    t87.start()
    t88.start()
    t89.start()
    t90.start()
    t91.start()
    t92.start()
    t93.start()
    t94.start()
    t95.start()
    t96.start()
    t97.start()
    t98.start()
    t99.start()
    t100.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()
    t7.join()
    t8.join()
    t9.join()
    t10.join()
    t11.join()
    t12.join()
    t13.join()
    t14.join()
    t15.join()
    t16.join()
    t17.join()
    t18.join()
    t19.join()
    t20.join()
    t20.join()
    t21.join()
    t22.join()
    t23.join()
    t24.join()
    t25.join()
    t26.join()
    t27.join()
    t28.join()
    t29.join()
    t30.join()
    t31.join()
    t32.join()
    t33.join()
    t34.join()
    t35.join()
    t36.join()
    t37.join()
    t38.join()
    t39.join()
    t40.join()
    t41.join()
    t42.join()
    t43.join()
    t44.join()
    t45.join()
    t46.join()
    t47.join()
    t48.join()
    t49.join()
    t50.join()
    t51.join()
    t52.join()
    t53.join()
    t54.join()
    t55.join()
    t56.join()
    t57.join()
    t58.join()
    t59.join()
    t60.join()
    t61.join()
    t62.join()
    t63.join()
    t64.join()
    t65.join()
    t66.join()
    t67.join()
    t68.join()
    t69.join()
    t70.join()
    t71.join()
    t72.join()
    t73.join()
    t74.join()
    t75.join()
    t76.join()
    t77.join()
    t78.join()
    t79.join()
    t80.join()
    t81.join()
    t82.join()
    t83.join()
    t84.join()
    t85.join()
    t86.join()
    t87.join()
    t88.join()
    t89.join()
    t90.join()
    t91.join()
    t92.join()
    t93.join()
    t94.join()
    t95.join()
    t96.join()
    t97.join()
    t98.join()
    t99.join()
    t100.join()


    print("done in : ",time.time()-t)
    context = {'collect_data': links }
    return redirect('foro')


@login_required
def bk_results(request):
    session_id = request.session['session_token']

    bk_link = Backlinks.objects.filter(session_id = session_id)
    total = len(bk_link)
    collect_data= []
    bk_filter = BacklinksFilter(request.GET, queryset=bk_link)

    for bk in bk_link:
        collect_data.append(bk)

    context = {'collect_data': collect_data, 'total': total, 'filter':bk_filter}
    return render(request, 'ahrefs/backlinks/results.html', context)

@login_required
def search_bk(request):

    if request.method == 'POST':
        form = SingleAhrefsForm(request.POST)
        form.save()
        return redirect('single_ahrefs')

    form_single = SingleAhrefsForm()
    context = {'form_single': form_single}
    return render(request, 'ahrefs/backlinks/search_bk.html', context)

@login_required
def search_foro(request):
    # bk_link = Backlinks.objects.all()
    # foro = re.compile('rank[a-z]+')
    #
    # for url in bk_link:
    #     web_url = url.url_from
    #     pk = url.pk
    #
    #     if re.search(foro, web_url):
    #         url.site_link = 'Foro'
    #         url.save()
    #     else:
    #         pass


    return redirect('excel')

@login_required
def export_excel(request):
    workbook = xlsxwriter.Workbook('ahrefs/static/ahrefs/download/backlinks.xlsx')
    worksheet = workbook.add_worksheet()
    bold = workbook.add_format({'bold': True})

    worksheet.write('A1', 'URL', bold)
    worksheet.write('B1', 'Idioma', bold)
    worksheet.write('C1', 'Ubicacion del Enlace', bold)
    worksheet.write('D1', 'Backlink', bold)
    worksheet.write('E1', 'Es Nofollow', bold)
    worksheet.write('F1', 'Tiene Foro', bold)

    row = 1
    col = 0

    data = Backlinks.objects.all()

    for d in data:
        url_from = d.url_from
        idioma = d.language
        ubicacion = d.site_link
        backlink = d.url_to
        nofollow = d.nofollow
        foro = d.foro

        if nofollow == 0:
            nofollow = 'nofollow'
        else:
            nofollow = 'follow'

        if foro == 0:
            foro = 'No'
        else:
            foro = 'Sí'


        worksheet.write(row, col, url_from)
        worksheet.write(row, col + 1, idioma)
        worksheet.write(row, col + 2, ubicacion)
        worksheet.write(row, col + 3, backlink)
        worksheet.write(row, col + 4, nofollow)
        worksheet.write(row, col + 5, foro)
        row += 1

    workbook.close()

    return redirect('results')


@login_required
def foros(request):
    bk_link = Backlinks.objects.all()

    for url_ in bk_link:
        web_url = url_.url_from
        pk = url_.pk
        response = requests.get(web_url, headers=USER_AGENT).content
        #sauce = urllib.request.urlopen(web_url).read()
        soup = BeautifulSoup(response,'lxml')

        section = soup.section
        foro = re.compile('foru[a-z]+')
        foro_num = 0

        for lelo in soup.find_all('a'):
            try:
                joinURL = urljoin(web_url,lelo.get('href'))
                parseURL = urlparse(joinURL)
                parseURL = parseURL.netloc
                searchURL = re.search(parseURL, joinURL)
                if searchURL:
                    foro_num += 1
                    print(joinURL)
                else:
                    pass
            except:
                print('no se puede acceder a ' + joinURL)

        if foro_num > 0:
            bk_link = Backlinks.objects.get(pk=pk)
            bk_link.site_link = 'Foro'
            bk_link.save()

    return redirect('excel')

@login_required
def google(request):
    print(request.session['session_token'])
    session = request.session['session_token']
    csv = CSV_import.objects.filter(session_id__exact = session ).delete()
    google = GoogleBD.objects.filter(session_id__exact = session ).delete()
    googleKey = GoogleSearch.objects.filter(session_id__exact = session ).delete()
    googleSingle = SingleAhref.objects.filter(session_id__exact = session ).delete()
    url = UrlSearch.objects.filter(session_id__exact = session ).delete()
    bk = Backlinks.objects.filter(session_id__exact = session ).delete()

    if request.method == 'POST':
        form = GoogleForm(request.POST)
        form.save()
        return redirect('google_search')

    form = GoogleForm()
    context = {'form': form, 'session_id': session}

    return render(request, 'ahrefs/google/google.html', context)

@login_required
def google_search(request):
    google_url = 'https://www.google.com/search?q={}&num={}'
    keyword = GoogleSearch.objects.all()
    session_id = request.session['session_token']

    redes = ['wikipedia', 'facebook', 'twitter', 'plus', 'youtube', 'linkedin', 'mercadolibre', 'amazon', 'google', 'instagram', 'pinterest']


    for key in keyword:
        pk = key.pk
        cant = key.cant
        search = google_url.format(key, cant)
        response = requests.get(search, headers=USER_AGENT)
        response.raise_for_status()
        content = response.content

        soup = BeautifulSoup(content, 'html.parser')
        result = soup.find_all('div', attrs={'class': 'rc'})

        for r in result:
            link = r.find('a', href=True)
            title = r.find('h3', attrs={'class': 'r'})
            description = r.find('span', attrs={'class': 'st'})

            if link:
                link = link['href']

            domain = urlparse(link)
            domain = domain.netloc

            google = GoogleBD.objects.create(
                keyword = key,
                url = link,
                domain = domain,
                session_id = session_id
            )
            google.save()

    search = GoogleBD.objects.all()

    for row in search:
        if search.filter(domain=row.domain).count() > 1:
            row.delete()

    for s in search:
        dm = s.domain
        for r in redes:
            if r in dm:
                peco = s.pk
                if peco is None:
                    print('mamalo chino')
                else:
                    lola = search.get(pk=peco)
                    lola.delete()
            else:
                pass

    return redirect('google_results')

@login_required
def google_results(request):
    google = GoogleBD.objects.all()
    context = {'google': google}
    return render(request, 'ahrefs/google/google_results.html', context)

@login_required
def bk_google_all(request):
    search_token = TokenAhref.objects.get(pk=1)
    #token = 'ef2fdefde20c70af3ad0ccd6352d1bedda36a5e1'
    token = search_token.token
    url_ahref = 'http://apiv2.ahrefs.com?from=backlinks&target={}&mode=domain&order_by=ahrefs_rank%3Adesc&output=json&token={}'
    google = GoogleBD.objects.all()
    collect_data = []

    for el in google:
        domain = el.domain
        response = requests.get(url_ahref.format(domain, token)).json()
        print(response)

        number_response = len(response['refpages'])
        i = 0

        while i < number_response:
            backlink_info = {
                'url_from': response['refpages'][i]['url_from'],
                'title': response['refpages'][i]['title'],
                'url_to': response['refpages'][i]['url_to'],
                'language': response['refpages'][i]['language'],
                'anchor': response['refpages'][i]['anchor'],
                'nofollow': response['refpages'][i]['nofollow']
            }
            bk = Google_bk_single.objects.create(
                url_from = backlink_info['url_from'],
                title = backlink_info['title'],
                url_to = backlink_info['url_to'],
                language = backlink_info['language'],
                anchor = backlink_info['anchor'],
                nofollow = backlink_info['nofollow'],
                site_link = 'Articulo',
            )
            bk.save()
            i += 1

        links = Google_bk_single.objects.all()
        lenght = len(links)
        div = int(lenght / 25)
        p = 0

        collect = []
        while p < lenght:
            if p == 0:
                a = links[:div]
                collect.append(a)
            else:
                h = div + p
                a = links[p:h]
                collect.append(a)
            p += div

        print(links)
        t1= threading.Thread(target=ah.scrapper_0, args=(collect[0], links))
        t2= threading.Thread(target=ah.scrapper_1, args=(collect[1], links))
        t3= threading.Thread(target=ah.scrapper_2, args=(collect[2], links))
        t4= threading.Thread(target=ah.scrapper_3, args=(collect[3], links))
        t5= threading.Thread(target=ah.scrapper_4, args=(collect[4], links))
        t6= threading.Thread(target=ah.scrapper_5, args=(collect[5], links))
        t7= threading.Thread(target=ah.scrapper_6, args=(collect[6], links))
        t8= threading.Thread(target=ah.scrapper_7, args=(collect[7], links))
        t9= threading.Thread(target=ah.scrapper_8, args=(collect[8], links))
        t10= threading.Thread(target=ah.scrapper_9, args=(collect[9], links))
        t11= threading.Thread(target=ah.scrapper_10, args=(collect[10], links))
        t12= threading.Thread(target=ah.scrapper_11, args=(collect[11], links))
        t13= threading.Thread(target=ah.scrapper_12, args=(collect[12], links))
        t14= threading.Thread(target=ah.scrapper_13, args=(collect[13], links))
        t15= threading.Thread(target=ah.scrapper_14, args=(collect[14], links))
        t16= threading.Thread(target=ah.scrapper_15, args=(collect[15], links))
        t17= threading.Thread(target=ah.scrapper_16, args=(collect[16], links))
        t18= threading.Thread(target=ah.scrapper_17, args=(collect[17], links))
        t19= threading.Thread(target=ah.scrapper_18, args=(collect[18], links))
        t20= threading.Thread(target=ah.scrapper_19, args=(collect[19], links))
        t21= threading.Thread(target=ah.scrapper_20, args=(collect[20], links))
        t22= threading.Thread(target=ah.scrapper_21, args=(collect[21], links))
        t23= threading.Thread(target=ah.scrapper_22, args=(collect[22], links))
        t24= threading.Thread(target=ah.scrapper_23, args=(collect[23], links))
        t25= threading.Thread(target=ah.scrapper_24, args=(collect[24], links))


        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t5.start()
        t6.start()
        t7.start()
        t8.start()
        t9.start()
        t10.start()
        t11.start()
        t12.start()
        t13.start()
        t14.start()
        t15.start()
        t16.start()
        t17.start()
        t18.start()
        t19.start()
        t20.start()
        t21.start()
        t22.start()
        t23.start()
        t24.start()
        t25.start()

        t1.join()
        t2.join()
        t3.join()
        t4.join()
        t5.join()
        t6.join()
        t7.join()
        t8.join()
        t9.join()
        t10.join()
        t11.join()
        t12.join()
        t13.join()
        t14.join()
        t15.join()
        t16.join()
        t17.join()
        t18.join()
        t19.join()
        t20.join()
        t20.join()
        t21.join()
        t22.join()
        t23.join()
        t24.join()
        t25.join()


        context = {'collect_data': links }

    return render(request, 'ahrefs/google/bk_google_all.html')

@login_required
def g_single(request, pk):
    search_token = TokenAhref.objects.get(pk=1)
    #token = 'ef2fdefde20c70af3ad0ccd6352d1bedda36a5e1'
    token = search_token.token
    url_ahref = 'http://apiv2.ahrefs.com?from=backlinks&target={}&limit=200&mode=domain&order_by=ahrefs_rank%3Adesc&output=json&token={}'
    el = GoogleBD.objects.get(pk=pk)
    domain = el.domain

    response = requests.get(url_ahref.format(domain, token)).json()
    print(response)

    number_response = len(response['refpages'])

    i = 0

    collect_data = []

    while i < number_response:
        backlink_info = {
            'url_from': response['refpages'][i]['url_from'],
            'title': response['refpages'][i]['title'],
            'url_to': response['refpages'][i]['url_to'],
            'language': response['refpages'][i]['language'],
            'anchor': response['refpages'][i]['anchor'],
            'nofollow': response['refpages'][i]['nofollow']
        }
        bk = Google_bk_single.objects.create(
            url_from = backlink_info['url_from'],
            title = backlink_info['title'],
            url_to = backlink_info['url_to'],
            language = backlink_info['language'],
            anchor = backlink_info['anchor'],
            nofollow = backlink_info['nofollow'],
            site_link = 'Articulo',
        )
        bk.save()
        i += 1

    links = Google_bk_single.objects.all()
    number_links = len(links)
    p = 0

    for l in links:
        leng = l.language
        pk = l.pk
        url = l.url_from
        to_url = l.url_to
        s_ = 0

        if 'forum' in url or 'foro' in url:
            l.foro = True
            l.save()
        else:
            pass

        if leng != 'en' and leng != 'es':
            erase = Google_bk_single.objects.get(pk=pk).delete()
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
                eraseTwo = Google_bk_single.objects.get(pk=pk).delete()

        if s_ > 0:
            l.site_link = 'Comentario'
            l.save()

    context = {'collect_data': links }
    return redirect('foro')



# Upload File or CSV
import csv
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import ahrefs.process_upload_csv as process

@login_required
def upload_file(request):
    session_id = request.session['session_token']
    if request.method == 'POST' and request.FILES['csv_file']:
        myfile = request.FILES['csv_file']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)

        results = []
        with open(uploaded_file_url) as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',')
            for row in reader:
                results.append(row)

        magic = []
        for r in results:
            url = r['Referring Page URL']
            domain = urlparse(url)
            domain = domain.netloc
            extends = {
                'url': url,
                'lang': r['Language'],
                'url_to': r['Link URL'],
                'domain': domain,
            }
            magic.append(extends)

        lenght = len(magic)
        div = int(lenght / 20)
        print(len(magic))
        print(div)

        p = 0

        collect = []
        while p < lenght:
            if p == 0:
                a = magic[:div]
                collect.append(a)
            else:
                h = div + p
                a = magic[p:h]
                collect.append(a)
            p += div

        t = time.time()

        t1= threading.Thread(target=process.upload_0, args=(collect[0], uploaded_file_url, session_id,))
        t2= threading.Thread(target=process.upload_1, args=(collect[1], uploaded_file_url, session_id,))
        t3= threading.Thread(target=process.upload_2, args=(collect[2], uploaded_file_url, session_id,))
        t4= threading.Thread(target=process.upload_3, args=(collect[3], uploaded_file_url, session_id,))
        t5= threading.Thread(target=process.upload_4, args=(collect[4], uploaded_file_url, session_id,))
        t6= threading.Thread(target=process.upload_5, args=(collect[5], uploaded_file_url, session_id,))
        t7= threading.Thread(target=process.upload_6, args=(collect[6], uploaded_file_url, session_id,))
        t8= threading.Thread(target=process.upload_7, args=(collect[7], uploaded_file_url, session_id,))
        t9= threading.Thread(target=process.upload_8, args=(collect[8], uploaded_file_url, session_id,))
        t10= threading.Thread(target=process.upload_9, args=(collect[9], uploaded_file_url, session_id,))
        t11= threading.Thread(target=process.upload_10, args=(collect[10], uploaded_file_url, session_id,))
        t12= threading.Thread(target=process.upload_11, args=(collect[11], uploaded_file_url, session_id,))
        t13= threading.Thread(target=process.upload_12, args=(collect[12], uploaded_file_url, session_id,))
        t14= threading.Thread(target=process.upload_13, args=(collect[13], uploaded_file_url, session_id,))
        t15= threading.Thread(target=process.upload_14, args=(collect[14], uploaded_file_url, session_id,))
        t16= threading.Thread(target=process.upload_15, args=(collect[15], uploaded_file_url, session_id,))
        t17= threading.Thread(target=process.upload_16, args=(collect[16], uploaded_file_url, session_id,))
        t18= threading.Thread(target=process.upload_17, args=(collect[17], uploaded_file_url, session_id,))
        t19= threading.Thread(target=process.upload_18, args=(collect[18], uploaded_file_url, session_id,))
        t20= threading.Thread(target=process.upload_19, args=(collect[19], uploaded_file_url, session_id,))

        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t5.start()
        t6.start()
        t7.start()
        t8.start()
        t9.start()
        t10.start()
        t11.start()
        t12.start()
        t13.start()
        t14.start()
        t15.start()
        t16.start()
        t17.start()
        t18.start()
        t19.start()
        t20.start()

        t1.join()
        t2.join()
        t3.join()
        t4.join()
        t5.join()
        t6.join()
        t7.join()
        t8.join()
        t9.join()
        t10.join()
        t11.join()
        t12.join()
        t13.join()
        t14.join()
        t15.join()
        t16.join()
        t17.join()
        t18.join()
        t19.join()
        t20.join()

        print("done in : ",time.time()-t)

        for row in CSV_import.objects.all():
            if CSV_import.objects.filter(domain=row.domain).count() > 1:
                row.delete()

        return render(request, 'ahrefs/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return redirect('index')

################################## MultiThread #####################################
import threading
import time
import ahrefs.scrapper_csv as scr



####################################################################################

@login_required
def search_csv(request):
    search = CSV_import.objects.all()
    lenght = len(search)
    div = int(lenght / 100)

    p = 0

    collect = []
    while p < lenght:
        if p == 0:
            a = search[:div]
            collect.append(a)
        else:
            h = div + p
            a = search[p:h]
            collect.append(a)
        p += div

    t = time.time()

    t1= threading.Thread(target=scr.scrapper_0, args=(collect[0], search,))
    t2= threading.Thread(target=scr.scrapper_1, args=(collect[1], search,))
    t3= threading.Thread(target=scr.scrapper_2, args=(collect[2], search,))
    t4= threading.Thread(target=scr.scrapper_3, args=(collect[3], search,))
    t5= threading.Thread(target=scr.scrapper_4, args=(collect[4], search,))
    t6= threading.Thread(target=scr.scrapper_5, args=(collect[5],))
    t7= threading.Thread(target=scr.scrapper_6, args=(collect[6],))
    t8= threading.Thread(target=scr.scrapper_7, args=(collect[7],))
    t9= threading.Thread(target=scr.scrapper_8, args=(collect[8],))
    t10= threading.Thread(target=scr.scrapper_9, args=(collect[9],))
    t11= threading.Thread(target=scr.scrapper_10, args=(collect[10],))
    t12= threading.Thread(target=scr.scrapper_11, args=(collect[11],))
    t13= threading.Thread(target=scr.scrapper_12, args=(collect[12],))
    t14= threading.Thread(target=scr.scrapper_13, args=(collect[13],))
    t15= threading.Thread(target=scr.scrapper_14, args=(collect[14],))
    t16= threading.Thread(target=scr.scrapper_15, args=(collect[15],))
    t17= threading.Thread(target=scr.scrapper_16, args=(collect[16],))
    t18= threading.Thread(target=scr.scrapper_17, args=(collect[17],))
    t19= threading.Thread(target=scr.scrapper_18, args=(collect[18],))
    t20= threading.Thread(target=scr.scrapper_19, args=(collect[19],))
    t21= threading.Thread(target=scr.scrapper_20, args=(collect[20],))
    t22= threading.Thread(target=scr.scrapper_21, args=(collect[21],))
    t23= threading.Thread(target=scr.scrapper_22, args=(collect[22],))
    t24= threading.Thread(target=scr.scrapper_23, args=(collect[23],))
    t25= threading.Thread(target=scr.scrapper_24, args=(collect[24],))
    t26= threading.Thread(target=scr.scrapper_25, args=(collect[25],))
    t27= threading.Thread(target=scr.scrapper_26, args=(collect[26],))
    t28= threading.Thread(target=scr.scrapper_27, args=(collect[27],))
    t29= threading.Thread(target=scr.scrapper_28, args=(collect[28],))
    t30= threading.Thread(target=scr.scrapper_29, args=(collect[29],))
    t31= threading.Thread(target=scr.scrapper_30, args=(collect[30],))
    t32= threading.Thread(target=scr.scrapper_31, args=(collect[31],))
    t33= threading.Thread(target=scr.scrapper_32, args=(collect[32],))
    t34= threading.Thread(target=scr.scrapper_33, args=(collect[33],))
    t35= threading.Thread(target=scr.scrapper_34, args=(collect[34],))
    t36= threading.Thread(target=scr.scrapper_35, args=(collect[35],))
    t37= threading.Thread(target=scr.scrapper_36, args=(collect[36],))
    t38= threading.Thread(target=scr.scrapper_37, args=(collect[37],))
    t39= threading.Thread(target=scr.scrapper_38, args=(collect[38],))
    t40= threading.Thread(target=scr.scrapper_39, args=(collect[39],))
    t41= threading.Thread(target=scr.scrapper_40, args=(collect[40],))
    t42= threading.Thread(target=scr.scrapper_41, args=(collect[41],))
    t43= threading.Thread(target=scr.scrapper_42, args=(collect[42],))
    t44= threading.Thread(target=scr.scrapper_43, args=(collect[43],))
    t45= threading.Thread(target=scr.scrapper_44, args=(collect[44],))
    t46= threading.Thread(target=scr.scrapper_45, args=(collect[45],))
    t47= threading.Thread(target=scr.scrapper_46, args=(collect[46],))
    t48= threading.Thread(target=scr.scrapper_47, args=(collect[47],))
    t49= threading.Thread(target=scr.scrapper_48, args=(collect[48],))
    t50= threading.Thread(target=scr.scrapper_49, args=(collect[49],))
    t51= threading.Thread(target=scr.scrapper_50, args=(collect[50],))
    t52= threading.Thread(target=scr.scrapper_51, args=(collect[51],))
    t53= threading.Thread(target=scr.scrapper_52, args=(collect[52],))
    t54= threading.Thread(target=scr.scrapper_53, args=(collect[53],))
    t55= threading.Thread(target=scr.scrapper_54, args=(collect[54],))
    t56= threading.Thread(target=scr.scrapper_55, args=(collect[55],))
    t57= threading.Thread(target=scr.scrapper_56, args=(collect[56],))
    t58= threading.Thread(target=scr.scrapper_57, args=(collect[57],))
    t59= threading.Thread(target=scr.scrapper_58, args=(collect[58],))
    t60= threading.Thread(target=scr.scrapper_59, args=(collect[59],))
    t61= threading.Thread(target=scr.scrapper_60, args=(collect[60],))
    t62= threading.Thread(target=scr.scrapper_61, args=(collect[61],))
    t63= threading.Thread(target=scr.scrapper_62, args=(collect[62],))
    t64= threading.Thread(target=scr.scrapper_63, args=(collect[63],))
    t65= threading.Thread(target=scr.scrapper_64, args=(collect[64],))
    t66= threading.Thread(target=scr.scrapper_65, args=(collect[65],))
    t67= threading.Thread(target=scr.scrapper_66, args=(collect[66],))
    t68= threading.Thread(target=scr.scrapper_67, args=(collect[67],))
    t69= threading.Thread(target=scr.scrapper_68, args=(collect[68],))
    t70= threading.Thread(target=scr.scrapper_69, args=(collect[69],))
    t71= threading.Thread(target=scr.scrapper_70, args=(collect[70],))
    t72= threading.Thread(target=scr.scrapper_71, args=(collect[71],))
    t73= threading.Thread(target=scr.scrapper_72, args=(collect[72],))
    t74= threading.Thread(target=scr.scrapper_73, args=(collect[73],))
    t75= threading.Thread(target=scr.scrapper_74, args=(collect[74],))
    t76= threading.Thread(target=scr.scrapper_75, args=(collect[75],))
    t77= threading.Thread(target=scr.scrapper_76, args=(collect[76],))
    t78= threading.Thread(target=scr.scrapper_77, args=(collect[77],))
    t79= threading.Thread(target=scr.scrapper_78, args=(collect[78],))
    t80= threading.Thread(target=scr.scrapper_79, args=(collect[79],))
    t81= threading.Thread(target=scr.scrapper_80, args=(collect[80],))
    t82= threading.Thread(target=scr.scrapper_81, args=(collect[81],))
    t83= threading.Thread(target=scr.scrapper_82, args=(collect[82],))
    t84= threading.Thread(target=scr.scrapper_83, args=(collect[83],))
    t85= threading.Thread(target=scr.scrapper_84, args=(collect[84],))
    t86= threading.Thread(target=scr.scrapper_85, args=(collect[85],))
    t87= threading.Thread(target=scr.scrapper_86, args=(collect[86],))
    t88= threading.Thread(target=scr.scrapper_87, args=(collect[87],))
    t89= threading.Thread(target=scr.scrapper_88, args=(collect[88],))
    t90= threading.Thread(target=scr.scrapper_89, args=(collect[89],))
    t91= threading.Thread(target=scr.scrapper_90, args=(collect[90],))
    t92= threading.Thread(target=scr.scrapper_91, args=(collect[91],))
    t93= threading.Thread(target=scr.scrapper_92, args=(collect[92],))
    t94= threading.Thread(target=scr.scrapper_93, args=(collect[93],))
    t95= threading.Thread(target=scr.scrapper_94, args=(collect[94],))
    t96= threading.Thread(target=scr.scrapper_95, args=(collect[95],))
    t97= threading.Thread(target=scr.scrapper_96, args=(collect[96],))
    t98= threading.Thread(target=scr.scrapper_97, args=(collect[97],))
    t99= threading.Thread(target=scr.scrapper_98, args=(collect[98],))
    t100= threading.Thread(target=scr.scrapper_99, args=(collect[99],))




    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()
    t8.start()
    t9.start()
    t10.start()
    t11.start()
    t12.start()
    t13.start()
    t14.start()
    t15.start()
    t16.start()
    t17.start()
    t18.start()
    t19.start()
    t20.start()
    t21.start()
    t22.start()
    t23.start()
    t24.start()
    t25.start()
    t26.start()
    t27.start()
    t28.start()
    t29.start()
    t30.start()
    t31.start()
    t32.start()
    t33.start()
    t34.start()
    t35.start()
    t36.start()
    t37.start()
    t38.start()
    t39.start()
    t40.start()
    t41.start()
    t42.start()
    t43.start()
    t44.start()
    t45.start()
    t46.start()
    t47.start()
    t48.start()
    t49.start()
    t50.start()
    t51.start()
    t52.start()
    t53.start()
    t54.start()
    t55.start()
    t56.start()
    t57.start()
    t58.start()
    t59.start()
    t60.start()
    t61.start()
    t62.start()
    t63.start()
    t64.start()
    t65.start()
    t66.start()
    t67.start()
    t68.start()
    t69.start()
    t70.start()
    t71.start()
    t72.start()
    t73.start()
    t74.start()
    t75.start()
    t76.start()
    t77.start()
    t78.start()
    t79.start()
    t80.start()
    t81.start()
    t82.start()
    t83.start()
    t84.start()
    t85.start()
    t86.start()
    t87.start()
    t88.start()
    t89.start()
    t90.start()
    t91.start()
    t92.start()
    t93.start()
    t94.start()
    t95.start()
    t96.start()
    t97.start()
    t98.start()
    t99.start()
    t100.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()
    t7.join()
    t8.join()
    t9.join()
    t10.join()
    t11.join()
    t12.join()
    t13.join()
    t14.join()
    t15.join()
    t16.join()
    t17.join()
    t18.join()
    t19.join()
    t20.join()
    t20.join()
    t21.join()
    t22.join()
    t23.join()
    t24.join()
    t25.join()
    t26.join()
    t27.join()
    t28.join()
    t29.join()
    t30.join()
    t31.join()
    t32.join()
    t33.join()
    t34.join()
    t35.join()
    t36.join()
    t37.join()
    t38.join()
    t39.join()
    t40.join()
    t41.join()
    t42.join()
    t43.join()
    t44.join()
    t45.join()
    t46.join()
    t47.join()
    t48.join()
    t49.join()
    t50.join()
    t51.join()
    t52.join()
    t53.join()
    t54.join()
    t55.join()
    t56.join()
    t57.join()
    t58.join()
    t59.join()
    t60.join()
    t61.join()
    t62.join()
    t63.join()
    t64.join()
    t65.join()
    t66.join()
    t67.join()
    t68.join()
    t69.join()
    t70.join()
    t71.join()
    t72.join()
    t73.join()
    t74.join()
    t75.join()
    t76.join()
    t77.join()
    t78.join()
    t79.join()
    t80.join()
    t81.join()
    t82.join()
    t83.join()
    t84.join()
    t85.join()
    t86.join()
    t87.join()
    t88.join()
    t89.join()
    t90.join()
    t91.join()
    t92.join()
    t93.join()
    t94.join()
    t95.join()
    t96.join()
    t97.join()
    t98.join()
    t99.join()
    t100.join()

    print("done in : ",time.time()-t)

    return redirect('CSV_export_excel')

@login_required
def CSV_export_excel(request):
    workbook = xlsxwriter.Workbook('ahrefs/static/ahrefs/download/CSV_export.xlsx')
    worksheet = workbook.add_worksheet()
    bold = workbook.add_format({'bold': True})

    worksheet.write('A1', 'Dominio', bold)
    worksheet.write('B1', 'Documento', bold)
    worksheet.write('C1', 'Idioma', bold)
    worksheet.write('D1', 'URL', bold)
    worksheet.write('E1', 'Backlink', bold)
    worksheet.write('F1', 'Ubicacion del Enlace', bold)
    worksheet.write('G1', 'Nofollow', bold)
    worksheet.write('H1', 'Foro', bold)

    row = 1
    col = 0

    data = CSV_import.objects.all()

    for d in data:
        backlink = d.backlink
        document = d.document
        idioma = d.language
        ubicacion = d.site_link
        url_to = d.url_to
        nofollow = d.nofollow
        foro = d.foro
        domain = d.domain

        if nofollow == 0:
            nofollow = 'nofollow'
        else:
            nofollow = 'follow'

        if foro == 0:
            foro = 'No'
        else:
            foro = 'Sí'


        worksheet.write(row, col, domain)
        worksheet.write(row, col + 1, document)
        worksheet.write(row, col + 2, idioma)
        worksheet.write(row, col + 3, backlink)
        worksheet.write(row, col + 4, url_to)
        worksheet.write(row, col + 5, ubicacion)
        worksheet.write(row, col + 6, nofollow)
        worksheet.write(row, col + 7, foro)
        row += 1

    workbook.close()

    return redirect('result_csv')

@login_required
def result_csv(request):
    bk_link = CSV_import.objects.all()
    total = len(bk_link)
    collect_data= []
    bk_filter = CSVFilter(request.GET, queryset=bk_link)

    for bk in bk_link:
        collect_data.append(bk)

    context = {'collect_data': collect_data, 'total': total, 'filter':bk_filter}

    return render(request, 'ahrefs/result_csv.html', context)


## Single Ahrefs
@login_required
def single_ahrefs(request):
    search_token = TokenAhref.objects.get(pk=1)
    #token = 'ef2fdefde20c70af3ad0ccd6352d1bedda36a5e1'
    token = search_token.token
    url_ahref = 'http://apiv2.ahrefs.com?from=linked_domains&target={}&mode=domain&output=json&token={}'

    bk = SingleAhref.objects.all()
    collect_data = []

    for b in bk:
        url = b.url
        response = requests.get(url_ahref.format(url, token)).json()
        print(response)
        number_response = len(response['refpages'])
        i = 0

        while i < number_response:
            backlink_info = {
                'url_from': response['refpages'][i]['url_from'],
                'title': response['refpages'][i]['title'],
                'url_to': response['refpages'][i]['url_to'],
                'language': response['refpages'][i]['language'],
                'anchor': response['refpages'][i]['anchor'],
                'nofollow': response['refpages'][i]['nofollow']
            }
            bk = SingleBacklinks.objects.create(
                url_from = backlink_info['url_from'],
                title = backlink_info['title'],
                url_to = backlink_info['url_to'],
                language = backlink_info['language'],
                anchor = backlink_info['anchor'],
                nofollow = backlink_info['nofollow'],
                site_link = 'Articulo',
            )
            bk.save()
            i += 1

        links = SingleBacklinks.objects.all()

        number_links = len(links)

        p = 0

        for l in links:
            leng = l.language
            url = l.url_from
            to_url = l.url_to
            pk = l.pk
            s_ = 0

            if 'forum' in url or 'foro' in url:
                l.foro = True
                l.save()
            else:
                pass


            if leng != 'en' and leng != 'es' and leng != ' ':
                erase = SingleBacklinks.objects.get(pk=pk).delete()
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
                    eraseTwo = SingleBacklinks.objects.get(pk=pk).delete()

            if s_ > 0:
                l.site_link = 'Comentario'
                l.save()

        context = {'collect_data': links }
        return redirect('foro')



## DELETE Section
@login_required
def delete_google(request):
    try:
        bk = GoogleBD.objects.all()
        gl = GoogleSearch.objects.all()
        bk.delete()
        gl.delete()
    except Backlinks.DoesNotExist:
        raise Http404("No MyModel matches the given query.")

    return redirect('google')


@login_required
def delete_backlinks(request):
    session_id = request.session['session_token']
    try:
        bk = Backlinks.objects.filter(session_id = session_id)
        bk.delete()
    except Backlinks.DoesNotExist:
        raise Http404("No MyModel matches the given query.")

    return redirect('search_bk')

@login_required
def delete_csv(request):
    try:
        bk = CSV_import.objects.all()
        bk.delete()
    except Backlinks.DoesNotExist:
        raise Http404("No MyModel matches the given query.")

    return redirect('search_bk')
