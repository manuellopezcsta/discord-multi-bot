import discord


def create_embed():
  pic = "https://imagenes.elpais.com/resizer/ignf5hRqPoNrcNeilF3aB9CKy-M=/1960x0/cloudfront-eu-central-1.images.arcpublishing.com/prisa/HE3SMC3L7Z7XENXLHLLKE3CDEA.jpg"
  embed = discord.Embed(
    title = "Titulo",
    description = "Esta es la descripcion",
    colour = discord.Colour.blue()
  )
  embed.set_footer(text="This is a footer.")
  embed.set_image(url=pic)
  embed.set_thumbnail(url=pic)
  embed.set_author(name="Nombre de author",icon_url=pic)
  embed.add_field(name="Field Name", value="Field Value",inline=False)
  embed.add_field(name="Field Name", value="Field Value",inline=True)
  embed.add_field(name="Field Name", value="Field Value",inline=True)
  return embed


def help_embed():
  embed = discord.Embed(
    title = "Help Commands",
    description = "Aqui estan los comandos y que hace cada uno",
    colour = discord.Colour.blue()
  )
  embed.set_footer(text="If you break it plz message me ultragames007#1836.")
  embed.add_field(name="!help", value="Shows this help message",inline=False)
  embed.add_field(name="!setactive", value="Adds the Bot to the current channel.",inline=False)
  embed.add_field(name="!removeactive", value="Removes the Bot from the current channel.",inline=False)
  embed.add_field(name="!hello", value="Says hello back !",inline=False)
  embed.add_field(name="!a", value="A :D !",inline=False)
  embed.add_field(name="!saludo", value="Generates a greeting. Can be passed aguments like __!saludo Hola animal adj adj lugar . Como estas?__",inline=False)
  embed.add_field(name="!meme", value="Gives you a meme. can be passed a subbreddit and a quantity, max 25. __!meme sub quantity__",inline=False)
  embed.add_field(name="!easteregg", value="This does nothing.. believe me",inline=False)
  embed.add_field(name="!reset", value="Resets something.. I dont know what",inline=False)
  embed.add_field(name="!clear", value="Deletes 1 message. Can be passed args like this __!clear 5__ to delete more msgs. MAX is 100 ",inline=False)
  embed.add_field(name="!noticias", value="Shows you the latest news from genbeta.com",inline=False)
  embed.add_field(name="!noticias2", value="Shows you the latest news from news.ycombinator.com",inline=False)
  embed.add_field(name="!search", value="Searchs on stack overflow for results. Do __!search my question here__",inline=False)
  return embed

def help_embed_admin():
  embed = discord.Embed(
    title = "Help Commands",
    description = "Aqui estan los comandos admin y que hacen",
    colour = discord.Colour.blue()
  )
  embed.add_field(name="!resetacl", value="Admin Command. Resets ALL Active current channels",inline=False)
  embed.add_field(name="!checkacl", value="Admin Command. Prints a list of ALL Active current channels",inline=False)
  return embed

def news_embed(arr1,arr2):
  embed = discord.Embed(
    title = "News from Genbeta",
    description = "Aqui estan los titulares mas recientes.",
    colour = discord.Colour.blue()
  )

  for item in range(0,len(arr1)):
    link = "[--LINK--](" + arr2[item] + ")"
    #print(link)
    embed.add_field(name=arr1[item], value=link,inline=False)
  return embed

def search_embed(arr1,arr2,search_term):
  embed = discord.Embed(
    title = "Search Results",
    description = " ",
    colour = discord.Colour.blue()
  )

  for item in range(0,len(arr1)):
    link = "[--LINK--](" + arr2[item] + ")"
    embed.add_field(name=arr1[item], value=link,inline=False)
  
  st = search_term.replace(" ","+")
  href = "https://www.google.com/search?q=" +st + "+site%3Astackoverflow.com"
  embed.add_field(name="--MORE RESULTS--", value=href, inline=False)
  
  return embed

def news_embed2(arr1,arr2):
  embed = discord.Embed(
    title = "News from Hacker News",
    description = "Aqui estan los 5 titulares mas recientes.",
    colour = discord.Colour.blue()
  )

  for item in range(0,5):
    link = "[--LINK--](" + arr2[item] + ")"
    #print(link)
    embed.add_field(name=arr1[item], value=link,inline=False)
  href = "https://news.ycombinator.com/"
  embed.add_field(name="--MORE RESULTS--", value=href, inline=False)
  return embed