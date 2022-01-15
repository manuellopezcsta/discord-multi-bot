import random


animal_list = ["Abeja","Abejorro","Águila","Albatros","Alce","Almeja",
"Anguila","Antílope","Arenque","Armadillo","Asno","Atún","Avestruz",
"Babuino","Bacalao","Ballena","Barracuda","Beluga","Bisonte","Boa",
"Bonobo","Buey","Búfalo","Búho","Buitre","Burro","Caballo","Caballito de mar",
"Cacatúa","Camaleón","Camello","Canguro","Canario","Cangrejo","Caracol","Castor",
"Cebra","Chacal","Chimpancé","Chinchilla","Ciervo","Cigala","Cisne","Cochinilla",
"Cocodrilo","Colibrí","Comadreja","Conejo","Cóndor","Coyote","Delfín","Dingo","Dragón de Komodo","Elefante","Emú","Equidna","Erizo","Estrella de mar","Faisán",
"Flamingo","Foca","Gacela","Gallina","Gallo","Ganso","Garza","Gato","Gavilán",
"Golondrina","Gorila","Gorrión","Grulla","Guepardo","Halcón","Hamster","Hiena",
"Hipopótamo","Hormiga","Hurón","Iguana","Jabalí","Jirafa","Jaguar","Kiwi","Koala",
"Lagarto","Lechuza","Lémur","León","Leopardo","Liebre","Lince","Llama","Lobo","Loro",
"Luciérnaga","Mamut","Mandril","Mapache","Mariposa","Marmota","Medusa","Mono","Murciélago","Nutria","Ñandú","Ocelote","Oso","Oso panda","Ornitorrinco","Oveja","Pájaro","Paloma","Pantera","Pelicano","Perico","Perro","Pez","Pingüino","Puercoespín","Pulpo","Puma","Rana","Rata","Ratón","Reno","Rinoceronte","Ruiseñor","Salamandra","Saltamontes","Sapo","Serpiente","Tejón","Tiburón","Tigre","Topo","Toro","Tortuga","Tritón","Trucha","Tucán","Urraca","Vaca","Venado","Wombat","Yacare","Zorro","Zebra"]

adj_list = ["Maestro","Maquina","Voladora","Titan","Guerrero","Exterminador","Rufian","Cowboy","Monstruo","Simpático","Limpio","Sutil","Grande","Hábil","Amable",
"Alto","Maravilloso","Inteligente","Colorido","Agradable","Transparente","Peludo",
"Aburrido","Rápido","Galactico/a","Volador/a","Cambiaformas"]

lugar_list = ["del Oeste", "de Narnia", "de Github","del Sur","del Norte","del Este",
"de Hogwarts","de la Atlantida","de Tierra Media","de los Andes","de la Patagonia","del Internet","del Nilo","de Taringa","de Reddit","de Tiktok","de Instagram",
"de Youtube","del viejo Oeste","de Oriente","de Roma","de Chacarita","del Minecraft"]

random_list = ["Hola, Lince Galactica!",
"Buen día Codorniz cuantica Italiana",
"Que haces Manati Narniano de Chocolomo",
"Buenaaaaas Mono Titi de las Praderas!",
"Jojo como va ? Todo bien amigo de los mapaches?",
"Ehhhh ! es el caballo brillante del sur bailarin",
"Buenas guepardo digital del cuadrante Oeste de Github!"]


def get_animal():
  result = random.choice(animal_list)
  return result

def get_adj():
  result = random.choice(adj_list)
  return result

def get_lugar():
  result = random.choice(lugar_list)
  return result

def get_random():
  result = random.choice(random_list)
  return result