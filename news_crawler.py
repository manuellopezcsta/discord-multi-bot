from bs4 import BeautifulSoup
import lxml
import requests

def crawl_news():
  """
  Returns titles array, and then links array
  """

  url = "https://www.genbeta.com/categoria/actualidad"
  headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
  }
  #Conseguimos la data
  f = requests.get(url, headers = headers)
  #La pasamos a un objeto.
  soup = BeautifulSoup(f.content,'lxml')
  #Empezamos a sacar los divs para conseguir la data que queremos
  recent = soup.find("div", {"class":"section-recent-list"})
  recent_articles = recent.find_all("article")
  # Creamos 2 array vacios para guardar los datos
  news_tittles = []
  news_links = []
  for movie in recent_articles:
    holder = movie.find("h2", {"class":"abstract-title"})
    holder_a = holder.find("a")["href"]
    holder_title = holder.find("a").contents[0]
    #print(holder_a)
    #print(holder_title)
    news_tittles.append(holder_title)
    news_links.append(holder_a)
  
  return news_tittles,news_links
  

def crawl_2():
  url = "https://news.ycombinator.com"
  headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
  }
  #Conseguimos la data
  f = requests.get(url, headers = headers)
  #La pasamos a un objeto.
  soup = BeautifulSoup(f.content,'lxml')
  #Empezamos a sacar los divs para conseguir la data que queremos
  recent = soup.find("table", {"class": "itemlist"})
  recent_articles = recent.find_all("tr", {"class": "athing"})

  news_tittles = []
  news_links = []

  #print("------------------------------------")
  for item in recent_articles:
    holder = item.find_all("td", {"class":"title"})
    holder2 = holder[1].find("a", {"class": "titlelink"})
    
    #print(holder2,",Holder 2")
    holder_a = holder2.get("href")
    holder_title = holder2.contents[0]
    #print(holder_a, ",Link")
    #print(holder_title,", Titulo")

    news_tittles.append(holder_title)
    news_links.append(holder_a)
    news_links2 = []
  
  #Reisamos si hay alguno onda item?id=29874669 y
  #lo cambiamos x la url verdadera
  for item in news_links:
    if(item[4]== "?" and item[6]=="d"):
      item = "https://news.ycombinator.com/"+ item
      news_links2.append(item)
      #print(item)
    else:
      news_links2.append(item)
      #Lo guardo en un nuevo array xq sino no queda
      #guardado
  
  return news_tittles,news_links2