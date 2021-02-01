import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import re

def create_soup(url):
    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument("widow-size=1920x1080")
    browser = webdriver.Chrome('./webscraping_basic/chromedriver', options=options)
    browser.get(url)
    soup = BeautifulSoup(browser.page_source, 'lxml')
    return soup

def print_news(idx, title, link):
    print('{}. {}'.format(idx+1, title))
    print("  (링크 : {})".format(link))

def scrape_weather():
    url = "https://search.naver.com/search.naver?where=nexearch&sm=top_sug.pre&fbm=0&acr=7&acq=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8&qdt=0&ie=utf8&query=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8"
    soup = create_soup(url)
    weather = soup.find("div", attrs={'class':'info_data'})

    text = weather.find('p', attrs={'class':'cast_txt'}).get_text()
    temp = weather.find("span", attrs={'class':'todaytemp'}).get_text()
    minimum = weather.find('span', attrs={"min"}).get_text()
    maximum = weather.find('span', attrs={"max"}).get_text()

    info = soup.find('li', attrs={'class':'date_info today'})
    am_rainy = info.find('span', attrs={'class':'point_time morning'}).get_text().strip()
    pm_rainy = info.find('span', attrs={'class':'point_time afternoon'}).get_text().strip()

    dust = soup.find("dl", attrs={'class':'indicator'})
    small_dust = dust.find_all('dd')[0].get_text()
    extreme_small_dust = dust.find_all('dd')[1].get_text()

    print("[오늘의 날씨]")
    print(text)
    print(f"현재 {temp}℃ (최저 {minimum} / 최고 {maximum})" )
    print(f"오전 {am_rainy} / 오후 {pm_rainy}")
    print()
    print('미세먼지 {}'.format(small_dust))
    print('초미세먼지 {}'.format(extreme_small_dust))
    print()

def scrape_headline_news():
    print("[헤드라인 뉴스]")
    url = "https://news.naver.com"
    soup = create_soup(url)
    news_list = soup.find('ul', attrs={"class":'hdline_article_list'}).find_all('li', limit=3)
    for idx, news in enumerate(news_list):
        title = news.find('a').get_text().strip()
        link = url + news.find('a')['href']
        print_news(idx, title, link)
    print()

def scrape_it_news():
    print("[IT 뉴스]")
    url = "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=105&sid2=230"
    soup = create_soup(url)
    news_list = soup.find("ul", attrs={'class':'type06_headline'}).find_all('li', limit=3) # 3개까지만 가져오기
    
    for idx, news in enumerate(news_list):
        a_idx = 0
        img = news.find("img")
        if img:
            a_idx = 1
        a_tag = news.find_all("a")[a_idx]
        title = a_tag.get_text().strip()
        link = url + a_tag['href']
        print_news(idx, title, link)
    print()

def scrape_english():
    print("[오늘의 영어 회화]")
    url = "https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=haceng_submain_lnb_eng_I_others_english&logger_kw=haceng_submain_lnb_eng_I_others_english"
    soup = create_soup(url)
    sentences = soup.find_all("div", attrs={'id':re.compile('^conv_kor_t')})
    print("(영어 지문)")
    for sentence in sentences[len(sentences)//2:]:
        print(sentence.get_text().strip())

    print() 
    print("(한글 지문)")
    for sentence in sentences[:len(sentences)//2]:
        print(sentence.get_text().strip())
    print()

if __name__ == "__main__":
    scrape_weather() # 오늘의 날씨 정보 가져오기
    scrape_headline_news() # 헤드라인 뉴스 정보 가져오기
    scrape_it_news() # IT 뉴스 정보 가져오기
    scrape_english() # 오늘의 영어 회화 가져오기