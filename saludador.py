import animales as listas


def saludar(texto):
  if(texto == "random"):
    result_string = listas.get_random()
    return result_string
  
  while("animal" in texto):
    holder = listas.get_animal()
    texto = texto.replace("animal", holder,1)
  #print(texto)
  while("adj" in texto):
    holder = listas.get_adj()
    texto = texto.replace("adj", holder,1)
  while("lugar" in texto):
    holder = listas.get_lugar()
    texto = texto.replace("lugar", holder,1)

  return texto
