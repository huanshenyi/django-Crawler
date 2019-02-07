from django.shortcuts import render
from django.http import HttpResponse
import requests as rt
from lxml import etree
import re
from datetime import datetime
from django.views.decorators import csrf

def index(request):
    url = 'https://paiza.jp/career/job_offers'
    respons = rt.get(url)
    text = respons.text
    html = etree.HTML(text)
    count = html.xpath("//span[@class='total_count']/text()")[0]

    """python求人数"""
    url_python = 'https://paiza.jp/career/job_offers/dev_language/Python3'
    respons_python = rt.get(url_python)
    text_python = respons_python.text
    html_python = etree.HTML(text_python)
    count_python = html_python.xpath("//span[@class='total_count']/text()")[0]
    """php求人数"""
    url_php = 'https://paiza.jp/career/job_offers/dev_language/PHP'
    respons_php = rt.get(url_php)
    text_php = respons_php.text
    html_php = etree.HTML(text_php)
    count_php = html_php.xpath("//span[@class='total_count']/text()")[0]
    """ruby"""
    url_ruby = 'https://paiza.jp/career/job_offers/dev_language/Ruby'
    respons_ruby = rt.get(url_ruby)
    text_ruby = respons_ruby.text
    html_ruby = etree.HTML(text_ruby)
    count_ruby = html_ruby.xpath("//span[@class='total_count']/text()")[0]
    """Go言語"""
    url_go = 'https://paiza.jp/career/job_offers/dev_language/Go言語'
    respons_go = rt.get(url_go)
    text_go = respons_go.text
    html_go = etree.HTML(text_go)
    count_go = html_go.xpath("//span[@class='total_count']/text()")[0]

    nowtime = datetime.now()
    return render(request, 'index.html',context={'count': count, 'nowtime': nowtime, 'count_python': count_python,'count_php': count_php,'count_ruby':count_ruby,'count_go':count_go})

def language(request,key_word):
    lists=[]
    url = 'https://paiza.jp/career/job_offers/dev_language/'+key_word
    respons = rt.get(url)
    text = respons.text
    html = etree.HTML(text)
    jobs = html.xpath("//a[@class='c-job_offer-box__header__title__link']/h3[@class='c-job_offer-box__header__title']/text()")
    jobs = list(map(lambda x: re.sub('\s', '', x), jobs))

    jobs = list(filter(None, jobs))
    companys = html.xpath("//h4[@class='c-job_offer-recruiter__name']/a/text()")
    contents = html.xpath("//dl[@class ='c-job_offer-summary']/dd/text()")
    contents = list(map(lambda x: re.sub('\s', '', x), contents))
    contents = list(filter(None,contents))
    offices = html.xpath("//table[@class='c-job_offer-detail']//tr[2]/td[@class='c-job_offer-detail__description']/text()")
    requests_q = html.xpath("//p[@class='mb0']")
    xlists = list(map(lambda x: x.xpath('string(.)'), requests_q))
    xlists = list(map(lambda x: re.sub('\s', '', x), xlists))
    # requests_x=[x for x in requests_q if x!= '以下すべてのご経験をお持ちの方からのご応募をおまちしています！']
    moneys = html.xpath("//strong[@class='c-job_offer-detail__salary']/text()")
    imgs = html.xpath("//img[@class='c-job_offer-recruiter__thumbnail']/@src")

    for job, company, content, office, xlist,money,img in zip(jobs, companys, contents, offices, xlists,moneys,imgs):

        lists.append(
           {'job': job.replace('\n', ''), 'company': company, 'content': content, 'office': office, 'xlist': xlist,'money':money,'img':img}
       )

    return render(request, 'language.html', context={'lists': lists, 'key_word': key_word})


def frameworks(request, key_word):
    lists = []
    url = 'https://paiza.jp/career/job_offers/dev_frameworks/' + key_word
    respons = rt.get(url)
    text = respons.text
    html = etree.HTML(text)
    jobs = html.xpath(
        "//a[@class='c-job_offer-box__header__title__link']/h3[@class='c-job_offer-box__header__title']/text()")
    jobs = list(map(lambda x: re.sub('\s', '', x), jobs))
    jobs = list(filter(None, jobs))
    companys = html.xpath("//h4[@class='c-job_offer-recruiter__name']/a/text()")
    contents = html.xpath("//dl[@class ='c-job_offer-summary']/dd/text()")
    contents = list(map(lambda x: re.sub('\s', '', x), contents))
    offices = html.xpath(
        "//table[@class='c-job_offer-detail']//tr[2]/td[@class='c-job_offer-detail__description']/text()")
    requests_q = html.xpath("//p[@class='mb0']")
    xlists = list(map(lambda x: x.xpath('string(.)'), requests_q))
    xlists = list(map(lambda x: re.sub('\s', '', x), xlists))
    # requests_x=[x for x in requests_q if x!= '以下すべてのご経験をお持ちの方からのご応募をおまちしています！']
    moneys = html.xpath("//strong[@class='c-job_offer-detail__salary']/text()")
    imgs = html.xpath("//img[@class='c-job_offer-recruiter__thumbnail']/@src")

    for job, company, content, office, xlist, money, img in zip(jobs, companys, contents, offices, xlists, moneys,
                                                                imgs):
        lists.append(
            {'job': job.replace('\n', ''), 'company': company, 'content': content, 'office': office, 'xlist': xlist,
             'money': money, 'img': img}
        )
    return render(request, 'frameworks.html', context={'lists': lists, 'key_word': key_word})

