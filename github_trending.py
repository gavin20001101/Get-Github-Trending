import requests
from bs4 import BeautifulSoup
from googletrans import Translator

# GitHub趨勢頁面的URL
url = "https://github.com/trending?since=daily&spoken_language_code="

# https://steam.oxxostudio.tw/category/python/spider/beautiful-soup.html#a3
# https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/#find-all
web = requests.get(url)                        # 取得網頁內容
soup = BeautifulSoup(web.text, "html.parser")  # 轉換成標籤樹
h2 = soup.find_all("h2","h3 lh-condensed") # 取得所有 h2 標籤
p = soup.find_all("p","col-9 color-fg-muted my-1 pr-4")   # 取得所有 p 標籤

# https://bbs.mnya.tw/d/8670-python-shi-fou-you-ke-yi-ying-fan-zhong-de-fan-yi-gong-ju
translator = Translator()                      # 建立翻譯器

for i in range(0, 14):
    print(i+1,end="")                            # 印出編號
    print(". ",end="")                           # 印出點
    print(h2[i].a['href'])                         # 印出 h2 -> a -> href 標籤的文字
    p_text = p[i].get_text()                         # 印出 p 標籤的文字
    translation = translator.translate(p_text, dest='zh-tw') # 翻譯成中文
    print(f" {p_text}")                       # 印出原始文字
    print(f"      {translation.text}")             # 印出翻譯後的文字
    print()
    
