import discord
import os
from keep_alive import keep_alive
from saludador import saludar
from request_meme import GetMeme
from easter_egg import get_easteregg
from replit import db
import active_channels_manager as acm
import embed_gen as eg
import news_crawler as news
import stack_overflow_searcher as search
#import TTSRequest

#Creamos el cliente
client = discord.Client()
token = os.environ['token']
db["counter"] = "0"


# Funcion que va a correr el Bot
def get_greet(string="A"):
  message = string
  return message


#Creamos las funciones , los nombres son fijos de la documentacion.
#Cuando se prende
@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))


@client.event
async def on_guild_join(guild):
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            await channel.send('Felíz cumple Emi n.n ! Usa !help para aprender mas sobre mi :)')
        break

# How the bot responds when it gets a message
@client.event
async def on_message(message):
  if (message.author == client.user):
    return
  
  msg = message.content
  #counter = 0

  if(not msg.startswith("!")):
    return
  
  if (msg == "!help"):
    data = "Poner aca un cuadrito de ayuda con los comandos"
    embed_data = eg.help_embed()
    await message.channel.send(data,embed=embed_data)
    print("Se le mostro el cuadro de ayuda a", message.author)
  
  if (msg == "!helpadmin" and str(message.author.id) == os.environ['admin_id']):
     # Si sos el admin y pusiste el msg
    data = "Aca tenes Manu n.n !"
    embed_data = eg.help_embed_admin()
    await message.channel.send(data,embed=embed_data)
    print("Se le mostro comandos de admin a", message.author)
  
  if(msg == "!setactive"):
    idc = message.channel.id
    #print("El id del canal es:",idc)
    result = acm.add_channel_to_db(idc)
    if result:
      await message.channel.send("Se agrego este canal como activo. Ahora el bot funcionara aqui.")  
  
  if(msg == "!removeactive"):
    idc = message.channel.id
    #print("El id del canal es:",idc)
    result = acm.remove_channel_from_db(idc)
    if result:
      await message.channel.send("El bot , ya no respondera a este canal. Para activarlo aqui usa !setactive")
    #else:
      #await message.channel.send("Este canal no estaba activo.")      
    
  # DESPUES DE ESTOS 2 , siempre queremos controlar que el bot tenga permisos en
  # ese canal para ejecutar comandos.
  channel_state = acm.check_if_channel_is_active(message.channel.id)
  if(not channel_state):
    return
  ## Lo hacemos asi ^^ para no tener q meter todo en un while y que quede todo feo
  
  if(msg == "!resetacl"):
    result = acm.reset_active_channels(message.author.id)
    if result:
      await message.channel.send("Se reseteo todos los canales activos")
    else:
      await message.channel.send("Tu no eres un admin ¬¬ .. fuera")
  
  if(msg == "!checkacl"):
    result,lista = acm.check_active_channels_list(message.author.id)
    if result:
      print("Admin pidio lista, imprimiendo..")
      await message.channel.send(lista)
    else:
      await message.channel.send("Tu no eres un admin ¬¬ .. fuera")
    


  if msg.startswith("!hello"):
    await message.channel.send("Hello!")
    print("Se saludo a", message.author)

  if (msg == "!a"):
    data = get_greet()
    await message.channel.send(data)
    print("Se le dijo A! a", message.author)
  
  if msg.startswith("!saludo"):
    #data = "Hola lince Galactico!"
    # Si data es random dar un saludo random.
    saludo = msg.split("!saludo ",1)
    if(len(saludo) == 1):
      data = saludar("random")
    else:
      data = saludar(saludo[1])
    await message.channel.send(data)
    print("Se creo un saludo para", message.author)

  if msg.startswith("!meme"):
    arguments = msg.split("!meme ")
    if(len(arguments) == 2): # Si hay un sub seleccionado
      sub = arguments[1]
      #print("Sub", sub)
      new_sub = sub.split(" ")
      #print("New sub",new_sub)

      if(len(new_sub)==2): # Si da 2 es sub+cant
        sub = new_sub[0]
        cant = new_sub[1]
        url_meme = GetMeme(sub,cant)
      elif(len(new_sub)==1): # Si da 1 es sub
        url_meme = GetMeme(new_sub[0])
      elif(len(new_sub)>=3):
        url_meme = "Pasaste mal los argumentos, mira !help para ver como usar el comando."
        await message.channel.send(url_meme)
        return
    else: # Si no hay pedimos del comun
      url_meme = GetMeme()
    
    #If The sub has no posts with imgs..
    if("has no posts" in url_meme):
      await message.channel.send("This subreddit has no Posts with Images")
      return
    if("try again" in url_meme):
      await message.channel.send("Unknown error, please try again.")
      return
    if("does not exist" in url_meme):
      await message.channel.send("This subreddit does not exist.")
      return
    if("Unable" in url_meme):
      await message.channel.send("Unable to access Subreddit. Subreddit is locked or private.")
      return

    #print(url_meme)
    #Mandamos el msg
    for x in range(len(url_meme)):
      await message.channel.send(url_meme[x])
    print("Se le dieron",len(url_meme),"memes a",message.author)
  
  if ((msg == "!easteregg") and int(db["counter"]) <= 14):
    counter = int(db["counter"])
    msg = get_easteregg(counter)
    counter += 1
    db["counter"] = counter
    #print(counter) #For Debbuging.
    await message.channel.send(msg)
  
  if(msg == "!reset"):
    db["counter"] = 0
    msg = "Se reseteo el counter del easter egg"
    print("Se reseteo el counter del Easter Egg")
    await message.channel.send(msg)
  
  if(msg.startswith("!clear")):
    #Capturamos la cantidad de mensajes a limpiar
    num = msg.split("!clear ",1)
    if(len(num) == 1):
      limit = 2 #X defecto borra 1 solo
    else:
      limit = int(num[1]) + 1
    if(limit> 101):
      msg = "Intenta con un numero menor a 100"
      await message.channel.send(msg)
      return
    print("Se eliminaron",limit,"mensajes")
    await message.channel.purge(limit=limit)
  
  if(msg == "!noticias"):
    #Pedimos las noticias
    arr1,arr2 = news.crawl_news()
    #Mandamos los msgs
    embed_data = eg.news_embed(arr1,arr2)
    print("Se le mostraron las noticias a",message.author)
    await message.channel.send(embed=embed_data)
  
  if(msg == "!noticias2"):
    #Pedimos las noticias
    arr1,arr2 = news.crawl_2()
    #Mandamos los msgs
    embed_data = eg.news_embed2(arr1,arr2)
    print("Se le mostraron las noticias2 a",message.author)
    await message.channel.send(embed=embed_data)
  
  if(msg.startswith("!search ")):
    search_term = msg.split("!search ")[1]
    #print("Search term:", search_term)
    arr1,arr2 = search.get_results(search_term)
    embed_data = eg.search_embed(arr1,arr2,search_term)
    print("Se le mostraron resultados de busqueda a",message.author)
    await message.channel.send(embed=embed_data)
    


#Ping the server so it doesnt sleep
keep_alive()
#Line to run the Bot
try:
  client.run(token)
except Exception as error:
  print(error)
