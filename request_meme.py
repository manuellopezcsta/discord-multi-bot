import requests
import json


#Credit to https://github.com/D3vd/Meme_Api for the API.

api_request_limit = 25 # El real es 50, pero uso menos x las dudas

def GetMeme(subreddit="",quantity="1"):
  if(int(quantity) > api_request_limit):
    quantity = str(api_request_limit)
  url = "https://meme-api.herokuapp.com/gimme/"+quantity

  if(subreddit != ""):
    url = "https://meme-api.herokuapp.com/gimme/" + subreddit +"/" + quantity
  
  #print(url)
  response = requests.get(url).text
  #print(response)
  response_info = json.loads(response)
  #print(response_info.keys()) # Nos fijamos las keys

  meme_url = []

  # Nos fijamos si existe el subreddit , revisando la respuesta del server
  #print(response_info.keys())
  if("message" in response_info.keys()):
    #print("Sub no existe")
    meme_url.append(response_info["message"])
    print("Error comun:",meme_url[0])
    return meme_url[0]

  quantity = int(quantity)
  realQuantity = str(response_info["count"])
  # Si el sub existe se ejecuta esto para agarrar el meme
  #print(response_info["memes"][0]["url"])
  
  for x in range(int(realQuantity)):
    meme_url.append(response_info["memes"][x]["url"])
  if(int(realQuantity) != int(quantity)):
    meme_url.append("Sorry, the API could not retrieve that quantity.This is all we got :c")
  #print("Meme Comun:",meme_url)
  return meme_url



