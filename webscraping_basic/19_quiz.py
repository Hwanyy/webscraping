import requests
from bs4 import BeautifulSoup

url = "https://search.daum.net/search?w=tot&DA=UME&t__nil_searchbox=suggest&sug=&sugo=15&sq=%EC%86%A1%ED%8C%8C+%ED%97%AC%EB%A6%AC%EC%98%A4%EC%8B%9C%ED%8B%B0&o=1&q=%EC%86%A1%ED%8C%8C+%ED%97%AC%EB%A6%AC%EC%98%A4%EC%8B%9C%ED%8B%B0"

res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')

houses = soup.find("tbody").find_all('tr')

for idx, house in enumerate(houses):    
    # print(house.find('td', attrs={'class':'col1'}).get_text())
    # print(house)
    # print('='*30)
    
    type_ = house.find('td', attrs={'class':'col1'}).get_text().strip()
    size = house.find('td', attrs={'class':'col2'}).get_text().strip()
    price = house.find('td', attrs={'class':'col3'}).get_text().strip()
    dong = house.find('td', attrs={'class':'col4'}).get_text().strip()
    ho = house.find('td', attrs={'class':'col5'}).get_text().strip()
    print('='*11+f'매물{idx+1}'+'='*11)
    print('거래 : ', type_, '(공급/전용)')
    print('가격 : ', price, '(만원)')
    print('동 : ', dong)
    print('호 : ', ho)