def occupation(request, key_word):
    lists = []
    url = 'https://paiza.jp/career/job_offers/occupation/' + key_word
    respons = rt.get(url)
    text = respons.text
    html = etree.HTML(text)
    jobs = html.xpath(
        "//a[@class='c-job_offer-box__header__title__link']/h3[@class='c-job_offer-box__header__title']/text()")
    jobs = list(map(lambda x: re.sub('\s', '', x), jobs))
    jobs = list(filter(None, jobs))
    companys = html.xpath("//h4[@class='c-job_offer-recruiter__name']/a/text()")
    contents = html.xpath("//dl[@class ='c-job_offer-summary']/dd/text()")
    contents = list(map(lambda x: re.sub('\s', '', x), contents))
    offices = html.xpath(
        "//table[@class='c-job_offer-detail']//tr[2]/td[@class='c-job_offer-detail__description']/text()")
    requests_q = html.xpath("//p[@class='mb0']")
    xlists = list(map(lambda x: x.xpath('string(.)'), requests_q))
    xlists = list(map(lambda x: re.sub('\s', '', x), xlists))
    moneys = html.xpath("//strong[@class='c-job_offer-detail__salary']/text()")
    imgs = html.xpath("//img[@class='c-job_offer-recruiter__thumbnail']/@src")

    for job, company, content, office, xlist, money, img in zip(jobs, companys, contents, offices, xlists, moneys,
                                                                imgs):
        lists.append(
            {'job': job.replace('\n', ''), 'company': company, 'content': content, 'office': office, 'xlist': xlist,
             'money': money, 'img': img}
        )
    return render(request, 'language.html', context={'lists': lists,'key_word': key_word})

def companys(request):
    lists = []
    if request.method == 'POST':
        key_word = request.POST.get('key_word')
        url="https://paiza.jp/career/search/?utf8=%E2%9C%93&c%5Brecruiter_name%5D={}&commit=検索".format(key_word)
        respons = rt.get(url)
        text = respons.text
        html = etree.HTML(text)
        jobs = html.xpath(
            "//a[@class='c-job_offer-box__header__title__link']/h3[@class='c-job_offer-box__header__title']/text()")
        jobs = list(map(lambda x: re.sub('\s', '', x), jobs))
        jobs = list(filter(None, jobs))
        companys = html.xpath("//h4[@class='c-job_offer-recruiter__name']/a/text()")
        contents = html.xpath("//dl[@class ='c-job_offer-summary']/dd/text()")
        contents = list(map(lambda x: re.sub('\s', '', x), contents))
        offices = html.xpath(
            "//table[@class='c-job_offer-detail']//tr[2]/td[@class='c-job_offer-detail__description']/text()")
        requests_q = html.xpath("//p[@class='mb0']")
        xlists = list(map(lambda x: x.xpath('string(.)'), requests_q))
        xlists = list(map(lambda x: re.sub('\s', '', x), xlists))
        moneys = html.xpath("//strong[@class='c-job_offer-detail__salary']/text()")
        imgs = html.xpath("//img[@class='c-job_offer-recruiter__thumbnail']/@src")

        for job, company, content, office, xlist, money, img in zip(jobs, companys, contents, offices, xlists, moneys,
                                                                    imgs):
            lists.append(
                {'job': job.replace('\n', ''), 'company': company, 'content': content, 'office': office, 'xlist': xlist,
                 'money': money, 'img': img}
            )
        return render(request, 'companys.html', context={'lists': lists, 'key_word': key_word})
    else:
        return HttpResponse('違う')

