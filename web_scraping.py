import requests #wwb sayfa ya talep göndermek için kullanılır

response=requests.get("http://ktun.edu.tr") #istek yapılır ve cevap response nesnesine atanır
print("status Code:",response.status_code)
print("headers:",response.headers)
print(response.text[:200])

params={"query":"sait ali uymaz","source":"chrome"}
response=requests.get("http://www.google.com/search",params=params)
#parametre gondermek için params kullanılır
from bs4 import BeautifulSoup #kutuphane HTML ve XML dosyalarını işlemek için kullanılır

soup=BeautifulSoup(response.text,"html5lib")
"""python içerisindeki dahili parser kütüphanesi veya 
3. parti kütüphaneler kullanılabilir."""
all_urls=[a['href'] #web sayfadaki linkleri topladık
            for a in soup('a')
            if a.has_attr('href')]
print(len(all_urls)) #kac tane oldugunu
print(soup.title.text)  #başlıkları
print(soup.find("a").text)