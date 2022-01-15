import os
import requests


voiceRssToken = os.environ['voiceRSStoken']
url = "https://voicerss-text-to-speech.p.rapidapi.com/"

querystring = {"hl":"es-mx",
"src":"Banana",
"key": voiceRssToken,
"v":"Silvia",
"f":"8khz_8bit_mono",
"c":"mp3",
"r":"0"}

headers = {
    'x-rapidapi-host': "voicerss-text-to-speech.p.rapidapi.com",
    'x-rapidapi-key': "28bc09d5bemsh24a2ffe2179926bp123cfbjsn50951306425b"
    }

def GetAudio():
  response = requests.request("GET", url, headers=headers, params=querystring)
  print(response.text)




