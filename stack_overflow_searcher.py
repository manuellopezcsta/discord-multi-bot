from googlesearch import search


def get_results(search_term):
  """
  Returns Titulos + Results in 2 arrays
  """
  query = search_term + " site:stackoverflow.com"
  results = []
  titulos = []

  for result in search(query, num_results=4, lang="en"):
    #print(result)
    results.append(result)
  
  #print(results)
  for i in results:
    holder = i.split("/")
    # Hay 2 tipos de url, el que dice el num y dsps
    #el titulo y el q solo tira el numero.
    if(len(holder) == 6):
      holder = holder[5]
    else:
      holder = holder[4]
    #print(len(holder),holder)
    #print(holder)
    holder2 = holder.replace("-", " ")
    holder2 = holder2.capitalize()
    titulos.append(holder2)
  # Damos los 2 array
  return titulos,results