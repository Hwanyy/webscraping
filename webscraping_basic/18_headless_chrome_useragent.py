from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("widow-size=1920x1080")
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36")

browser = webdriver.Chrome('/Users/gimtaehwan/github/webscraping/webscraping_basic/webscraping_basic/chromedriver', options=options)
browser.maximize_window()

# 페이지 이동
url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent"
browser.get(url)

detected_value = browser.find_element_by_id("detected_value")
print(detected_value.text)
browser.quit()