def reviews(request,key_word):
    lists=[]
    url = 'https://en-hyouban.com/search/?SearchWords='+key_word
    respons = rt.get(url)
    text = respons.text
    html = etree.HTML(text)
    try:
        main_url_pazu = html.xpath("//h2[@class='companyName']/a/@href")[0]
    except BaseException:
       return HttpResponse(

           "<body background='/static/404.jpg' style=background-repeat:no-repeat;background-size:100% 100%;background-attachment:fixed;' >"
       )
    main_url = 'https://en-hyouban.com'+main_url_pazu+'kuchikomi/'
    """詳細ページを取得"""
    respons_main = rt.get(main_url)
    text_main = respons_main.text
    html_main = etree.HTML(text_main)
    """評価してる人"""
    statuss = html_main.xpath("//div[@class='status']/a/text()")
    statuss = list(map(lambda x:re.sub('\s','',x),statuss))
    """コメント"""
    comments = html_main.xpath("//div[@class='comment']")
    comments = list(map(lambda x: x.xpath("string(.)"), comments))
    comments = list(map(lambda x: re.sub('\s*','',x),comments))
    comments = list(map(lambda x: re.sub('\d+代/.+?なった！\d','',x),comments))
    comments = list(map(lambda x: re.sub('転職・就職・採用の口コミ情報','',x),comments))
    # print(comments)
    """年数"""
    years = html_main.xpath("//div[@class='year']/text()")
    """性別"""
    sexs = list(map(lambda x: re.search('(\w+性)',x).group(),statuss))

    """twitterの情報"""
    # twitters= twitter(key_word)
    """会社の詳細情報"""
    url_md_base="https://careerconnection.jp/review/search.html?corpName={}&reportkind=1".format(key_word)
    respons_md_base = rt.get(url_md_base)
    text_md_base = respons_md_base.text
    html_md_base = etree.HTML(text_md_base)
    try:
      url_md = html_md_base.xpath("//ul[@class='result_y']/li/a/@href")[0]
    except BaseException:
       return HttpResponse(
            "<body background='/static/404.jpg' style=background-repeat:no-repeat;background-size:100% 100%;background-attachment:fixed;' >"
       )
    list_md=[]
    response_md = rt.get(url_md)
    text_md = response_md.text
    html_md = etree.HTML(text_md)
    try:
        """売上高"""
        price_heigh = html_md.xpath("//dl[@class='company-performance-area__list']/dd/text()")[0]
        """営業利益"""
        price_sales = html_md.xpath("//dl[@class='company-performance-area__list']/dd/text()")[1]
        """経常利益"""
        price_keijyo = html_md.xpath("//dl[@class='company-performance-area__list']/dd/text()")[2]
        """平均年収"""
        man_price = html_md.xpath("//dd[@class='value-main']/text()")[0]
        """従業員数"""
        man_int = html_md.xpath("//dl[@class='company-performance-area__list']/dd/text()")[4]
        """平均年齢"""
        man_age = html_md.xpath("//dl[@class='company-performance-area__list']/dd/text()")[5]
        """月残業時間"""
        overtime = html_md.xpath("//dl[@class='overview-area__time-list overview-area__time-list1']/dd/strong/text()")[0]
        """月休日出勤"""
        overday = html_md.xpath("//dl[@class='overview-area__time-list overview-area__time-list2']/dd/strong/text()")[0]
        """有給消化率"""
        holiday = html_md.xpath("//dl[@class='overview-area__time-list overview-area__time-list3']/dd/strong/text()")[0]
        # list_md.append(
        #     {'price_heigh':price_heigh,'price_sales':price_sales, 'price_keijyo': price_keijyo, 'man_price': man_price, 'man_int': man_int,'man_age':man_age,'overtime':overtime,'overday':overday,'holiday':holiday}
        # )
        list_md = [price_heigh,price_sales,price_keijyo,man_price,man_int,man_age,overtime,overday,holiday]
    except BaseException:
        list_md = []


    for status, comment, year, sex in zip(statuss,comments,years,sexs):

        lists.append(
            {'status': status, 'comment': comment, 'year': year, 'sex': sex}
        )

    return render(request, 'reviews.html', context={'lists': lists, 'key_word': key_word, 'list_md': list_md})

def twitter(key_word):
    pass

def job_offers(request,key_word):
    lists = []
    url = 'https://paiza.jp/career/job_offers/pf/' + key_word
    respons = rt.get(url)
    text = respons.text
    html = etree.HTML(text)
    jobs = html.xpath(
        "//a[@class='c-job_offer-box__header__title__link']/h3[@class='c-job_offer-box__header__title']/text()")
    jobs = list(map(lambda x: re.sub('\s', '', x), jobs))
    jobs = list(filter(None, jobs))
    companys = html.xpath("//h4[@class='c-job_offer-recruiter__name']/a/text()")
    contents = html.xpath("//dl[@class ='c-job_offer-summary']/dd/text()")
    contents = list(map(lambda x: re.sub('\s', '', x), contents))
    offices = html.xpath(
        "//table[@class='c-job_offer-detail']//tr[2]/td[@class='c-job_offer-detail__description']/text()")
    requests_q = html.xpath("//p[@class='mb0']")
    xlists = list(map(lambda x: x.xpath('string(.)'), requests_q))
    xlists = list(map(lambda x: re.sub('\s', '', x), xlists))
    moneys = html.xpath("//strong[@class='c-job_offer-detail__salary']/text()")
    imgs = html.xpath("//img[@class='c-job_offer-recruiter__thumbnail']/@src")

    for job, company, content, office, xlist, money, img in zip(jobs, companys, contents, offices, xlists, moneys,
                                                                imgs):
        lists.append(
            {'job': job.replace('\n', ''), 'company': company, 'content': content, 'office': office, 'xlist': xlist,
             'money': money, 'img': img}
        )
    return render(request, 'job_offers.html', context={'lists': lists, 'key_word': key_word})

